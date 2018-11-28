#include<iostream>
#include<utility>
#include<vector>
#include<cmath>

using namespace std;

typedef pair<int,int> PII;

vector<PII> blue,orange;

int n;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		blue.clear();
		orange.clear();

		cin>>n;
		for(int i=0;i<n;i++)
		{
			char c;
			int x;
			cin>>c>>x;
			if (c=='B') blue.push_back(PII(i,x));
			else orange.push_back(PII(i,x));
		}
		int ci = 0,t=0,bp = 1, op = 1, bi = 0, oi = 0;
		while(ci!=n)
		{
			++t;
			bool push=false;;
			if (bi<blue.size())
			{
				if (bp!=blue[bi].second) bp-=(bp-blue[bi].second)/abs(bp-blue[bi].second);
				else if (ci==blue[bi].first) { push = true; ++bi; }
			}

			if (oi<orange.size())
			{
				if (op!=orange[oi].second) op-=(op-orange[oi].second)/abs(op-orange[oi].second);
				else if (ci==orange[oi].first) { push = true; ++oi; }
			}
			if (push) ++ci;
		}
		printf("Case #%d: %d\n",tt,t);

	}
	return 0;
}
