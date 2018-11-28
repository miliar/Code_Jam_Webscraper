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
#include <numeric>
using namespace std;

#include <iostream>

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }


void Solve(int caseNo)
{
	int N;
	long long L,H;
	cin >> N >> L >> H;

	vector<long long> FF(N); // bug1
	REP(i,N) {
		cin >> FF[i];
	}

	bool isFound = false;
	for (long long f = L; f <= H; f++)
	{
		bool isOK = true;
		REP(i,N){
			if ((FF[i]%f != 0) && (f % FF[i] != 0)){
				isOK = false; // f is non-harmonic with i
				break;
			}
		}
		if (isOK) {
			printf("Case #%d: ", caseNo);
			cout << f << '\n';
			isFound = true;
			break;
		}
	}
	if (!isFound){
		printf("Case #%d: ", caseNo);
		cout << "NO\n";
	}
}


int main()
{
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

	FOR(i, 1, caseCount) {
		clock_t now = clock();
		cerr << "case " << i << "...";
		
		Solve(i);
		fflush(stdout);

		cerr << "Done!; Elapsed ms:" << (double)(clock() - now) * 1000 / CLOCKS_PER_SEC << "\n";
	}
	cerr << "Total elapsed seconds:" << (double)(clock() - totalNow) / CLOCKS_PER_SEC << "\n";

	exit(0);
}