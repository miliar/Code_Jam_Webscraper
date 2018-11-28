#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <cstring>
#include <cassert>

using namespace std;

int b[1010], e[1010], w[1010];

int t[1010];
bool cmp(const int x, const int y){ return w[x] < w[y]; }

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int icase=1; icase<=cases; ++icase)
	{
		double res = 0.0;
		int X, S, R, T, N;
		scanf("%d%d%d%d%d", &X, &S, &R, &T, &N);
		assert(N<=1000);
		for(int i=0; i<N; ++i) scanf("%d%d%d", &b[i], &e[i], &w[i]);

		int n = N;
		int sum = 0;
		sum += b[0];
		for(int i=1; i<n; ++i) sum += b[i]-e[i-1];
		sum += X - e[n-1];
		
		if(R * T <= sum)
		{
			res = T;
			res += (double)(sum - T*R) / S;
			for(int i=0; i<n; ++i) res += double(e[i]-b[i]) / (S + w[i]);
		}
		else
		{
			res = double(sum) / R;
			double left = T - res;
			
			for(int i=0; i<n; ++i) t[i] = i;
			sort(t, t+n, cmp);
			for(int i=0; i<n; ++i)
			{
				int nr = t[i];
				
				double dist = e[nr]-b[nr];
				if(dist/(R+w[nr]) <= left){ res += dist/(R+w[nr]); left -= dist/(R+w[nr]); }
				else
				{
					res += left;
					dist -= left * (R+w[nr]);
					left = 0.0;
					res += dist/(S+w[nr]);
				}
			}
		}
		
		printf("Case #%d: %.9lf\n", icase, res);
	}
	return 0;
}
