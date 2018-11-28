#include <cstdio>
#include <memory>
#include <cstdlib>
using namespace std;

const int maxn = 55;

int N, K;

char board[maxn][maxn];
char tmp[maxn][maxn];
bool f[255];

void rotate()
{
	memset(tmp, '.', sizeof(tmp));
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < N; j ++)
			tmp[i][j] = board[N - j - 1][i];
	memset(board, '.', sizeof(board));
	for (int j = 0; j < N; j ++)
	{
		int k = N - 1;
		for (int i = N - 1; i >= 0; i --)
			if (tmp[i][j] != '.') board[k --][j] = tmp[i][j];
	}
}

void dig(int x, int y, int dx, int dy)
{
	int k = 0; char c = '$';
	while (0 <= x && x < N && 0 <= y && y < N)
	{
		if (board[x][y] == c)
		{
			k ++;
			if (k >= K) f[c] = 1;
		}
		else
		{
			k = 1;
			c = board[x][y];
		}
		x += dx; y += dy;
	}
}

void print()
{
	for (int i = 0; i < N; i ++)
	{
		for (int j = 0; j < N; j ++)
			printf("%c", board[i][j]);
		printf("\n");
	}
}

void count()
{
	for (int i = 0; i < N; i ++)
	{
		dig(i, 0, 0, 1);
		dig(0, i, 1, 0);
		dig(0, i, 1, 1);
		dig(i, 0, 1, 1);
		dig(0, i, 1, -1);
		dig(i, N - 1, 1, -1);
	}
}

void init()
{
	memset(board, '.', sizeof(board));
	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; i ++)
		scanf("%s", board[i]);
}

void solve()
{
	f['B'] = 0; f['R'] = 0;
//	print();
	rotate();
//	print();
	count();
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int _T = 1; _T <= T; _T ++)
	{
		init();
		solve();
		printf("Case #%d: ", _T);
		if (f['R'] && f['B']) printf("Both");
		else if (f['R']) printf("Red");
		else if (f['B']) printf("Blue");
		else printf("Neither");
		printf("\n");
	}
}
