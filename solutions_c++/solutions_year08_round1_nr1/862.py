#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define min(a, b) ((a) < (b) ? (a) : (b))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define EPS 1e-8

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef set<int> SI;
typedef map<int, int> MII;

int n;
VI a, b;
LL ans = 1LL << 62;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		printf("Case #%d: ", cc);
		ans = 1LL << 62;
		scanf("%d", &n);
		a.clear();
		b.clear();
		for (int i = 0; i < n; ++i) {
			int x;
			scanf("%d", &x);
			a.push_back(x);
		}
		for (int i = 0; i < n; ++i) {
			int x;
			scanf("%d", &x);
			b.push_back(x);
		}
		
		sort(b.begin(), b.end());
		do {
			LL r = 0;
			for (int i = 0; i < n; ++i)
				r += (long long)a[i] * b[i];
			ans <?= r;
		} while (next_permutation(b.begin(), b.end()));
		cout << ans << "\n";
	}
	return 0;
}

