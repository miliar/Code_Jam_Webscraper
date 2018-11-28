#include <iostream>
using namespace std;

#define MAXN 55
char tile[MAXN][MAXN];
int n, m, ok;

inline bool canPlace (int x, int y)
{
	return tile[x][y] == '#' && tile[x + 1][y] == '#' && tile[x][y + 1] == '#' && tile[x + 1][y + 1] == '#';
}

inline void place (int x, int y)
{
	tile[x][y]		= '/'	, tile[x + 1][y]		= '\\';
	tile[x][y + 1]	= '\\'	, tile[x + 1][y + 1]	= '/';
}

inline void remove (int x, int y)
{
	tile[x][y]		= '#'	, tile[x + 1][y]		= '#';
	tile[x][y + 1]	= '#'	, tile[x + 1][y + 1]	= '#';
}


void back (int x, int y, int numBlue, int numRed)
{
	if (ok)
		return;

	if (numBlue == 0) {
		ok = true;
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= m; ++j) 
				cout << tile[i][j];

			cout << endl;
		}
	} else {
		y = (y == m) ? (++x, 1) : (y + 1);
		if (x > n) {
			return;
		}
		
		if (canPlace (x, y)) {
			place (x, y);
			back (x, y, numBlue - 4, numRed + 4);
			remove (x, y);
		} else {
			back (x, y, numBlue, numRed);
		}
	}
}

void doTest ()
{
	int numBlue = 0;
	cin >> n >> m;
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			cin >> tile[i][j];
			if (tile[i][j] == '#')
				numBlue++;
		}
	}
	
	ok = false;
	if (numBlue % 4 == 0) {
		back (0, 1, numBlue, 0);
	}
	if (!ok) {
		cout << "Impossible" << endl;
	}
}

int main ()
{
	//freopen ("square.in", "r", stdin);
	//freopen ("suare.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ":" << endl;
		doTest ();
	}

}