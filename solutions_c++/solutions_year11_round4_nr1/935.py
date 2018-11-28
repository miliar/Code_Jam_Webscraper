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

/*

int shift[MAXROW1 + 5];
int pi[MAXROW2 + 5];

void compute_prefix(char *P, int m, int *pi) { 
	int k = pi[0] = -1; 
	for (int q = 1; q<m; ++q) { 
		while (k >= 0 && P[k + 1] != P[q]) k = pi[k]; 
		if (P[k + 1] == P[q]) ++k; 
		pi[q] = k;
	}
}

int kmp_match(char *T, char *P, int *shift) { 
	int n, m, q = -1, shifts = 0; n = strlen(T); m = strlen(P); 
	compute_prefix(P, m, pi);
	REP(i,n) { 
		while (q > -1 && P[q + 1] != T[i]) q = pi[q]; 
		if (P[q + 1] == T[i]) ++q; 
		if (q == m - 1) { 
			shift[shifts++] = i - m + 1; 
			q = pi[q]; 
		} 
	} 
	return shifts; 
}
*/

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}

// ptrrsn_1's template

typedef pair<int, PII> PIII;
#define MPIII(a,b,c) MP(a,MP(b,c))
#define A F
#define B S.F
#define C S.S

vector <PIII> v;
int len, walk, run, t, N;

int main () {
	OPEN("prog");
	int nTC = getInt();
	FOR (tc, 1, nTC) {
		v.clear();
		scanf("%d%d%d%d", &len, &walk, &run, &t);
		scanf("%d", &N);
		REP (i, N) {
			int a, b, c;
			scanf("%d%d%d", &a, &b, &c);
			v.PB(MPIII(a, b, c));
		}
		sort(ALL(v));
		v.PB(MPIII(v[SIZE(v) - 1].B, len, 0));
		v.PB(MPIII(0, v[0].A, 0));
		sort(ALL(v));
		REP (i, SIZE(v) - 1) {
			v.PB(MPIII(v[i].B, v[i + 1].A, 0));
		}
		REP (i, SIZE(v)) {
			swap(v[i].A, v[i].C);
			swap(v[i].B, v[i].C);
		}
		sort(ALL(v));
		double T = t;
		double ret = 0.0;
		REP (i, SIZE(v)) {
			double s = v[i].C - v[i].B;
			double running = MIN (1. * s / (v[i].A + run), T);
			T -= running;
			s -= (v[i].A + run) * running;
			ret += running;
			
			double walking = 1. * s / (v[i].A + walk);
			ret += walking;
		}
		
		printf("Case #%d: %.10lf\n", tc, ret);
	}
    return 0;
}
