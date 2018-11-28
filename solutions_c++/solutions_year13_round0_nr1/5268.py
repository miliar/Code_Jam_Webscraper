// .... .... .... !

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cassert>

#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

#include <cstdio>
#include <cstring>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define fch(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define sz(x) (int((x).size()))
#define X first
#define Y second
#define pb push_back

typedef long long ll;
typedef pair <int, int> pii;

////////////////////////////////////////////////////////////////////////////////

int tt, tc = 1;
char a[8][8];

int main()
{
	ios::sync_with_stdio (false);
	ofstream cout ("o.out");

	for (cin >> tt; tc <= tt; tc++)
	{
		rep (i, 4) cin >> a[i];

		char winner = '#';
		int x, o, t, empty = 0;

		rep (i, 4)
		{
			x = o = t = 0; rep (j, 4) x += (a[i][j] == 'X'), o += (a[i][j] == 'O'), t += (a[i][j] == 'T');
			if (x+t == 4) winner = 'X'; if (o+t == 4) winner = 'O';
			x = o = t = 0; rep (j, 4) x += (a[j][i] == 'X'), o += (a[j][i] == 'O'), t += (a[j][i] == 'T');
			if (x+t == 4) winner = 'X'; if (o+t == 4) winner = 'O';
		}
		x = o = t = 0; rep (i, 4) x += (a[i][i] == 'X'), o += (a[i][i] == 'O'), t += (a[i][i] == 'T');
		if (x+t == 4) winner = 'X'; if (o+t == 4) winner = 'O';
		x = o = t = 0; rep (i, 4) x += (a[3-i][i] == 'X'), o += (a[3-i][i] == 'O'), t += (a[3-i][i] == 'T');
		if (x+t == 4) winner = 'X'; if (o+t == 4) winner = 'O';
		rep (i, 4) rep (j, 4) empty += (a[i][j] == '.');

		cout << "Case #" << tc << ": ";
		if (winner != '#') cout << winner << " won" << endl;
		else if (empty == 0) cout << "Draw" << endl;
		else cout << "Game has not completed" << endl;

		cin >> ws;
	}
	

	{ int _; cin >> _; return 0; }
}
