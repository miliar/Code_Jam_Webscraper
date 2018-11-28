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

const int maxn = 110;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int board[maxn][maxn];
int cnt[maxn][maxn];
int color[maxn][maxn];
char res[maxn][maxn];
pair < int, int > prev[maxn][maxn];
int h, w;

bool inboard ( int x, int y )
{
	return ( x >= 0 && y >= 0 && x < h && y < w ); 	
}

void calc ( int i, int j ) 
{
	cnt[i][j] = 1;
	prev[i][j] = MP ( i, j );

	int minx = INF;
	FOR(k, 4) {
		int x = i + dx[k];
		int y = j + dy[k];
		if ( inboard ( x, y ) && board[x][y] < board[i][j] ) {
			minx = min ( minx, board[x][y] );
		}
	}

	if ( minx == INF ) return;

	FOR(k, 4) {
		int x = i + dx[k];
		int y = j + dy[k];
		if ( inboard ( x, y ) && board[x][y] < board[i][j] && board[x][y] == minx ) {
			if ( cnt[x][y] == -1 )
				calc ( x, y );
			cnt[i][j] = max( cnt[i][j], cnt[x][y] + 1 );
			prev[i][j] = prev[x][y];
			break;
		}
	}
}

void dfs ( int i, int j, int col )
{
	color[i][j] = col;
	FOR(k, 4) {
		int x = i + dx[k];
		int y = j + dy[k];
		if ( inboard ( x, y ) && prev[x][y] == prev[i][j] ) {
			if ( color[x][y] == -1 )
				dfs ( x, y, col);
		}
	}
}

void solvecase ( int test )
{
	cout << "Case #" << test << ": " << endl;
	CLR(res, 0);
	CLR(board, 0);
	cin >> h >> w;
	FOR(i, h) FOR(j, w) 
		cin >> board[i][j];
	
    CLR(cnt, -1);
    FOR(i, h) FOR(j, w) if ( cnt[i][j] == -1 )
    	calc ( i, j );

    int cur = 0;
    CLR(color, -1);
    FOR(i, h) FOR(j, w) if ( color[i][j] == -1 ) 
    {
		dfs ( i, j, cur++ );
    }

    FOR(i, h) {
    	FOR(j, w) cout << (char)('a' + color[i][j]) << " ";
    	cout << endl;
    }
}

void solve()
{
	int T;
	cin >> T;
	FOR(i, T) solvecase ( i + 1 );
}

int main()
{
	init();
	solve();
	return 0;
}
