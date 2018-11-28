//============================================================================
// Author       : LAM PHAN VIET - lamphanviet@gmail.com
// Problem Name : 
// Time Limit   : .000s
// Description  : 
//============================================================================
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define sqr(x) ((x) * (x))

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI 3.1415926535897932385
#define INF 1000111222
#define eps 1e-7
#define maxN 10

const int n = 4;
char s[maxN][maxN];

bool check(char c) {
	int d1 = 0, d2 = 0;
	rep(i, n) {
		int row = 0, col = 0;
		rep(j, n) {
			if (s[i][j] == c || s[i][j] == 'T') row++;
			if (s[j][i] == c || s[j][i] == 'T') col++;
		}
		if (row == 4 || col == 4) return true;
		if (s[i][i] == c || s[i][i] == 'T') d1++;
		if (s[i][n - i - 1] == c || s[i][n - i - 1] == 'T') d2++;
	}
	if (d1 == 4 || d2 == 4) return true;
	return false;
}

int solve() {
	if (check('X')) return 0;
	if (check('O')) return 1;
	bool empty = false;
	rep(i, n) rep(j, n) empty |= (s[i][j] == '.');
	return empty ? 3 : 2;
}

int main() {
	#ifndef ONLINE_JUDGE
		freopen("test.inp", "r", stdin);
		freopen("test.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		rep(i, n) scanf(" %s ", s[i]);
		int res = solve();
		printf("Case #%d: ", ++caseNo);
		if (res == 0) puts("X won");
		else if (res == 1) puts("O won");
		else if (res == 2) puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}
