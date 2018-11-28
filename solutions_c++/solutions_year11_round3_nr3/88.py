#include <cstdio>
#include <cstring>

using namespace std;

int n, arr[102];

bool judge(int x) {
	for (int i = 0; i < n; i++) {
		if (arr[i] % x != 0 && x % arr[i] != 0) {
			return false;
		}
	}
	return true;
}

void solve(int ca) {
	int ll, hh;
	scanf("%d%d%d", &n, &ll, &hh);
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	bool flag = false;
	printf("Case #%d: ", ca);
	for (int i = ll; i <= hh; i++) {
		if (judge(i)) {
			flag = true;
			printf("%d\n", i);
			break;
		}
	}
	if (!flag) {
		puts("NO");
	}
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("csmall.out", "w", stdout);
	int nca;
	scanf("%d", &nca);
	for (int ii = 1; ii <= nca; ii++) {
		solve(ii);
	}
	return 0;
}
