#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <math.h>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for (int (i) = (a); (i) <= (b); (i)++)
#define DFOR(i, a, b) for (int (i) = (a) - 1; (i) >= (b); (i)--)
#define CLR(a, b) memset(a, (b), sizeof(a))
#define VI vector <int>
#define VS vector <string>
#define PB push_back
#define MP make_pair
#define SS stringstream
#define INF 1073741824
#define PII pair <int, int>
#define ALL(a) a.begin(), a.end()
#define SZ(x) (int)x.size()

#define LL long long
#define X first
#define Y second

void init()
{
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
}

const int maxn = 520;
const int inf = 1000;

int board[maxn][maxn];
int sides[maxn][maxn];
int res[maxn];
int n, m;


int hex(char ch)
{
	if (isdigit(ch))
		return (int)(ch - '0');
	else
		return (int)(ch - 'A') + 10;
}

void ReadBoard()
{
	CLR(board, 0);
	CLR(sides, 0);
	CLR(res, 0);

	char buf[maxn];
	scanf("%d%d\n", &n, &m);
	for (int i = 0; i < n; ++i)
	{
		gets(buf);
		for (int j = 0; j < m / 4; ++j)
		{
			int h = hex(buf[j]);
			for (int k = 0; k < 4; ++k)
				board[i][4 * j + (3 - k)] = (bool)(h & (1 << k));
		}
	}
	for (int i = 0; i < n; ++i)
		board[i][m] = inf;
	for (int j = 0; j < m; ++j)
		board[n][j] = inf;
	board[n][m] = inf;
}

void increase(int x, int y)
{
	for (int s = sides[x][y] + 1; s <= min ( n - x, m - y ) + 1; ++s)
	{
		bool ok = true;
		for (int a = x; a < x + s; ++a)
			ok &= (board[a][y + s - 1] == 1 - board[a][y + s - 2]);
		for (int b = y; b < y + s; ++b)
			ok &= (board[x + s - 1][b] == 1 - board[x + s - 2][b]);
		ok &= (board[x + s - 1][y + s - 1] == board[x][y]);
		if (!ok)
		{
			sides[x][y] = s - 1;
			break;
		}
	}
}

void CalcSides()
{
	CLR(sides, 0);

	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j) if (board[i][j] != -1)
		{
			sides[i][j] = 1;
			if (i > 0)
				sides[i][j] = max(sides[i][j], sides[i - 1][j] - 1);
			if (j > 0)
				sides[i][j] = max(sides[i][j], sides[i][j - 1] - 1);

			increase(i, j);
		}
	}
}

bool DeleteSquares()
{
	int maxs = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			maxs = max(maxs, sides[i][j]);
	if ( maxs <= 1 )
	{
		int cnt = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				if (board[i][j] != -1)
					cnt++;
			}
		}
		res[1] += cnt;
		return true;
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j) if (sides[i][j] == maxs && board[i][j] != -1) {
			bool ok = true;			
			for (int x = i; x < i + maxs; ++x)
				for (int y = j; y < j + maxs; ++y)
					ok &= (board[x][y] != -1);
			if (!ok)
				continue;
			for (int x = i; x < i + maxs; ++x)
				for (int y = j; y < j + maxs; ++y)
					board[x][y] = -1;
			res[maxs]++;
		}
	}
	return false;
}

void solvecase(int ntest)
{
	cout << "Case #" << ntest << ": ";
	ReadBoard();
	while (true)
	{
		CalcSides();
		if (DeleteSquares())
			break;
	}
	int cnt = 0;
	for (int i = 1; i < maxn; ++i)
		if (res[i] > 0)
			cnt++;
	cout << cnt << endl;
	for (int i = maxn; i > 0; --i)
		if (res[i] > 0)
			cout << i << " " << res[i] << endl;
}

void solve()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
		solvecase(i);
}

int main()
{
	init();
	solve();
	return 0;
}
