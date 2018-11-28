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

// 0 - OK+no surp, 1 - OK + surp, -1 - impossible
int getSurp(int n, int p) {
	if (n >= 29) {
		return 0;
	}
	if (n == 1) {
		if (p <= 1) {
			return 0;
		} else {
			return -1;
		}
	}
	if (n == 0) {
		if (p <= 0) {
			return 0;
		} else {
			return -1;
		}
	}
	if (n%3 == 0) {
		int avP = n / 3; // ex: 9
		if (p > avP + 1) return -1;
		if (p == avP + 1) return 1;
		if (p <= avP) return 0;
		assert(false);
	}
	if (n%3 == 1) {
		int avP = n / 3; // ex: 28/3=9
		if (p > avP + 1) return -1;
		return 0;
	}
	if (n%3 == 2) {
		int avP = n / 3; // ex: 26/3=8
		if (p > avP + 2) return -1;
		if (p == avP + 2) return 1;
		return 0;
	}
	assert(false);
	return -1;
}

void Solve(int caseNo)
{
	int N,S,p;
	scanf("%d%d%d", &N, &S, &p);

	int ans=0;
	forn(i,N) {
		int m;
		cin >> m;
		int res = getSurp(m, p);
		if (res == 0) {
			ans++;
		}
		if ((res == 1) && (S > 0)) {
			ans++;
			S--;
		}
	}
	printf("Case #%d: %d\n", caseNo, ans);
    //printf( "%2.1f\n", ans );
}


int main()
{
	//if (freopen("c:\\_temp\\B.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\B-small-attempt0.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B-small-attempt0.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\B_test.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B_test.out", "wt", stdout) == NULL) throw 2;

	if (freopen("c:\\_temp\\B-large.in", "rt", stdin) == NULL) throw 1;
	if (freopen("c:\\_temp\\B-large.out", "wt", stdout) == NULL) throw 2;

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