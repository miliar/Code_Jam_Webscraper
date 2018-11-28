// created on: 2013-04-13
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>

using namespace std;

// For vim: auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while

#define ALL(c) c.begin(), c.end()
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(int)(b); ++i)
#define FOREACH(X,C) for(typeof(C.begin()) X=C.begin();X!=C.end();++X)
#define PB push_back
#define SS stringstream
#define EPS (1e-9)
#define INF (1<<30)
#define SQR(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define EQUAL(a,b) (ABS((a)-(b))<eps)
#define px first
#define py second

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define FORX(i,a,b,x) for (int i=(a); i<=(int)(b); i+=x)
#define FORD(i,a,b) for (int i=a; i>=b; --i)

#define REV(c) reverse(c.begin(), c.end())
#define SORT(c) sort(c.begin(), c.end())

typedef vector<int> VI; typedef vector<VI> VVI;
typedef vector<string> VS; typedef vector<VS> VVS;
typedef vector<long long> VLL;
typedef signed long long LL; typedef unsigned long long ULL;
typedef pair<int,int> PII;

typedef map<int,int> MII;
typedef map<char,int> MCI;
typedef map<string,int> MSI;

LL tonum(string s){ stringstream in(s); LL x; in>>x; return x; }
string tostr(LL n){ stringstream in; in << n; string x; in>>x; return x; }
LL gcd(LL a, LL b) { return __gcd(a, b); }

/* end of pre-code */
int check_x_win(VS grid) {
	int cnt = 0;
	REP(col, 4) {
		cnt = 0;
		REP(row, 4) if (grid[row][col] == 'X' || grid[row][col] == 'T') cnt++;
		if (cnt >= 4) return 1;
	}
	REP(row, 4) {
		cnt = 0;
		REP(col, 4) if (grid[row][col] == 'X' || grid[row][col] == 'T') cnt++;
		if (cnt >= 4) return 1;
	}

	cnt = 0;
	REP(i, 4) if (grid[i][i] == 'X' || grid[i][i] == 'T') cnt++;
	if (cnt >= 4) return 1;

	cnt = 0;
	REP(i, 4) if (grid[3-i][i] == 'X' || grid[3-i][i] == 'T') cnt++;
	if (cnt >= 4) return 1;

	return 0;
}

int check_o_win(VS grid) {
	int cnt = 0;
	REP(col, 4) {
		cnt = 0;
		REP(row, 4) if (grid[row][col] == 'O' || grid[row][col] == 'T') cnt++;
		if (cnt >= 4) return 1;
	}
	REP(row, 4) {
		cnt = 0;
		REP(col, 4) if (grid[row][col] == 'O' || grid[row][col] == 'T') cnt++;
		if (cnt >= 4) return 1;
	}

	cnt = 0;
	REP(i, 4) if (grid[i][i] == 'O' || grid[i][i] == 'T') cnt++;
	if (cnt >= 4) return 1;

	cnt = 0;
	REP(i, 4) if (grid[3-i][i] == 'O' || grid[3-i][i] == 'T') cnt++;
	if (cnt >= 4) return 1;

	return 0;
}

int check_full(VS grid) {
	REP(x, 4) REP(y, 4) if (grid[x][y] == '.') return 0;
	return 1;
}

int main() {
	freopen ("input.txt", "rb", stdin);
	freopen ("output.txt", "w", stdout);

	int T; cin >> T;
	int t_case = 0;
	VS grid(4);
	while (T--) {
		getline(cin, grid[0]);
		getline(cin, grid[0]); getline(cin, grid[1]); getline(cin, grid[2]); getline(cin, grid[3]);

		cout << "Case #" << ++t_case << ": ";

		if (check_x_win(grid))
			cout << "X won" << endl;
		else if (check_o_win(grid))
			cout << "O won" << endl;
		else if (check_full(grid))
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}

	return 0;
}
