#include<stdio.h>
#include<algorithm>
using namespace std;

int bitx[512][512];
int bity[512][512];
int bitm[512][512];
int m[512][512];
int r, c;

int getx(int y, int x)
{
	int ans = 0, X = x;
	while (y > 0)
	{
		x = X;
		while (x > 0)
		{
			ans += bitx[y][x];
			x -= x&(-x);
		}
		y -= y&(-y);
	}
	return ans;
}

int gety(int y, int x)
{
	int ans = 0, X = x;
	while (y > 0)
	{
		x = X;
		while (x > 0)
		{
			ans += bity[y][x];
			x -= x&(-x);
		}
		y -= y&(-y);
	}
	return ans;
}
int getm(int y, int x)
{
	int ans = 0, X = x;
	while (y > 0)
	{
		x = X;
		while (x > 0)
		{
			ans += bitm[y][x];
			x -= x&(-x);
		}
		y -= y&(-y);
	}
	return ans;
}


int solve()
{
	memset(bitx, 0, sizeof bitx);
	memset(bity, 0, sizeof bity);
	memset(bitm, 0, sizeof bitm);

	char s[555];
		
	scanf("%d %d %*d", &r, &c);
	for (int i = 1; i <= r; i++)
	{
		scanf("%s", s + 1);
		for (int j = 1; j <= c; j++)
		{
			m[i][j] = s[j] - '0';
			
			int ii = i; 
			while (ii <= r)
			{
				int jj = j;
				while (jj <= c)
				{
					bity[ii][jj] += m[i][j] * i;
					bitx[ii][jj] += m[i][j] * j;
					bitm[ii][jj] += m[i][j];
					jj += jj&-jj;
				}
				ii += ii&-ii;
			}
		}
	}

/*	for (int i = 1; i <= r; i++)
	{
		for (int j = 1; j <= c; j++)
		{
			printf("%d", m[i][j]);
		}
		puts("");
	}
	puts("");
	for (int i = 1; i <= r; i++)
	{
		for (int j = 1; j <= c; j++)
		{
			printf("%d ", bitx[i][j]);
		}
		puts("");
	}
*/
	
	int maxk = 2;
	for (int i = 1; i <= r; i++)
	{
		for (int j = 1; j <= c; j++)
		{
			for (int k = maxk + 1; i + k - 1 <= r && j + k - 1 <= c; k++)
			{
				int mass = (getm(i + k - 1, j + k - 1)
				+ getm(i - 1, j - 1)
				- getm(i - 1, j + k - 1)
				- getm(i + k - 1, j - 1) - 
				m[i][j] -
				m[i][j + k - 1] -
				m[i + k - 1][j] -
				m[i + k - 1][j + k - 1]);
				
				if (2*(
				getx(i + k - 1, j + k - 1)
				+ getx(i - 1, j - 1)
				- getx(i - 1, j + k - 1)
				- getx(i + k - 1, j - 1) - 
				m[i][j] * (j) -
				m[i][j + k - 1] * (j + k - 1) -
				m[i + k - 1][j] * (j) -
				m[i + k - 1][j + k - 1] * (j + k - 1)) == (j + j + k - 1) * mass
				)
				if (2*(
				gety(i + k - 1, j + k - 1)
				+ gety(i - 1, j - 1)
				- gety(i - 1, j + k - 1)
				- gety(i + k - 1, j - 1) - 
				m[i][j] * (i) -
				m[i][j + k - 1] * (i) -
				m[i + k - 1][j] * (i + k - 1) -
				m[i + k - 1][j + k - 1] * (i + k - 1)) == (i + i + k - 1) * mass
				)
				{
//					printf("%d %d\n", i, j);
					maxk = k;
				}
			}
		}
	}
	return maxk;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ", i);
		int ans = solve();
		if (ans == 2)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);	
	}
	return 0;
	
}
