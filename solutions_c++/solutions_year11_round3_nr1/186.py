#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#define mp make_pair
#define st first
#define nd second
#define FOR(i,n) for(int i=0;i<(n);i++)
#define FORO(i,n) for(int i=1;i<=(n);i++)
#define FORS(i,a,n) for(int i=(a);i<(n);i++)
#define FORB(i,a,n) for(int i=(a);i>=(n);i--)
#define FORE(i,v) for(typeof((v).begin())i=(v).begin();i!=(v).end();i++)
#define INRANGE(a,b,c,d) ((a)>=0&&(b)>=0&&(a)<(c)&&(b)<(d))
#define pf printf
typedef long long ll;
using namespace std;

int R, C;
char B[60][60];

void solve() {
	scanf("%d%d", &R, &C);
	FOR(i, R)
		scanf("%s", B[i]);
	bool possible = true;
	FOR(r, R) {
		if (!possible)
			break;
		FOR(c, C) {
			if (!possible)
				break;
			if (B[r][c] == '#') {
				if (r == R-1 || c == C-1 || B[r+1][c] != '#' ||
					B[r][c+1] != '#' || B[r+1][c+1] != '#')
					possible = false;
				else {
					B[r][c] = B[r+1][c+1] = '/';
					B[r+1][c] = B[r][c+1] = '\\';
				}
			}
		}
	}
	if (possible)
		FOR(r, R) pf("%s\n", B[r]);
	else
		pf("Impossible\n");
}


int main() {
	//freopen(".in", "r", stdin); freopen(".out", "w", stdout);
	int n;
	scanf("%d", &n);
	FORO(i, n) {
		pf("Case #%d:\n", i);
		solve();
	}
}


