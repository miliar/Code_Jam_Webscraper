#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <vector>
#define _min(a, b) ((a) < (b) ? (a) : (b))
#define _max(a, b) ((a) > (b) ? (a) : (b))
using namespace std;

int dp[1010][1010];
int dp1[1010][1010];
int L, P, C;

int f(int a, int b)
{
	if(a * C >= b)
		return dp[a][b] = 0;
	if(dp[a][b] != -1)
		return dp[a][b];
	dp[a][b] = 0x7fffffff;
	int des;
	_int64 cur = a * C;
	for(cur = a; cur < b; cur *= C)
	{
		int t;
		if(dp[a][b] > (t = _max(f(a, cur), f(cur, b))))
		{
			dp[a][b] = t + 1;
			des = cur;
		}
	}
	return dp[a][b];
}

/*int ff(int a, int b)
{
	if(a * C >= b)
		return dp1[a][b] = 0;
	if(dp1[a][b] != -1)
		return dp1[a][b];
	dp1[a][b] = 0x7fffffff;
	int des, cur;
	for(cur = a + 1; cur < b; cur++)
	{
		int t;
		if(dp1[a][b] > (t = _max(f(a, cur), f(cur, b))))
		{
			dp1[a][b] = t + 1;
			des = cur;
		}
	}
	return dp1[a][b];
}*/

int main()
{
	freopen("A_in.txt", "r", stdin);
	freopen("A_out.txt", "w", stdout);
	int T, cas;
	for(scanf("%d", &T), cas = 1; cas <= T; cas++)
	{
//		mp.clear();
		scanf("%d%d%d", &L, &P, &C);
		memset(dp, -1, sizeof(dp));
//		memset(dp1, -1, sizeof(dp1));
//		printf("f1 = %d, f2 = %d\n", f(L, P), ff(L, P));
		printf("Case #%d: %d\n", cas, f(L, P));
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}


