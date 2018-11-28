#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

vector<int> t[3];
int n, s, p, ans;

int main() {
	int cases; scanf("%d", &cases);

	for (int T = 1; T <= cases; ++T) {
		printf("Case #%d: ", T); ans = 0;
		t[0].clear(), t[1].clear(), t[2].clear();

		scanf("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; ++i) {
			int x; scanf("%d", &x);
			t[x % 3].push_back(x);
		}
		for (int i = 0; i < t[1].size(); ++i) {
			if ((t[1][i] + 2) / 3 >= p) ans++;
		}
		for (int i = 0; i < t[0].size(); ++i) {
			if ((t[0][i] + 2) / 3 >= p) {
				ans++; continue;
			}

			if (t[0][i] > 0 && (t[0][i] + 2) / 3 + 1 >= p && s > 0) ans++, s--;
		}
		for (int i = 0; i < t[2].size(); ++i) {
			if ((t[2][i] + 2) / 3 >= p) {
				ans++; continue;
			}

			if ((t[2][i] + 2) / 3 + 1 >= p && s > 0) ans++, s--;
		}

		printf("%d\n", ans);
	}

	return 0;
}
