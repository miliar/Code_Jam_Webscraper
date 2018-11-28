#include <iostream>
#include <algorithm>
using namespace std;
int bk[100];

int cnt1(int x)
{
	//printf("cnt %d ", x);
	int r = 0;
	while (x)
	{
		r++;
		x-=x&-x;
	}
	//printf("%d\n", r);
	return r;
}
int m, n;


bool check(int st, int lastst)
{
	for (int i=1; i<n; i++)
		if ((st&(1<<i)) && (st&(1<<(i-1))))
			return false;
	for (int i=0; i<n; i++)
	{
		if (st&(1<<i))
		{
			int x;
			x = i-1;
			if (x>=0&&x<n && (lastst&(1<<x))) return false;
			x=i+1;
			if (x>=0&&x<n && (lastst&(1<<x))) return false;
		}			
	}
	return true;
}


int main()
{
	int C;
	scanf("%d", &C);
	for (int ca=1; ca<=C; ca++)
	{
		scanf("%d%d", &m, &n);
		memset(bk, 0, sizeof(bk));
		for (int i=0; i<m; i++)
			for (int j=0; j<n; j++)
			{
				char ch;
				do { ch = getchar(); } while (ch != '.' && ch != 'x');
				if (ch == 'x')
					bk[i] |= (1<<j);
			}
			/*
		int f[100][100][2] = {0};
		int fx[3][2] = {{-1,-1}, {-1,1}, {0,-1}};
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				if (bk[i][j])
					f[i][j][0] = f[i][j][1] = 0;
				else
				{
					f[i][j][0] = 0;
					if (j==0 && i>0)
						f[i][j][0] = max(f[i-1][m-1][0], f[i-1][m-1][1]);
					else if (i>0)
						f[i][j][0] = max(f[i][j-1][0], f[i][j-1][1]);

					f[i][j][1] = max{doubuzuo}
					int m0 = 0, m1 = 0;
					for (int k=0; k<3; k++)
					{
						int x = i+fx[k][0];
						int y = j+fx[k][1];
						if (x >= 0 && y>=0)
						{
							if (f[x][y][0] < m0)
								m0 = f[x][y][0];
							if (f[x][y][1] < m1)
								m1 = f[x][y][1];
						}
						* 
					sorry!!!!
			*/
			
			int f[100][1024];

			memset(f, 0, sizeof(f));
			int res = 0;
			for (int i=0; i<m; i++)
				for (int j=0; j<(1<<n);j++)
				{
					if ((j & bk[i]) == 0)
					{
						if (i==0)
						{
							if (check(j,0))
								f[i][j] = cnt1(j);
						}
						else
						for (int k=0; k<(1<<n);k++) // last
						{
							if (check(j,k))
								f[i][j] = max(f[i][j], f[i-1][k]+cnt1(j));
						}
					}
					else
						;//printf("bad\n");
					if (f[i][j] > res)
						res = f[i][j];
				}
				/*
			for (int i=0; i<m; i++)
			{
				for (int j=0; j<(1<<n); j++)
					printf("%d ", f[i][j]);
				putchar(10);
			}
			*/
			
			printf("Case #%d: %d\n", ca, res);
		
	}
}

/*
1
1 10
..........
*/
