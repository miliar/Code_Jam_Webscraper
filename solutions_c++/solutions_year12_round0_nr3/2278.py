#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <ctime>

#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <numeric>
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair


typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> inline void relaxmin(T& a, const T& b) { if (a > b) a = b; }
template<typename T> inline void relaxmax(T& a, const T& b) { if (a < b) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T> int sign(T x) { return x > 0 ? 1 : (x < 0 ? -1 : 0); }

string str( int i ) { char s[100]; sprintf(s, "%d", i); return string(s); }

bool isRec(int n, int m) {
	if (n >= m) return false; // for sure

	int pow = 10;
	int digs = 1;
	while (pow <= n) {
		digs++;
		pow *= 10;
	}
	if (m >= pow) return false;
	pow /= 10;
	// Ex: 23 -> 10, 99 -> 10, 9 -> 1

	forn(d, digs) {
		int dig = n % 10; // Ex: 3
		n = pow * dig + n / 10; // Ex: 3*10+(23/10)=32
		if (n == m) return true;
	}
	return false;
}

bool isRec2(int n, int m) {
	if (n >= m) return false; // for sure

	char sn[10];
	char sm[10];
	_itoa(n, sn, 10);
	_itoa(m, sm, 10);
	int nL = strlen(sn);
	int mL = strlen(sm);
	if (nL != mL) return false;

	forn(i, nL) {
		char last=sn[nL-1];
		fornd(j, nL) {
			sn[j]=sn[j-1];
		}
		sn[0]=last;
		if (strcmp(sn, sm)==0) {
			return true;
		}
	}
	return false;
}


//const int radix=10;
//const int maxA = 2000000;
//const int maxAA = maxA / radix + 1; // 200000
//int cache[maxAA + 1];
//
//void fillcache() {
//	zero(cache);
//	forab(bb, 1, maxAA) {
//		int ans = cache[bb-1];
//		forab(n, 0, bb*radix - 1) {
//			forab(m, (bb-1) * radix + 1, bb*radix) {
//				if (isRec(n, m)) {
//					ans++;
//				}
//			}
//		}
//		cache[bb] = ans;
//	}
//}
const int maxB = 3000;
int cache[maxB + 1];
void fillcache() {
	zero(cache);
	forab(b, 1, maxB) {
		int ans = cache[b-1];
		forab(n, 0, b - 1) {
			int m = b;
			//bool res = isRec(n, m);
			//bool res2 = isRec2(n, m);
			//if (res != res2) {
			//	assert(false);
			//}
			if (isRec(n, m)) {
				ans++;
			}
		}
		cache[b] = ans;
	}
}

int checkCase4(int A, int B) {
	int ans=0;
	forab(n, A, B-1) {
		forab(m, n+1, B) {
			if (isRec(n, m)) {
				//printf ("%d %d\n", n, m);
				ans++;
			}
		}
	}
	//printf("Ans=%d", ans);
	return ans;
}

void Solve(int caseNo)
{
	int A,B;
	scanf("%d%d", &A, &B);

	//int ans = cache[B] - cache[A-1];
	int ans = checkCase4(A, B);
	printf("Case #%d: %d\n", caseNo, ans);
    //printf( "%2.1f\n", ans );
}


int main()
{
	//assert(isRec(12345, 34512));
	//assert(isRec2(12345, 34512));
	//assert(isRec(1230, 3012));
	//assert(!isRec(1111, 1111));
	//assert(!isRec(1110, 111));
	//assert(!isRec(111, 1110));
	//assert(isRec(1001, 1100));
	//assert(!isRec(1010, 0101));
	//assert(!isRec(1000, 1001));
	//assert(!isRec2(1000, 1001));
	//fillcache();
	//int res = checkCase4(1111, 2222);
	//int res1 = checkCase4(0, 1110);
	//int res2 = checkCase4(0, 2222);
	//int res3 = cache[1110];
	//int res4 = cache[2222];

	//res = checkCase4(996, 999);
	//res1 = checkCase4(0, 899);
	//res2 = checkCase4(0, 1100);
	//res3 = cache[899];
	//res4 = cache[1100];

	//if (freopen("c:\\_temp\\C.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\C.out", "wt", stdout) == NULL) throw 2;

	if (freopen("c:\\_temp\\C-small-attempt0.in", "rt", stdin) == NULL) throw 1;
	if (freopen("c:\\_temp\\C-small-attempt0.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\C_test.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\C_test.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\C-large.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\C-large.out", "wt", stdout) == NULL) throw 2;

	int caseCount;
	scanf("%d%", &caseCount);
	clock_t totalNow = clock();

	forab(i, 1, caseCount) {
		clock_t now = clock();
		cerr << "case " << i << "...";
		
		Solve(i);
		fflush(stdout);

		cerr << "Done!; Elapsed ms:" << (double)(clock() - now) * 1000 / CLOCKS_PER_SEC << "\n";
	}
	cerr << "Total elapsed seconds:" << (double)(clock() - totalNow) / CLOCKS_PER_SEC << "\n";

	exit(0);
}