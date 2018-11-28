#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

#define SZ(x) (int)(x).size()
#define FOR(i, seq, n) for(int i = (seq); i < (n); ++i)
#define FORD(i, seq, n) for(int i = (seq); i >= (n); --i)
#define REP(i, n) for(int i = 0; i < (n); ++i)
#define REPD(i, n) for(int i = (n) - 1; i >= 0; --i)
#define ALL(x) (x).begin(), (x).end()
#define SQR(x) (x)*(x)
typedef unsigned long long u64;
typedef signed long long i64;
typedef pair<int, int> pii;
#define X first
#define Y second

int freq[200];

int main()
{
	int T;
	cin >> T;
	REP (t, T) {
		int N, L, H;
		cin >> N >> L >> H;
		REP (i, N) cin >> freq[i];

		int res = -1;
		for (int c = L; c <= H; ++c) {
			bool ok = true;
			REP (i, N) if (c % freq[i] != 0 && freq[i] % c != 0) ok = false;
			if (ok) { res = c; break; }
		}
		cout << "Case #" << (t + 1) << ": ";
		if (res == -1) cout << "NO" << endl;
		else cout << res << endl;
	}
	return 0;
}

