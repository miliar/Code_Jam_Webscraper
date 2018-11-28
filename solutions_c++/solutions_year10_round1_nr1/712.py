#include<iostream>
using namespace std;

#define N 51

int n, K;
int mat[N][N];
bool red, blue;

void check(int, int, int, int);

int main()
{
//	freopen("g:\\A-large.in", "r", stdin);
//	freopen("g:\\a.out", "w", stdout);

	int testnum;
	cin >> testnum;
	for (int tcnt = 1; tcnt <= testnum; ++tcnt)
	{
		//input
		cin >> n >> K;
		int i;
		for (i = 1; i <= n; ++i)
		{
			char tmpst[N];
			cin >> tmpst;
			for (int j = 0; j < n; ++j)
			{
				if (tmpst[j] == 'R')
					mat[i][j + 1] = 1;
				else if (tmpst[j] == 'B')
					mat[i][j + 1] = 2;
				else mat[i][j + 1] = 0;
			}
		}

		// rotate and gravity
		for (i = 1; i <= n; ++i)
		{
			int last = n;
			for (int j = n; j >= 1; --j)
			{
				if (mat[i][j] != 0)
				{
					int tmp = mat[i][j];
					mat[i][j] = 0;
					mat[i][last--] = tmp;
				}
			}
		}

		//check
		red = blue = false;
		for (i = 1; i <= n; ++i)
		{
			check(i, 1, 0, 1);
			check(1, i, 1, 0);
			check(1, i, 1, 1);
			check(i, 1, 1, 1);
			check(i, 1, -1, 1);
			check(n, i, -1, 1);
		}

		cout << "Case #" << tcnt << ": ";
		if (red && blue)
			cout << "Both" << endl;
		else if (red)
			cout << "Red" << endl;
		else if (blue)
			cout << "Blue" << endl;
		else
			cout << "Neither" << endl;
	}

	return 0;
}

void check(int si, int sj, int inci, int incj)
{
	int i, j;
	int redcnt, bluecnt;
	redcnt = bluecnt = 0;
	for (i = si, j = sj; i > 0 && i <= n && j > 0 && j <= n; i += inci, j += incj)
	{
		if (mat[i][j] == 1)
		{
			redcnt++;
			bluecnt = 0;
		}
		else if (mat[i][j] == 2)
		{
			bluecnt++;
			redcnt = 0;
		}
		else 
			bluecnt = redcnt = 0;
		if (redcnt >= K)
			red = true;
		if (bluecnt >= K)
			blue = true;
	}
}