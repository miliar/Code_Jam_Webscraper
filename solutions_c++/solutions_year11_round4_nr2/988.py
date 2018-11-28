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

int R, C, D;
char W[550][550];
ll Sum[550][550];

void fillsums() {
	FOR(r, R)
		FOR(c, C)
			Sum[r+1][c+1] = Sum[r+1][c] + Sum[r][c+1] - Sum[r][c] + W[r][c];
}

ll tsum(int r1, int c1, int r2, int c2) {
	return Sum[r2][c2] - Sum[r2][c1] - Sum[r1][c2] + Sum[r1][c1];
}

bool check_corner(int r, int c, int d) {
	int r1 = r-d, r2 = r+d, c1 = c-d, c2 = c+d;
	if (r1 < 0 || r2 > R || c1 < 0 || c2 > R)
		return false;
	ll stop = tsum(r1, c1, r, c2) - W[r1][c1] - W[r1][c2-1];
	ll sbot = tsum(r, c1, r2, c2) - W[r2-1][c1] - W[r2-1][c2-1];
	if (stop != sbot)
		return false;
	ll sleft = tsum(r1, c1, r2, c) - W[r1][c1] - W[r2-1][c1];
	ll sright = tsum(r1, c, r2, c2) - W[r1][c2-1] - W[r2-1][c2-1];
	if (sleft != sright)
		return false;
	return true;
}

bool check_center(int r, int c, int d) {
	int rr = r+1, cc = c+1;
	int r1 = r-d, r2 = rr+d, c1 = c-d, c2 = cc+d;
	if (r1 < 0 || r2 > R || c1 < 0 || c2 > R)
		return false;
	ll stop = tsum(r1, c1, r, c2) - W[r1][c1] - W[r1][c2-1];
	ll sbot = tsum(rr, c1, r2, c2) - W[r2-1][c1] - W[r2-1][c2-1];
	if (stop != sbot)
		return false;
	ll sleft = tsum(r1, c1, r2, c) - W[r1][c1] - W[r2-1][c1];
	ll sright = tsum(r1, cc, r2, c2) - W[r1][c2-1] - W[r2-1][c2-1];
	if (sleft != sright)
		return false;
	return true;
}

typedef typeof(check_center) fja;

void tcase() {
	scanf("%d%d%d", &R, &C, &D);
	FOR(i, R)
		scanf("%s", W[i]);
	FOR(i, R) FOR(j, C) W[i][j] -= '0';
	fillsums();
	int bestside = 0;
	FOR(r, R+1) FOR(c, C+1) FORS(s, 2, 270)
		if (check_corner(r, c, s))
			bestside = max(bestside, 2*s);
	FOR(r, R) FOR(c, C) FORO(s, 270)
		if (check_center(r, c, s))
			bestside = max(bestside, 2*s+1);
	if (bestside == 0)
		pf("IMPOSSIBLE\n");
	else
		pf("%d\n", bestside);
}


int main() {
	int tc;
	scanf("%d", &tc);
	FORO(i, tc) {
		pf("Case #%d: ", i);
		tcase();
	}
}


