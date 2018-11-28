#include <iostream>
const int maxn = 101;
int a[maxn][maxn];
char lab[maxn][maxn];
using namespace std;
int h, w;
char lc;
int incr[4][2] = 
{
	{-1, 0},
	{0, -1},
	{0, 1},
	{1, 0},
};

bool sink(int r, int c)
{
	int i;
	for (i = 0; i < 4; i++)
	{
		int r2 = r + incr[i][0];
		int c2 = c + incr[i][1];
		if (r2 >= 0 && r2 < h && c2 >= 0 && c2 < w)
		{
			if (a[r2][c2] < a[r][c])
			{
				return false;
			}
		}
	}
	return true;
}

char floodFill(int r, int c)
{
	int i;
	if (lab[r][c] != 0)
	{
		return lab[r][c];		
	}
	if (sink(r, c))
	{
		lab[r][c] = lc++;
		return lab[r][c];
	}

	int minh = 10001, mr = r, mc = c;
	for (i = 0; i < 4; i++)
	{
		int r2 = r + incr[i][0];
		int c2 = c + incr[i][1];
		if (r2 >= 0 && r2 < h && c2 >= 0 && c2 < w)
		{
			if (a[r2][c2] < minh)
			{
				minh = a[r2][c2];
				mr = r2;
				mc = c2;
			}
		}
	}
	lab[r][c] = floodFill(mr, mc);
	return lab[r][c];
}

int main()
{
	int i, j, t, n, c = 0;
	//freopen("B-small-attempt0.in", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("in.txt", "r", stdin);
	cin>>t;
	while (t--)
	{
		cin>>h>>w;
		memset(lab, 0, sizeof(lab));
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				cin>>a[i][j];
			}
		}
		lc = 'a';
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				if (lab[i][j] == 0)
				{
					lab[i][j] = floodFill(i, j);
				}
			}
		}
		printf("Case #%d:\n", ++c);
		for (i = 0; i < h; i++)
		{
			for (j = 0; j < w; j++)
			{
				printf("%c ", lab[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
