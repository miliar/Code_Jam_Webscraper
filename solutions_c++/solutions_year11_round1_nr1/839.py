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


pair<long, long> reduce(long p, long q) {
	for(int i=2; i<50; i++){
		while ((p%i==0)&&(q%i==0)){
			p /=i;
			q /=i;
		}
	}
	return pair<long, long>(p,q);
}

int Solve(int caseNo)
{
	long long N, PD, PG;
	cin >> N >> PD >> PG;
	//scanf("%d%d%d", &N, &PD, &PG);

	pair<long,long> PDpair=reduce(PD,100);
	pair<long,long> PGpair=reduce(PG,100);

	if (PDpair.second > N) {
		return 0; // 1
	}
	if ((PD >0) && (PG == 0))
	{
		return 0; //2
	}
	if ((PD < 100) && (PG == 100))
	{
		return 0; //3
	}
	return 1;
}


int main()
{
	//if (freopen("c:\\_temp\\A.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\A.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\A-small-attempt0.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\A-small-attempt0.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\A_test.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\A_test.out", "wt", stdout) == NULL) throw 2;

	if (freopen("c:\\_temp\\A-large.in", "rt", stdin) == NULL) throw 1;
	if (freopen("c:\\_temp\\A-large.out", "wt", stdout) == NULL) throw 2;

	int caseCount;
	scanf("%d%", &caseCount);
	clock_t totalNow = clock();

	FOR(i, 1, caseCount) {
		clock_t now = clock();
		cerr << "case " << i << "...";
		
		int ans = Solve(i);
		if (ans == 0)
		{
			printf("Case #%d: Broken\n", i);
		}
		else
		{
			printf("Case #%d: Possible\n", i);
		}

		fflush(stdout);

		cerr << "Done!; Elapsed ms:" << (double)(clock() - now) * 1000 / CLOCKS_PER_SEC << "\n";
	}
	cerr << "Total elapsed seconds:" << (double)(clock() - totalNow) / CLOCKS_PER_SEC << "\n";

	exit(0);
}