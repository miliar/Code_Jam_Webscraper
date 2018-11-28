#include<stdio.h>
#include<string.h>

const int maxn = 1005;

int n,m,d;

char a[maxn][maxn];
int a1[maxn][maxn];
int a2[maxn][maxn];
long long s1[maxn][maxn];
long long s2[maxn][maxn];
long long s[maxn][maxn];

bool balance(int x, int y, int k)
{
	if(x==2 && y==2 && k==5)
	{
		k = k;
	}
	long long sum = s[x+k-1][y+k-1] - s[x-1][y+k-1] - s[x+k-1][y-1] + s[x-1][y-1] - a[x][y] - a[x+k-1][y] - a[x][y+k-1] - a[x+k-1][y+k-1];
	long long sum1 = s1[x+k-1][y+k-1] - s1[x-1][y+k-1] - s1[x+k-1][y-1] + s1[x-1][y-1] - a1[x][y] - a1[x+k-1][y] - a1[x][y+k-1] - a1[x+k-1][y+k-1];
	long long sum2 = s2[x+k-1][y+k-1] - s2[x-1][y+k-1] - s2[x+k-1][y-1] + s2[x-1][y-1] - a2[x][y] - a2[x+k-1][y] - a2[x][y+k-1] - a2[x+k-1][y+k-1];
	long long u1, u2;

	if(k % 2 == 0)
	{
		u1 = sum1 - sum * (x*2+k-1);
		u2 = sum2 - sum * (y*2+k-1);
	}
	else
	{
		u1 = sum1 - sum * (x*2+k-1);
		u2 = sum2 - sum * (y*2+k-1);
	}

	return u1 == 0 && u2 == 0;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int ntest;
	scanf("%d", &ntest);
	for(int test=1; test<=ntest; test++)
	{
		fprintf(stderr, "%d\n", test);
		scanf("%d%d%d", &n, &m, &d);
		for(int i=1; i<=n; i++)
		{
			scanf("%s", a[i]+1);
			for(int j=1; j<=m; j++)
			{
				a[i][j] -= '0';
				a1[i][j] = a[i][j] * i * 2;
				a2[i][j] = a[i][j] * j * 2;
				s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j];
				s1[i][j] = s1[i-1][j] + s1[i][j-1] - s1[i-1][j-1] + a1[i][j];
				s2[i][j] = s2[i-1][j] + s2[i][j-1] - s2[i-1][j-1] + a2[i][j];
			}
		}

		int ans = 2;

		for(int i=1; i<=n; i++)
			for(int j=1; j<m; j++)
			{
				for(int k=ans+1; i+k<=n+1 && j+k<=m+1; k++)
				{
					if(balance(i,j,k))
						ans = k;
				}
			}

		fprintf(stderr, "%d\n", test);
		printf("Case #%d: ", test);
		if(ans == 2) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}

	return 0;
}
