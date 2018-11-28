#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>

using namespace std;

int T, n, S, P;
int a[100];

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%d%d%d", &n, &S, &P);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
		}
		sort(a, a + n, greater<int>());
		int res = 0;
		for (int i = 0; i < n; ++i) {
			int t = (a[i] + 2) / 3;
			if (t >= P) {
				++res;
			} else if (S > 0 && a[i] >= 2) {
				t = (a[i] + 4) / 3;
				if (t >= P) {
					--S;
					++res;
				}
			}
		}
		printf("Case #%d: %d\n", caseNum, res);
	}
	return 0;
}
