#include <iostream>
#include <vector>
#include <string>
using namespace std;
int n, m;
int mmap[102][102];
int mark[102][102];
int num[102][102];
int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};
void init ()
{
	int kkk = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			int k;
			for (k = 0; k < 4; k++)
			{
				int tx = i + dir[k][0];
				int ty = j + dir[k][1];
				if (tx >= 0 && tx < n && ty >= 0 && ty < m)
				{
					if (mmap[tx][ty] < mmap[i][j])
						break;
				}
			}
			if (k == 4)num[i][j] = kkk++;
		}
	}
}
int dfs (int x, int y)
{
	if (num[x][y] != -1 )return num[x][y];
	int i;
	int mmin = mmap[x][y];
	int xx = -1;
	for (i = 0; i < 4; i++)
	{
		int tx = x + dir[i][0];
		int ty = y + dir[i][1];
		if (tx >= 0 && tx < n && ty >= 0 && ty < m 
			&& mmap[tx][ty] < mmin)
		{
			xx = i;
			mmin = mmap[tx][ty];
		}
	}
	if (xx != -1)
	{
		int tx = x + dir[xx][0];
		int ty = y + dir[xx][1];
		num[x][y] = dfs (tx, ty);
	}
	mark[x][y] = 1;
	return num[x][y];
}
int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t, ca = 1;
	cin >> t;
	while (t--)
	{
		cin >> n >> m;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
			{
				cin >> mmap[i][j];
				mark[i][j] = 0;
				num[i][j] = -1;
			}
			init();
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				//cout << num[i][j] <<" ";
				if (!mark[i][j])
				{
					dfs (i, j);
				}
			}
			//cout << endl;
		}
		int hash[30];
		memset (hash, -1, sizeof (hash));
		int kkk = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (hash[num[i][j]] == -1)
					hash[num[i][j]] = kkk++;
			}
		}
		printf ("Case #%d:\n", ca++);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m - 1; j++)
			{
				cout << char (hash[num[i][j]] + 'a') << " ";
			}
			cout << char (hash[num[i][m - 1]] + 'a')<< endl;
		}
	}
}