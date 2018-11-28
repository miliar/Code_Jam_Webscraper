#define SOLVE "B-small-attempt0"
#define ok(a,b) (a >= 0 && a < b)
#include <iostream>
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
typedef long long ld;

int R, C;
char G[64][64];
struct State {
	int r, c, br, bc, bd, yr, yc, yd;
};
bool operator<(State a, State b) { return memcmp(&a, &b, sizeof(a)) < 0; }
map <State, int> M;
deque<State> Q;

int main () {
	assert(freopen (SOLVE ".in", "r", stdin));
	assert(freopen (SOLVE ".out", "w", stdout));
	int kases = GI;
	REP(kase, kases) {
		printf("Case #%d: ", kase+1);
		int R = GI, C = GI;
		State s;
		s.br = s.bc = s.yr = s.yc = -1;
		REP(r,R) {
			scanf("%s", G[r]);
			REP(c,C) if (G[r][c] == 'O') s.r = r, s.c = c;
		}
		M.clear(); Q = deque<State>();
		M[s] = 0; Q.push_front(s);
		int ans = -1;
		while (!Q.empty()) {
			int dir = 0;
			State os = Q.front(); Q.pop_front();
			assert (ok(os.r,R) && ok(os.c,C));
			if (G[os.r][os.c] == '#') continue;
			//dbg (os.r); dbge(os.c);
			if (G[os.r][os.c] == 'X') { ans = M[os]; break;}
			FOR(dr, -1, +2) FOR(dc, -1, +2) if(dr*dc == 0) if (dr||dc) {
				dir ++;
				// Fire!
				#define TRY_FIRE(rr,cc,dd) \
				rr = s.r, cc = s.c; \
				while (ok(rr,R) && ok(cc,C) && G[rr][cc] != '#') rr += dr, cc += dc;\
				rr -= dr, cc -= dc; \
				if (os.br != rr || os.bc != cc || os.bd != dir) \
				if (os.yr != rr || os.yc != cc || os.yd != dir) \
				if (dd = dir, !M.count(s)) {\
					M[s] = M[os]; Q.push_front(s);\
				}
				s = os; s.bd = -2; TRY_FIRE(s.br,s.bc,s.bd);
				s = os; s.yd = -2; TRY_FIRE(s.yr,s.yc,s.yd);
				s = os; s.r += dr, s.c += dc;
				if (ok(s.r,R) && ok(s.c,C) && !M.count(s)) {
					M[s] = M[os]+1;
					Q.push_back(s);
				}
				s = os; if (s.r == s.yr && s.c == s.yc) s.r = s.br, s.c = s.bc; 
				if (ok(s.r,R) && ok(s.c,C) && !M.count(s)) {
					M[s] = M[os]+1;
					Q.push_back(s);
				}
			}
			assert (4 == dir);
//			assert (M.sz < 1e5);
		}
		if (ans == -1) puts("THE CAKE IS A LIE");
		else cout << ans << endl;
	}
	return 0;
}
