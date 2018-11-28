#include <iostream>
#include <cstdio>
#define maxN 100

using std::cin;
using std::cout;
using std::endl;

int N, K;
char map[maxN][maxN];
char nm[maxN][maxN], g[maxN][maxN];

bool
doCheck(int i, int j, char q, int dx, int dy)
{
	for (int p = 1; p < K; p++)
	{
		i += dx;
		j += dy;
		if (1 > i || i > N || 1 > j || j > N || g[i][j] != q)
			return(false);
	}
	return true;
}

bool
check(char q)
{
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= N; j++)
			if (g[i][j] == q)
				if (doCheck(i, j, q, 1, 0) || doCheck(i, j, q, 0, 1) || doCheck(i, j, q, 1, -1) || doCheck(i, j, q, 1, 1))
					return(true);
	return(false);
}

int
main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, z;
	cin >> T;
	for (z = 1; z <= T; z++)
	{
		cin >> N >> K;
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++)
				cin >> map[i][j];
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++)
				nm[j][N - i + 1] = map[i][j];
		for (int i = 1; i <= N; i++)
		{
			int j = N;
			for (int k = N; k >= 1; k--)
				if (nm[k][i] != '.')
				{
					g[j][i] = nm[k][i];
					j--;
				}
			for (; j >= 1; j--)
				g[j][i] = '.';
		}
		bool red = check('R'), blue = check('B');
		cout << "Case #" << z << ": ";
		if (red && blue)
			cout << "Both" << endl;
		else if (red)
			cout << "Red" << endl;
		else if (blue)
			cout << "Blue" << endl;
		else
			cout << "Neither" << endl;
	}
	return(0);
}

