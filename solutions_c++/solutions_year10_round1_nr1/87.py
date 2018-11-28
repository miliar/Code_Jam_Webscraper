#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const long maxn = 110;
const long w[4][2] = {{-1, 0}, {0, 1}, {-1, -1}, {-1, 1}};

char g[maxn][maxn];
long n, k, t;
long flag;

void init()
{
	scanf("%ld%ld", &n, &k);
	for (long i = 0; i < n; ++i) scanf("%s", g[i]);
}

void rotate()
{
	for (long i = 0; i < n; ++i)
		for (long l, j = n-1; j >= 0; --j)
			if (g[i][j] != '.')
			{
				for (l = j+1; l < n && g[i][l] == '.'; ++l);
				g[i][l-1] = g[i][j];
				if (l-1 != j) g[i][j] = '.';
			}
}

void cal(long fa)
{
	for (long i = 0; i < n; ++i)
		for (long l, j = 0; j < n; ++j)
			if (g[i][j] != '.')
			{
				long x = i, y = j;
				for (l = 1, x+=w[fa][0], y+=w[fa][1]; 0 <= x && x < n && 0 <= y && y < n && g[x][y] == g[i][j]; ++l)
				{
					x+=w[fa][0], y+=w[fa][1];
				}
				
				if (l >= k)
				{
					if (g[i][j] == 'B') flag = flag | 1;
					else flag = flag | 2;
				}
			}
}

void solve()
{
	rotate();
	
	flag = 0;
	for (long l = 0; l < 4; ++l)
		cal(l);
	
	if (flag == 0) printf("Neither\n");
	if (flag == 3) printf("Both\n");
	if (flag == 1) printf("Blue\n");
	if (flag == 2) printf("Red\n");
}

int main()
{
	freopen("AL.in", "r", stdin);
	freopen("AL.out", "w", stdout);
	scanf("%ld", &t);
	for (long l = 1; l <= t; ++l)
	{
		init();
		printf("Case #%ld: ", l);
		solve();
	}
	return 0;
}
