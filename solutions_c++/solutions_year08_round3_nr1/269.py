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

#define EPS 1e-8

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int, int> PII;
typedef set<int> SI;
typedef map<int, int> MII;

const int maxn = 1024;

int p, k, l;
int a[maxn];
int key[maxn][maxn], size[maxn]; // # of chars in every key;
LL ans;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		printf("Case #%d: ", cc);
		scanf("%d %d %d", &p, &k, &l);
		for (int i = 0; i < l; ++i) scanf("%d", a + i);
		sort(a, a + l);
		
		for (int i = 0; i < k; ++i)
			for (int j = 0; j < p; ++j) key[i][j] = 0;
		memset(size, 0, sizeof(size));			
		int d, c = 0, i = l - 1;
		while (1) {
			d = 0;
			while (d < k && i >= 0) {
				key[d][c] = a[i];
				++d;
				--i;
			}
			if (i < 0) break;
			++c;
			if (c == p) break;
		}
		
		if (i >= 0) puts("Impossible");
		else {
				ans = 0;
				for (int i = 0; i < k; ++i)
					for (int j = 0; j < p; ++j) ans += (long long)key[i][j] * (j + 1);
				cout << ans << "\n";
		}
	}
	return 0;
}

