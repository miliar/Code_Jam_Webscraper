#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
#define MM(a , x) memset(a , x , sizeof(a))
#define sqr(x) ((x) * (x))
#define abs(x) ((x > 0) ? (x) : -(x))
#define REP(i , n) for ((i) = 0; (i) < (n); ++(i))
#define FOR(i , a , b) for ((i) = (a); (i) <= (b); ++(i))
#define FORD(i , a , b) for ((i) = (a); (i) >= (b); --(i))
typedef long long LL;

int n , m , tot , T , testcase;
double ans , f[3][108] , dp[108];
int g[108][108] , game[108];

void init()
{
	scanf("%d\n" , &n);
	int i , j , k;
	char ch;
	MM(g , 255); MM(game , 0);
	FOR (i , 1 , n)
	{
		k = n;
		FOR (j , 1 , n)
		{
			ch = getchar();
			if (ch == '1') g[i][j] = 1;
			if (ch == '0') g[i][j] = 0;
			if (ch == '.') k--;
		}
		ch = getchar();
		game[i] = k;
	}
}

void work()
{
	int i , j , k , tp , now , x , y;
	MM(f , 0);
	FOR (i , 1 , n)
	{
		k = 0;
		FOR (j , 1 , n)
		{
			if (g[i][j] == 1) k++;
		}
		f[0][i] = (double)k / (double)game[i];
	}
	FOR (i , 1 , n)
	{
		MM(dp , 0);
		FOR (j , 1 , n)
		{
			int win = 0 , cnt = 0;
			if (j == i) continue;
			FOR (k , 1 , n)
			{
				if (k == i) continue;
				if (g[j][k] != -1) cnt++;
				if (g[j][k] == 1) win++;
			}
			dp[j] = (double)win / (double)cnt;
		}
		FOR (j , 1 , n)
		{
			if (g[i][j] != -1)
			{
				f[1][i] += dp[j] / (double)game[i];
			}
		}
	}
	FOR (i , 1 , n)
	{
		FOR (j , 1 , n)
		{
			if (g[i][j] != -1)
			{
				f[2][i] += f[1][j] / (double)game[i];
			}
		}
	}
	printf("Case #%d:\n" , T);
	FOR (i , 1 , n) printf("%.7lf\n" , 0.25 * f[0][i] + 0.5 * f[1][i] + 0.25 * f[2][i]);
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	scanf("%d\n" , &testcase);
	FOR (T , 1 , testcase)
	{
		init();
		work();
	}
	return 0;
}
