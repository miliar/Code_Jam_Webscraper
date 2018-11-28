#include <cstdio>
#include <cstring>

using namespace std;

char str[3];
int n, arr[2][102];

inline int ABS(int x) {
	if (x > 0)
		return x;
	return -x;
}

int solve() {
	int posa = 1, posb = 1, ans = 0, time = 0;
	for (int i = 1; i <= n; i++) {
		if (arr[0][i] == 0) {
			int temp = ABS(arr[1][i] - posa);
			if (arr[0][i - 1] != 1) {
				time += temp + 1;
				ans += temp + 1;
			} else {
				if (temp <= time) {
					++ans;
					time = 1;
				} else {
					ans += temp - time + 1;
					time = temp - time + 1;
				}
			}
			posa = arr[1][i];
		} else {
			int temp = ABS(arr[1][i] - posb);
			if (arr[0][i - 1] != 0) {
				time += temp + 1;
				ans += temp + 1;
			} else {
				if (temp <= time) {
					++ans;
					time = 1;
				} else {
					ans += temp - time + 1;
					time = temp - time + 1;
				}
			}
			posb = arr[1][i];
		}
	}
	return ans;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int nca;
	scanf("%d", &nca);
	arr[0][0] = 3;
	arr[1][0] = 1;
	for (int ii = 1; ii <= nca; ++ii) {
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			scanf("%s%d", str, &arr[1][i]);
			if (str[0] == 'O') {
				arr[0][i] = 0;
			} else {
				arr[0][i] = 1;
			}
		}
		printf("Case #%d: %d\n", ii, solve());
	}
	return 0;
}
