#include<cstdio>
#include<cstring>
const int maxn = 30;
int a[100][100];
int b[30][30];

bool judge(int n)
{
	int i , j;
	for(i = 1;i <= 2 * n - 1;i++)
		for(j = 1;j <= 2 * n - 1;j++)
		{
			if(a[i][j] != -1 && a[i][2 * n - j] != -1 && a[i][j] != a[i][2 * n - j]) return false;
			if(a[i][j] != -1 && a[2 * n - i][j] != -1 && a[i][j] != a[2 * n - i][j]) return false;
		}
	return true;
}

bool build(int n , int m)
{
	int i , j;
	for(i = 1;i <= n - m + 1;i++)
	{
		for(j = n + 1 - i;j <= n - 1 + i;j = j + 2)
		{
			memset(a , -1 , sizeof(a));
			int x = i - 1 , y = j - m;
			int k , l;
			for(k = 1;k <= 2 * m - 1;k++)
				for(l = 1;l <= 2 * m - 1;l++)
					a[k + x][l + y] = b[k][l];
			if(judge(n)) return true;
		}
	}
	for(;i <= 2 * n - 2 * m + 1;i++)
	{
		for(j = n + 1 - (2 * n - 2 * m + 2 - i);j <= n - 1 + (2 * n - 2 * m + 2 - i);j = j + 2)
		{
			memset(a , -1 , sizeof(a));
			int x = i - 1 , y = j - m;
			int k , l;
			for(k = 1;k <= 2 * m - 1;k++)
				for(l = 1;l <= 2 * m - 1;l++)
					a[k + x][l + y] = b[k][l];
			if(judge(n)) return true;
		}
	}
	return false;
}

int solve(int m)
{
	int n = m;
	while(1)
	{
		if(build(n , m)) return n;
		n++;
	}
}

int main()
{
//	freopen("A-small-attempt2.in" , "r" , stdin);
//	freopen("1.txt" , "w" , stdout);
	int t;int p;
	scanf("%d" , &t);
	for(p = 1;p <= t;p++)
	{
		memset(b , -1 , sizeof(b));
		int i , j;
		int n;
		scanf("%d" , &n);
		for(i = 1;i <= n;i++)
		{
			for(j = n + 1 - i;j <= n - 1 + i;j = j + 2)
			{
				scanf("%d" , &b[i][j]);
			}
		}
		for(;i <= 2 * n - 1;i++)
		{
			for(j = n + 1 - (2 * n - i);j <= n - 1 + (2 * n - i);j = j + 2)
			{
				scanf("%d" , &b[i][j]);
			}
		}
		int temp = solve(n);
		printf("Case #%d: %d\n" , p , temp * temp - n * n);
	}
	return 0;
}
