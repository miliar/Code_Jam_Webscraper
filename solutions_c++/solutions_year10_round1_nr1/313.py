#include <cstdio>

using namespace std;

char table[100][100];
int t, n, k;

char cur;

int maxrow(int row)
{
	int MM=0;
	int c=0;
	for (int i=0;i<n;i++)
	{
		if (table[row][i] == cur)
		{
			c++;
			if (c>MM) MM=c;
		}
		else
			c=0;
	}
	return MM;
}

int maxcol(int col)
{
	int MM=0;
	int c=0;
	for (int i=0;i<n;i++)
	{
		if (table[i][col] == cur)
		{
			c++;
			if (c>MM) MM=c;
		}
		else
			c=0;
	}
	return MM;
}

int maxdiag1(int x, int y)
{
	int MM=0;
	int c=0;
	for (;x>=0&&x<n&&y>=0&&y<n;x--,y++)
	{
		if (table[y][x] == cur)
		{
			c++;
			if (c>MM) MM=c;
		}
		else
			c=0;
	}
	return MM;
}

int maxdiag2(int x, int y)
{
	int MM=0;
	int c=0;
	for (;x>=0&&x<n&&y>=0&&y<n;x++,y++)
	{
		if (table[y][x] == cur)
		{
			c++;
			if (c>MM) MM=c;
		}
		else
			c=0;
	}
	return MM;
}


bool solve(char ch)
{
	cur=ch;
	for (int i=0;i<n;i++)
	{
		if (maxrow(i) >= k)
			return true;
		if (maxcol(i) >= k)
			return true;
		if (maxdiag1(i,0)>=k)
			return true;
		if (maxdiag1(n-1, i)>=k)
			return true;
		if (maxdiag2(i,0)>=k)
			return true;
		if (maxdiag2(0, i)>=k)
			return true;
	}
	return false;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int cases=1; cases<=t; cases++)
	{
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;i++)
		{
			scanf("%s", table[i]);
			int k=n-1;
			for (int j=n-1;j>=0;j--)
			{
				if (table[i][j] != '.')
				{
					table[i][k] = table[i][j];
					k--;
				}
			}
			for (;k>=0;k--)
				table[i][k] = '.';
		}
		bool red = solve('R');
		bool black = solve('B');
		if (red && black)
		{
			printf("Case #%d: Both\n", cases);
		}
		else if (red)
		{
			printf("Case #%d: Red\n", cases);
		}
		else if(black)
		{
			printf("Case #%d: Blue\n", cases);
		}
		else
		{
			printf("Case #%d: Neither\n", cases);
		}
	}
	return 0;
}