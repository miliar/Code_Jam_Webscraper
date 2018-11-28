#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 128;

int t[MAXN];
vector <int> tt;

int not_sup(int x) {
	int r = x % 3;
	int a = x / 3;
	if (r) ++a;
	return a;
}

int sup(int x) {
	int r = x % 3;
	int a = x / 3;
	
	if (x == 0) return 0;
	if (x == 1) return 1;
	if (x == 2) return 2;
	if (r == 0) return a + 1;
	if (r == 1) return a + 1;
	if (r == 2) return a + 2;
}

int main() {
	int i, j, k;
	int m, n, s, p;
	int tc, cn(0);
	int tot, sum;
	
//	freopen("B-large.in", "r", stdin);
//	freopen("out.txt", "w", stdout);
	
	scanf("%d", &tc);
	while (tc--) {
		scanf("%d%d%d", &n, &s, &p);
		for (i=0; i<n; ++i) scanf("%d", t+i);
		tt.clear();
		for (i=0; i<n; ++i) {
			if (not_sup(t[i]) >= p) continue;
			tt.push_back(t[i]);
		}
		sum = 0;
		for (i=0; i<tt.size(); ++i) {
			if (sup(tt[i]) >= p) ++sum;
		}
		tot = min(sum, s) + n - tt.size();
		printf("Case #%d: %d\n", ++cn, tot);
	}
	return 0;
}