#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>
#include <sstream>

#define oo 1000000005
#define eps 1e-11

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define FOREACH(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define RESET(c,x) memset (c, x, sizeof (c))

#define sqr(x) ((x) * (x))
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ALL(c) (c).begin(), (c).end()
#define SIZE(c) (c).size()

using namespace std;

struct point {
	double x,y;
	point (double x,double y): x(x),y(y) {}
	point () {x=y=0.0; }
	point operator +(point q) { return point(x+q.x,y+q.y); }
	point operator -(point q) { return point(x-q.x,y-q.y); }
	point operator *(double t) { return point(x*t,y*t); }
	point operator /(double t) { return point(x/t,y/t); }
	double operator *(point q){ return q.x * x + q.y * y; }
	double operator %(point q){ return x*q.y - y*q.x; }
//	int cmp(point q) const { if(int t = ::cmp(x,q.x)) return t; return ::cmp(y,q.y); }
//	#define Comp(x) bool operator x (point q) const { return cmp(q) x 0; }
//	Comp(>) Comp(<) Comp(==) Comp(>=) Comp(<=) Comp(!=)
//	#undef Comp
};

const double PI = 2.0 * acos (0.0);

typedef long long LL;
typedef pair <int, int> PII;

inline int getInt () { int x; scanf ("%d", &x); return x; }
inline LL getLL () { LL x; scanf ("%lld", &x); return x; };
inline int NUM (char c) { return (int)c - 48; }
inline char CHR (int n) { return (char)(n + 48); }
template <class T> inline T MAX (T a, T b) { if (a > b) return a; return b; }
template <class T> inline T MIN (T a, T b) { if (a < b) return a; return b; }

inline int BPM (int a, int b, int MOD) {
    if (a == 0)
        return 0;
    if (b == 0)
        return 1 % MOD;
    if (b % 2 == 1)
        return (int)((LL) BPM (a, b - 1, MOD) * a % MOD);
    int tmp = BPM (a, b / 2, MOD);
    return (int)((LL) tmp * tmp % MOD);
}

inline int phi (int N) {
    int ret = N;
    for (int i = 2; N > 1; i++) {
        if (i * i > N) {
            ret -= ret / N;
            break;
        }
        if ( N % i == 0 ) {
            ret -= ret / i;
            while (N % i == 0)
                N /= i;
        }
    }
    return ret;
}

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}

// ptrrsn_1's template

inline int toInt(char c) {
	return c == 'O';
}

vector <int> each[2];
int sz[2];
vector <int> all;
int currentButton[2];
int nextButtonIdx[2];
int N;

inline void initAll() {
	all.clear();
	each[0].clear(); each[1].clear();
	currentButton[0] = currentButton[1] = 1;
	nextButtonIdx[0] = nextButtonIdx[1] = 0;
}

inline bool simulate(int player, bool canPush) {
	if (nextButtonIdx[player] == sz[player]) {
		return false;
	}
	int &a = currentButton[player];
	int b = each[player][nextButtonIdx[player]];
	if (a == b) {
		return canPush;
	} else if (a < b) {
		a++;
	} else {
		a--;
	}
	return false;
}

int main () {
	OPEN("prog");
	FOR (tc, 1, getInt()) {
		initAll();
		
		N = getInt();
		
		REP (i, N) {
			char c[2];
			int pos;
			scanf ("%s%d", c, &pos);
			all.PB(toInt(c[0]));
			each[toInt(c[0])].PB(pos);
		}
		
		sz[0] = SIZE(each[0]);
		sz[1] = SIZE(each[1]);
		
		int ret = 0;
		
		REP (i, SIZE(all)) {
			int curPlayer = all[i];
			bool finish = false;
			while (!finish) {
				finish = simulate(curPlayer, true);
				if (finish) {
					nextButtonIdx[curPlayer]++;
				}
				simulate(!curPlayer, false);
				ret++;
			}
		}
		
		printf("Case #%d: %d\n", tc, ret);
	}
    return 0;
}
