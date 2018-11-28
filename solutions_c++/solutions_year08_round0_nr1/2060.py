#include <cstdio>
#include <cstring>
#include <iostream>
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

const int maxn = 128;
const int maxq = 1024;
const int oo = 1000000000;

int f[maxq][maxn], a[maxq];
int n, q;
map<string, int> id;

int DP() {
	if (!q) return 0;
	
	int ret = oo;
	for (int i = 0; i < q; ++i)
		for (int j = 0; j < n; ++j) f[i][j] = oo;
	for (int j = 0; j < n; ++j)
		if (a[0] != j) f[0][j] = 0;
		
	for (int i = 1; i < q; ++i)
		for (int j = 0; j < n; ++j) {
			if (a[i] == j) {
				f[i][j] = oo;
				continue;
			}
			
			for (int k = 0; k < n; ++k)
				if (k == j) f[i][j] <?= f[i - 1][j];
				else
					if (f[i - 1][k] < oo) f[i][j] <?= f[i - 1][k] + 1;
//			printf("f[%d][%d] = %d\n", i, j, f[i][j]);
		}
	for (int j = 0; j < n; ++j) ret <?= f[q - 1][j];
	return ret;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int cases;
	string s;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		printf("Case #%d: ", cc);
		scanf("%d\n", &n);
		id.clear();
		for (int i = 0; i < n; ++i) {
			getline(cin, s);
//			cout << s << "\n";
			if (id.find(s) == id.end()) id[s] = i;
		}
		scanf("%d\n", &q);
		assert(q <= maxq && n <= maxn);
		for (int i = 0; i < q; ++i) {
			getline(cin, s);
			a[i] = id[s];
//			printf("a[%d] = %d\n", i, a[i]);
		}
		
		int ans = DP();
		printf("%d\n", ans);
	}
	return 0;
}

