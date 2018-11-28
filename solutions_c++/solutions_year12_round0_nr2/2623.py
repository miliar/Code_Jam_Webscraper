#include "stdio.h"
#include "string.h"

#define MAX_N 100
#define MAX_S 30
#define S_T 1
#define S_L 2
#define N_T 4
#define N_L 8
#define MAX_M 16

int ans, n, s, p;
int m[MAX_S * 3 + 1];
int c[MAX_M];
int a[MAX_N];

void dfs(int n, int s, int np)
{
	if(n < 0)
	{
		if(s == 0 && np > ans)
			ans = np;
		return;
	}
	if((m[a[n]] & N_T) == N_T)
		dfs(n - 1, s, np + 1);
	if((m[a[n]] & N_L) == N_L)
		dfs(n - 1, s, np);
	if(s)
	{
		if((m[a[n]] & S_T) == S_T)
			dfs(n - 1, s - 1, np + 1);
		if((m[a[n]] & S_L) == S_L)
			dfs(n - 1, s - 1, np);
	}
}

int main()
{
	freopen("b.in", "r", stdin);
	int N, t; // t[MAX_N];
	scanf("%d", &N);
	for(int T = 1; T <= N; T ++)
	{
		memset(m, 0, sizeof(m));
		memset(c, 0, sizeof(c));
		scanf("%d%d%d", &n, &s, &p);
		for(int i = 0; i <= MAX_S; i ++)
			for(int j = i; j <= MAX_S && j < i + 2; j ++)
				for(int k = j; k < i + 2 && k <= MAX_S; k ++)
				{
					int s = i + j + k;
					if(k >= p)
						m[s] |= N_T;
					else
						m[s] |= N_L;
				}
		for(int i = 0; i + 2 <= MAX_S; i ++)
			for(int j = i; j <= i + 2; j ++)
			{
				int s = i + j + i + 2;
				if(i + 2 >= p)
					m[s] |= S_T;
				else
					m[s] |= S_L;
			}
		for(int i = 0; i < n; i ++)
		{
			scanf("%d", &t);
			a[i] = t;
			c[m[t]] ++;
		}
		ans = 0;
		dfs(n - 1, s, 0);
		printf("Case #%d: %d\n", T, ans);
	}
	return 0;
}
