#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
int C;
int N,K,B,T;
int dp[60];
int xi[60];
int vi[60];
int main()
{
	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B-large.out","w",stdout);
	
	//freopen("..\\A.in","r",stdin);
	
	scanf("%d",&C);
	for(int t = 1;t <= C;t++)
	{
		scanf("%d %d %d %d", &N, &K, &B, &T);
		for(int i = 0;i < N;i++)
			scanf("%d", &xi[i]);
		for(int i = 0;i < N;i++)
			scanf("%d", &vi[i]);

		memset(dp, 255, sizeof(dp));
		for(int i = N - 1;i >= 0;i--)
		{
			double qq = (double)(B - xi[i]) / vi[i];
			if(qq <= (double)T)
			{
				int num = 0;
				for(int j = i + 1;j < N;j++)
				{
					if(dp[j] < 0)
						num++;
					if(dp[j] >= 0)
					{
						num += dp[j];
						break;
					}
				}
				dp[i] = num;
			}
		}
		sort(dp, dp + N);
		int res = 0;
		int numR = 0;
		for(int i = 0;i < N;i++)
		{
			if(dp[i] >= 0)
			{
				numR++;
				res += dp[i];
			}
			if(numR == K)
				break;
		}
		if(numR == K)
			printf("Case #%d: %d\n", t, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
	return 0;
}