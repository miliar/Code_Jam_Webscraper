#include <stdio.h>
#include <string.h>
#include <math.h>

int cas = 0;
int	T;

int row, col;
int b[513][513];
int ans[513];

int getNum(char ch)
{
	if (ch >= '0' && ch  <= '9')
		return ch - '0';
	return ch - 'A' + 10;
}

int getCell(int x, int y)
{
	if (x < 0 || x >= row || y < 0 || y >= col)
	{
		return -1;	
	}
	return b[x][y];
}

int cmp(int a, int b)
{
	// -1 for used	
	// 1 black
	// 0 white

	if (b == -1 || a == -1)	
		return 1;	
	return (a == b);
}

int in(int x, int sx, int y, int sy, int cx, int cy)
{
	if (cx < x || cx >= sx || cy < y || cy >= sy)
		return 0;
	return 1;
}

int check(int x, int y, int sz)
{
	int i, j, k;

	int sx = x + sz;
	int sy = y + sz;
	for (i=x; i<sx; i++)
		for (j=y; j<sy; j++)
		{						
			int c = b[i][j];

			if (c == -1)		return 0;

			if (in(x, sx, y, sy, i-1, j))
			{
				int top = getCell(i-1, j);
				if (cmp(b[i][j], top))
					return 0;
			}

			if (in(x, sx, y, sy, i+1, j))
			{
				int top = getCell(i+1, j);
				if (cmp(b[i][j], top))
					return 0;
			}

			if (in(x, sx, y, sy, i, j-1))
			{
				int top = getCell(i, j-1);
				if (cmp(b[i][j], top))
					return 0;
			}

			if (in(x, sx, y, sy, i, j+1))
			{
				int top = getCell(i, j+1);
				if (cmp(b[i][j], top))
					return 0;
			}
			
		}

	for (i=x; i<sx; i++)
		for (j=y; j<sy; j++)
			b[i][j] = -1;	

	return 1;
}

int main()
{	
		freopen("in.in", "r", stdin);
		freopen("out.out", "w", stdout);
	

	int i, j, k;

	scanf("%d", &T);	
	while (T--)
	{		
		scanf("%d %d", &row, &col);
		for (i=0; i<row; i++)
		{
			int sz = col / 4;			
			for (k=j=0; j<sz; j++)
			{
				char ch[100];
				scanf("%1s", ch);
				int num = getNum(ch[0]);
				
				b[i][k++] = (num & 8) > 0 ? 1 : 0;
				b[i][k++] = (num & 4) > 0 ? 1 : 0;
				b[i][k++] = (num & 2) > 0 ? 1 : 0;
				b[i][k++] = (num & 1) > 0 ? 1 : 0;
			}
		}
		memset(ans, 0, sizeof(ans));

		int kind = 0;
		k = row > col ? col : row;
		for (; k>0; k--)
		{
			int cnt = 0;
			for (i=0; i<=row-k; i++)
				for (j=0; j<=col-k; j++)
				{
					if (check(i, j, k))
						cnt++;
				}
			ans[k] = cnt;
			if (cnt > 0)
				kind++;
		}

		printf("Case #%d: %d\n", ++cas, kind);
		k = row > col ? col : row;
		for (i=k; i>0; i--)
		{
			if (ans[i] > 0)
			{
				printf("%d %d\n", i, ans[i]);
			}
		}		
	}
	return 0;
}