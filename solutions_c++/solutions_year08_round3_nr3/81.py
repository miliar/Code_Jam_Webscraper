#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <deque>
#include <memory>
using namespace std;
typedef vector<int> vi;
typedef long long li;
typedef pair<int,int> pi;
#define all(c) c.begin(), c.end()
#define fr(i, n) for(i = 0; i < n; ++i)
#define pb push_back
#define mp make_pair
#define INT 2147483647
#define X first
#define Y second
#define sc(a) scanf("%d", &(a))

#define MOD 1000000007

int main() {
	freopen("e:\\code\\c\\c-small.in", "r", stdin);
	freopen("e:\\code\\c\\c-small.out", "w", stdout);
	li x, y, z, n, m, p, l, i, j, k, t, T;
	cin >> T;
	for (t = 1; t <= T; ++t) {
		scanf("%lld %lld %lld %lld %lld", &n, &m, &x, &y, &z);
		vi em(n);
		vi A(m);
		fr(i, m) cin >> A[i];
		for (i = 0; i < n; ++i) {
			em[i] = A[i % m];
			A[i % m] = (x * A[i % m] + y * (i + 1)) % z;
		}
		li res = 0, cur = 0;
		vi dp(2000);
		fr(i, n) {
			cur = 0;
			fr(j, i) if (em[i] > em[j]) cur = (cur + dp[j]) % MOD;
			dp[i] = (1 + cur) % MOD;
		}
		fr(i, n) res = (res + dp[i]) % MOD;
		printf("Case #%lld: %lld\n", t, res);
	}
	fclose(stdout);
	return 0;
}
