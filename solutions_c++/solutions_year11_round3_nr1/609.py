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
	int R,C;
	scanf("%d%d", &R, &C);

	vector<vector<char>> RC(R,C);
	string s;
	REP(i,R) {
		cin >> s;
		REP(j,C) {
			RC[i][j] = s[j];
		}
	}

	REP(r,R-1){
		REP(c,C-1) {
			if ((RC[r][c]=='#')&&(RC[r+1][c]=='#')&&(RC[r][c+1]=='#')&&(RC[r+1][c+1]=='#'))
			{
				RC[r][c]='/';
				RC[r+1][c]='\\';
				RC[r][c+1]='\\';
				RC[r+1][c+1]='/';
			}
		}
	}

	bool isOK = true;
	REP(i,R) {
		REP(j,C) {
			if (RC[i][j] == '#'){
				isOK = false;
				break;
			}
		}
	}


	if (!isOK)
	{
		printf("Case #%d:\n", caseNo);
		cout << "Impossible\n";
	}
	else
	{
		printf("Case #%d:\n", caseNo);
		REP(i,R) {
			REP(j,C) {
				cout << RC[i][j];
			}
			cout << '\n';
		}
	}
    //printf( "%2.1f\n", ans );
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
		
		Solve(i);
		fflush(stdout);

		cerr << "Done!; Elapsed ms:" << (double)(clock() - now) * 1000 / CLOCKS_PER_SEC << "\n";
	}
	cerr << "Total elapsed seconds:" << (double)(clock() - totalNow) / CLOCKS_PER_SEC << "\n";

	exit(0);
}