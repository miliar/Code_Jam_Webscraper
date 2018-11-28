#include <cstdio>
#include <set>

using namespace std;

int len[10000001];
int pow10[10];

void init() {
	len[0] = 0;
	for (int i = 1; i <= 10000000; i++)
		len[i] = len[i/10] + 1;

	pow10[0] = 1;
	for (int i = 1; i < 10; i++)
		pow10[i] = pow10[i-1] * 10;
}

int count(int A, int n) {
	int l = len[n];

	set<int> ans;
	for (int i = 1; i < l; i++) {
		int a = pow10[i];
		int b = pow10[l - i];

		int m = (n % a) * b + (n / a);
		if (len[m] == l && A <= m && m < n) {
			ans.insert(m);
		}
	}

	return ans.size();
}

int main() {
	init();

	int T; scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		int A, B; scanf("%d %d", &A, &B);

		int ans = 0;
		for (int j = A; j <= B; j++) {
			ans += count(A, j);
		}

		printf("Case #%d: %d\n", i, ans);
	}

	return 0;
}
