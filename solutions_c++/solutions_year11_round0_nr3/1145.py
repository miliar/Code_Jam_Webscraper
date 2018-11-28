#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
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

int main()
{

	//if (freopen("c:\\_temp\\C.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\C.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\C-small-attempt0.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\C-small-attempt0.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\C_test.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\C_test.out", "wt", stdout) == NULL) throw 2;

	if (freopen("c:\\_temp\\C-large.in", "rt", stdin) == NULL) throw 1;
	if (freopen("c:\\_temp\\C-large.out", "wt", stdout) == NULL) throw 2;



	int T;
	cin >> T;

	FOR(test, 1, T) {
		cerr << "case " << test << "\n";
		int N;
		cin >> N;

		int checkSum = 0;
		vector<int> arr(N);
		REP(n,N) {
			cin >> arr[n];
			checkSum ^= arr[n];
		}

		if (checkSum == 0)
		{
			sort(arr.begin(), arr.end());
			int sum = 0;
			FOR(n, 1, N-1) {
				sum += arr[n];
			}
			printf("Case #%d: %d\n", test, sum);
		}
		else
		{
			printf("Case #%d: NO\n", test);
		}
		
	}

	fflush(stdout);
	exit(0);
}