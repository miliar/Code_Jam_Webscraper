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

#define MAXROW 500
#define MAXCOL 500

int nTC;
int nrows, ncols, D;
LL M[MAXROW + 5][MAXCOL + 5];
char s[MAXCOL + 5];

LL dp[MAXROW + 5][MAXCOL + 5];

LL atas[MAXROW + 5][MAXCOL + 5];
LL bawah[MAXROW + 5][MAXCOL + 5];
LL kanan[MAXROW + 5][MAXCOL + 5];
LL kiri[MAXROW + 5][MAXCOL + 5];

inline void initDP() {
	FOR (i, 1, nrows) {
		FOR (j, 1, ncols) {
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + M[i][j];
		}
	}
}

inline LL getTotal(int r1, int c1, int r2, int c2) {
	return dp[r2][c2] - dp[r1 - 1][c2] - dp[r2][c1 - 1] + dp[r1 - 1][c1 - 1];
}

inline void initAtas() {
	FOR (i, 1, nrows) FOR (j, 1, ncols) {
		atas[i][j] = dp[i][j] + atas[i - 1][j];
	}
}

inline void initBawah() {
	FORD (i, nrows, 1) FOR (j, 1, ncols) {
		bawah[i][j] = getTotal(i, 1, nrows, j) + bawah[i + 1][j];
	}
}

inline void initKiri() {
	FOR (i, 1, nrows) FOR (j, 1, ncols) {
		kiri[i][j] = dp[i][j] + kiri[i][j - 1];
	}
}

inline void initKanan() {
	FOR (i, 1, nrows) FORD (j, ncols, 1) {
		kanan[i][j] = getTotal(1, j, i, ncols) + kanan[i][j + 1];
	}
}

inline LL getAtas(int r1, int c1, int r2, int c2) {
	LL K = r2 - r1 + 1;
	return (atas[r2][c2] - atas[r1 - 1][c2] - K * dp[r1 - 1][c2])
		-  (atas[r2][c1 - 1] - atas[r1 - 1][c1 - 1] - K * dp[r1 - 1][c1 - 1]);
}

inline LL getBawah(int r1, int c1, int r2, int c2) {
	LL K = r2 - r1 + 1;
	return (bawah[r1][c2] - bawah[r2 + 1][c2] - K * getTotal(r2 + 1, 1, nrows, c2)) // dp[r2 + 1][c2])
	    -  (bawah[r1][c1 - 1] - bawah[r2 + 1][c1 - 1] - K * getTotal(r2 + 1, 1, nrows, c1 - 1)); //dp[r2 + 1][c1 - 1]);
}

inline LL getKiri(int r1, int c1, int r2, int c2) {
	LL K = c2 - c1 + 1;
	return (kiri[r2][c2] - kiri[r2][c1 - 1] - K * dp[r2][c1 - 1])
		-  (kiri[r1 - 1][c2] - kiri[r1 - 1][c1 - 1] - K * dp[r1 - 1][c1 - 1]);
}

inline LL getKanan(int r1, int c1, int r2, int c2) {
	LL K = c2 - c1 + 1;
	return (kanan[r2][c1] - kanan[r2][c2 + 1] - K * getTotal(1, c2 + 1, r2, ncols)) // dp[r2][c2 + 1])
		-  (kanan[r1 - 1][c1] - kanan[r1 - 1][c2 + 1] - K * getTotal(1, c2 + 1, r1 - 1, ncols)); //dp[r1 - 1][c2 + 1]);
}

int main () {
	OPEN("prog");
	
	scanf("%d", &nTC);
	
	FOR (tc, 1, nTC) {
		scanf("%d%d%d", &nrows, &ncols, &D);
		RESET(M, 0);
		REP (i, nrows) {
			scanf("%s", s);
			REP (j, ncols) {
				M[i + 1][j + 1] = NUM(s[j]) + D;
			}
		}
		
		initDP();
		initAtas();
		initBawah();
		initKiri();
		initKanan();
		/*
		FOR (i, 1, nrows) {
			FOR (j, 1, ncols) {
				cout << kanan[i][j] << " ";
			}
			cout << endl;
		}
		*/
		/*
		cout << getTotal(2,3,5,7) << endl;
		LL tot = 0;
		FOR (i, 2, 5) FOR (j, 3, 7) {
			tot += M[i][j];
		}
		cout << tot << endl;
		*/
		int ret = -1;
		
		FOR (i, 1, nrows) FOR (j, 1, ncols) FOR (k, 3, MIN(nrows, ncols)) {
			if (i + k - 1 > nrows || j + k - 1 > ncols) break;
			if (k & 1) {
				// ganjil
				LL dv = getAtas(i, j, i + (k/2) - 1, j + k - 1);
				dv -= getBawah(i + (k/2) - 1 + 2, j, i + k - 1, j + k - 1);
				dv -= M[i][j] * (k/2);
				dv -= M[i][j + k - 1] * (k/2);
				dv += M[i + k - 1][j] * (k/2);
				dv += M[i + k - 1][j + k - 1] * (k/2);
				LL dh = getKiri(i, j, i + k - 1, j + (k/2) - 1);
				/*
				if (k == 5 && i == 2 && j == 2) {
					cout << dh << endl;
				}
				*/
				dh -= getKanan(i, j + (k/2) - 1 + 2, i + k - 1, j + k - 1);
				
				/*
				if (k == 5 && i == 2 && j == 2) {
					cout << dh << endl;
				}
				*/
				dh -= M[i][j] * (k/2);
				dh += M[i][j + k - 1] * (k/2);
				dh -= M[i + k - 1][j] * (k/2);
				dh += M[i + k - 1][j + k - 1] * (k/2);
				if (dv == 0 && dh == 0) {
					ret = MAX(ret, k);
				}
			} else {
				// genap
				LL dv = getAtas(i, j, i + (k/2) - 1, j + k - 1);
				dv -= getBawah(i + (k/2) - 1 + 2, j, i + k - 1, j + k - 1);
				dv *= 2;
				dv -= getTotal(i, j, i + k - 1, j + k - 1);
				dv -= M[i][j] * (k-1);
				dv -= M[i][j + k - 1] * (k-1);
				dv += M[i + k - 1][j] * (k-1);
				dv += M[i + k - 1][j + k - 1] * (k-1);
				LL dh = getKiri(i, j, i + k - 1, j + (k/2) - 1);
				dh -= getKanan(i, j + (k/2) - 1 + 2, i + k - 1, j + k - 1);
				dh *= 2;
				dh -= getTotal(i, j, i + k - 1, j + k - 1);
				
				dv -= M[i][j] * (k-1);
				dv += M[i][j + k - 1] * (k-1);
				dv -= M[i + k - 1][j] * (k-1);
				dv += M[i + k - 1][j + k - 1] * (k-1);
				if (dv == 0 && dh == 0) {
					ret = MAX(ret, k);
				}
			}
		}
		
		printf("Case #%d: ", tc);
		if (ret == -1) {
			puts("IMPOSSIBLE");
		} else {
			cout << ret << endl;
		}
	}
	return 0;
}
