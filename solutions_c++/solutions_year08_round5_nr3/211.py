#define SOLVE "C-small-attempt2"
#include <iostream>
#define CLS(x) memset(x,0,sizeof(x))
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <string>
#include <cstdio>
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"
#define GI ({int t; scanf("%d",&t);t;})
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(it,v) FOR(it,(v).begin(), (v).end())
#define sz size()
#define pb push_back
#define cs c_str()
#define INF ((int)(1e8))
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef long double ld;
#include <cmath>
#define MN 82
int n;
char G[MN][MN]; int R, C;
bool S[MN][MN];
int cnt[2];
void go(int r, int c, int col = 0) {
	if (S[r][c]) return ;
	S[r][c] = 1;
	cnt[col] ++;
	#define _f(x,y) if (x >= 0 && y >= 0 && x < R && y < C && G[x][y] != 'x') go(x,y,!col);
	#define f(x,y) _f((x),(y))
	f(r-1,c-1); f(r-1,c+1);
	f(r,c-1);f(r,c+1);
	f(r+1,c-1); f(r+1,c+1);
}

#define MM 10
int idp[2][MM][MM][1 << MM];
int igo (bool flag, int r, int c, int f) {
	if (c == C) flag = c = 0, r ++;
	if (r == R) return 0;
	int &res = idp[flag][r][c][f];
	if (res == -1) {
		res = igo (f & (1<<c), r, c+1, f&~(1<<c));
		int mask = c ? (5 << (c-1)) : (2 << c);
		if (!(f & mask) && !flag && G[r][c] != 'x')
			res >?= igo (f & (1<<c), r, c+1, f|(1<<c)) + 1;
	}
	return res;
}
int solve2() {
	memset(idp, -1, sizeof(idp));
	return igo (0, 0, 0, 0);
}

int main () {
	assert(freopen (SOLVE ".in", "r", stdin));
	assert(freopen (SOLVE ".out", "w", stdout));
	int kases = GI;
	REP(kase, kases) {
		printf("Case #%d: ", kase+1);
		R = GI; C = GI;
		REP(r,R) scanf("%s",G[r]);
		memset(S,0,sizeof(S));
		int ans = 0;
		REP(r,R) REP(c,C) if (!S[r][c] && G[r][c] != 'x') {
			memset(cnt,0,sizeof(cnt));
			go(r,c);
			ans += cnt[0] >? cnt[1];
		}
//		cout << ans << endl;
		cout << solve2() << endl;
	}
	return 0;
}
