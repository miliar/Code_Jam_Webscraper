#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>

void solve() {
	int n;
	scanf("%d", &n);
	if (n == 1) {
		printf("0\n");
		return;
	}
	std::map<int, int> cnt;
	int ans = 1;
	for (int i = 2; i <= n; ++i) {
		int k = i;
		bool removed = true;
		int j = 2;
		for (j = 2; j * j <= i; ++j) {
			int cntx = 0;
			while (k % j == 0) {
				k /= j;
				++cntx;
			}
			if (cntx) {
				int& old = cnt[j];
				if (old < cntx) {
					old = cntx;
					removed = false;
				}
			}
		}
		if (k > 1) {
			int& old = cnt[k];
			if (old < 1) {
				old = 1;
				removed = false;
			}
		}
		if (!removed)
			++ans;
	}

	printf("%d\n", ans - cnt.size());
}

char s[1024];
int main(int argc, char* argv[]) {
    freopen(argv[1], "r", stdin);
    strcat(s, argv[1]);
    strcat(s, ".out");
    freopen(s, "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i+1);
		solve();
    }
        
}