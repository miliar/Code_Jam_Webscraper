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
#define pb push_back



int main()
{
	int T; cin >> T;
	REP (t, T) {
		int N; cin >> N;
		int can = 0, mn = 1 << 30, sum = 0;
		REP (i, N) {
			int c; cin >> c;
			can ^= c;
			mn = min(mn, c);
			sum += c;
		}
		
		cout << "Case #" << (t + 1) << ": ";
		if (can == 0)
			cout << (sum - mn) << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
