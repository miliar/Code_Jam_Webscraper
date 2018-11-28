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

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, R, C, B;
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
int alt[200][200];
int base[200][200];

int rek(int r, int c) {
	if (base[r][c] != -1) return base[r][c];
	int Min = oo, mind = -1;
	FOR(d, 0, 4) {
		int rr = r + dx[d], cc = c + dy[d];
		if (rr < 0 || rr >= R || cc < 0 || cc >= C) continue;
		if (alt[rr][cc] >= alt[r][c]) continue;
		if (alt[rr][cc] < Min) {
			Min = alt[rr][cc];
			mind = d;
		}
	}
	if (Min == oo) {
		base[r][c] = B++;
	} else {
		base[r][c] = rek(r + dx[mind], c + dy[mind]);
	}
	return base[r][c];
}

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> R >> C;
		FOR(i, 0, R) FOR(j, 0, C) cin >> alt[i][j];
		memset(base, -1, sizeof(base));
		B = 0;
		FOR(i, 0, R) FOR(j, 0, C) rek(i, j);
		cout << "Case #" << cs << ":" << endl;
		FOR(i, 0, R) {
			cout << char(base[i][0] + 'a');
			FOR(j, 1, C) cout << ' ' << char(base[i][j] + 'a');
			cout << endl;
		}
	}
	return 0;
}
