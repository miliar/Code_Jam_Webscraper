#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <memory>
#include <map>

using namespace std;

int N,M;

pair<long long,int> nmas[110];
pair<long long,int> mmas[110];

vector<pair<long long,long long> > results[110];

long long Run()
{
	for (int i=0; i<=N; i++)
	{
		results[i].clear();
	}

	results[0].push_back(make_pair(0,0));

	for (int i=0; i<N; i++)
	{
		for (int j=0; j<=i; j++)
		{
			for (int k=0; k<results[j].size(); k++)
			{
				long long locres = 0;
				long long pos = 0;
				long long need = nmas[i].first;
				long long added = 0;
				for (int p=0; p<M; p++)
				{
					if (pos+mmas[p].first > results[j][k].first)
					{
						if (mmas[p].second == nmas[i].second)
						{
							long long locPos = pos;
							long long canAdd = mmas[p].first;
							if (results[j][k].first > pos)
							{
								canAdd = pos+mmas[p].first - results[j][k].first;
								locPos = results[j][k].first;
							}

							if (canAdd > need)
							{
								canAdd = need;
							}
							results[i+1].push_back(make_pair(locPos+canAdd,results[j][k].second+canAdd+added));
							added += canAdd;
							need -= canAdd;
						}
					}
					pos += mmas[p].first;
				}
			}
		}

		map<long long, long long> m;
		for (int j=0; j<results[i+1].size(); j++)
		{
			if (m.find(results[i+1][j].first) == m.end() || m[results[i+1][j].first] < results[i+1][j].second)
				m[results[i+1][j].first] = results[i+1][j].second;
		}

		results[i+1].clear();
		results[i+1].assign(m.begin(),m.end());
	}

	long long res = 0;
	for (int i=0; i<=N; i++)
	{
		for (int j=0; j<results[i].size(); j++)
		{
			if (results[i][j].second > res)
				res = results[i][j].second;
		}
	}
	return res;
}

int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		cerr<<"Test :"<<t<<endl;
		scanf("%d%d", &N, &M);
		for (int i=0; i<N; i++)
		{
			long long f;
			int s;
			scanf("%lld%d", &f, &s);
			nmas[i] = make_pair(f,s);
		}
		for (int i=0; i<M; i++)
		{
			long long f;
			int s;
			scanf("%lld%d", &f, &s);
			mmas[i] = make_pair(f,s);
		}
		long long res = Run();
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}