#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define REP(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define FOR(i, a, b) for (int i = (a), _n = (b); i <= _n; ++i)
#define FORD(i, a, b) for (int i = (a), _n = (b); i >= _n; --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int INF = 1000000000;

const int NMAX = 1000000;

bool prime[NMAX+1];

void testcase() {
	LL N;
	cin >> N;
	if (N == 1) {
		cout << 0 << endl; 
		return;
	}
	LL res = 1;
	for (int x = 2; 1LL*x*x <= N; ++x) if (prime[x]) {
		LL y = 1LL*x*x;
		int cnt = 1;
		while (y*x <= N) {
			y *= x;
			++cnt;
		}
		res += cnt;
	}
	cout << res << "\n";
}

int main() {
	fill_n(prime, NMAX+1, true);
	prime[0] = prime[1] = false;
	for (int i = 2; 1LL*i*i <= NMAX; ++i)
		if (prime[i])
			for (int j = i*i; j <= NMAX; j += i)
				prime[j] = false;

	int T;
	scanf("%d", &T);
	FOR(i, 1, T) {
		printf("Case #%d: ", i);
		testcase();
	}
}
