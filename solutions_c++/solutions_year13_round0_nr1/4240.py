#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <cassert>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
//evtl noch: mp fuer make_pair, pb fuer push_back
char c[4][4];

bool checkCol(int i, char cc) {
	FOR(j, 0, 4) if (c[j][i] != cc && c[j][i] != 'T') return false;
	return true;
}

bool checkRow(int i, char cc) {
	FOR(j, 0, 4) if (c[i][j] != cc && c[i][j] != 'T') return false;
	return true;
}

bool checkDiag1(char cc) {
	FOR(j, 0, 4) if (c[j][j] != cc && c[j][j] != 'T') return false;
	return true;
}

bool checkDiag2(char cc) {
	FOR(j, 0, 4) if (c[j][3-j] != cc && c[j][3-j] != 'T') return false;
	return true;
}

bool check(char c) {
	return checkRow(0, c) || checkRow(1, c) || checkRow(2, c) || checkRow(3, c) || checkCol(0, c) || checkCol(1, c) || checkCol(2, c) || checkCol(3, c) || checkDiag1(c) || checkDiag2(c);
}

int main() {
	int n;
	cin >> n;
	FOR(i, 0, n) {
		bool fin = true;
		FOR(k, 0, 4) FOR(l, 0, 4) {
			cin >> c[k][l];
			if (c[k][l] == '.') fin = false;
		}
		if (check('O')) printf("Case #%d: O won\n", i+1);
		else if (check('X')) printf("Case #%d: X won\n", i+1);
		else if (fin) printf("Case #%d: Draw\n", i+1);
		else printf("Case #%d: Game has not completed\n", i+1);
	}
	return 0;
}



