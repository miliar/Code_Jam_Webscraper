#include <iostream>
#include <set>
using namespace std;
const int MAX = 1000005;

long long n, A, B, C, D, x0, y0, m;
long long dp[5][5];//, dp2[5][5], dp3[5][5];
struct POINT
{
	long long x, y;
}points[MAX];

int main (void)
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	long long Case = 1, T;
	scanf("%lld", &T);
	while (T --)
	{
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &m);
		int i, j, k, ii, jj, kk;
		points[0].x = x0; points[0].y = y0;
		memset(dp, 0, sizeof(dp));
		for (i = 1; i < n; ++ i)
		{
			points[i].x = (A*points[i-1].x + B) % m;
			points[i].y = (C*points[i-1].y + D) % m;
		}
		for (i = 0; i < n; ++ i)
			dp[points[i].x%3][points[i].y%3] ++ ;

		long long ans = 0, temp;
		for (i = 0; i < 3; ++ i)
			for (ii = 0; ii < 3; ++ ii)
				for (j = 0; j < 3; ++ j)
					for (jj = 0; jj < 3; ++ jj)
						for (k = 0; k < 3; ++ k)
							for (kk = 0; kk < 3; ++ kk)
							{
								if((i+j+k) % 3 || (ii+jj+kk) % 3)
									continue;
								if(i==j && j==k && ii==jj && jj==kk)
									temp = dp[i][ii]*(dp[j][jj]-1)*(dp[k][kk]-2);
								else if(i==j && ii==jj)
									temp = dp[i][ii]*(dp[j][jj]-1)*(dp[k][kk]);
								else if(j==k && jj==kk)
									temp = dp[i][ii]*(dp[j][jj])*(dp[k][kk]-1);
								else if(i==k && ii==kk)
									temp = dp[i][ii]*(dp[j][jj])*(dp[k][kk]-1);
								else
									temp = dp[i][ii]*(dp[j][jj])*(dp[k][kk]);
								if(temp < 0) temp=0;
									ans += temp;
							}

		printf("Case #%lld: %lld\n", Case++, ans / 6);
	}
	return 0;
}