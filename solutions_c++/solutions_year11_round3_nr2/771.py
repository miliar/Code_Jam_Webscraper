# include <iostream>
# include <string>
# include <fstream>
# include <vector>
# include <algorithm>
using namespace std;

int main()
{
	ifstream cin("CBB.in");
	ofstream cout("CBB.out");
	int T = 0;
	cin >> T;
	int casenum = 0;
	while(T - casenum)
	{
		int n, c, l;
		long long t;
		cin >> l >> t >> n >> c;
		vector<long long> dists(n);
		vector<long long> disthelpers(c);

		for(int i = 0; i < c; ++i)
			cin >> disthelpers[i];

		vector<long long> dists0(n + 1, 0);
		
		for(int i = 0; i < n; ++i)
		{
			dists[i] = disthelpers[i % c] ;
			dists0[i + 1] = dists0[i] + dists[i];
		}

		long long ans = dists0[n] * 2;
		if(l == 1)
		{
			for(int j = 0; j < n; ++j)
			{
				long long res = dists0[n] * 2;
				long long tmp_t = dists0[j] * 2;
				if(tmp_t >= t)
					res -= dists[j];
				else if(tmp_t + 2 * dists[j] >= t)
				{
					res -= dists[j] - (t - tmp_t) / 2;
				}
				ans = min(ans, res);
			}
		}
		else if(l == 2)
		{
			for(int i = 0; i < n; ++i)
				for(int j = i + 1; j < n; ++j)
				{
					long long res = 2 * dists0[n];
					long long tmp_t = 2 * dists0[i];
					if(tmp_t >= t)
						res -= dists[i] + dists[j];
					else if(tmp_t + 2 * dists[i] >= t)
					{
						res -= dists[i] - (t - tmp_t) / 2;
						res -= dists[j];
					}
					else
					{
						tmp_t = dists0[j] * 2;
						if(tmp_t >= t)
							res -= dists[j];
						else if(tmp_t + 2 * dists[j] >= t)
						{
							res -= dists[j] - (t - tmp_t) / 2;
						}
					}

					ans = min(ans, res);
				}
		}
		casenum++;
		cout << "Case #" << casenum << ": " << ans << endl;
	}
	return 0;
}
