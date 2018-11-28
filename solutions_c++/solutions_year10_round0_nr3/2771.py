#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <queue>
using namespace std;

int main() {
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int t;
	scanf("%d ", &t);
	for (int i = 0; i < t; i++) {
		printf("Case #%d: ", i + 1);
		int r, k, n, res = 0;
		scanf("%d %d %d ", &r, &k, &n);
		queue <int> q;
		for (int j = 0; j < n; j++) {
			int x;
			scanf("%d ", &x);
			q.push(x);
		}
		for (int ride = 0; ride < r; ride++) {
			int cur = 0, num = 0;
			while (cur + q.front() <= k && num < n) {
				cur += q.front();
				q.push(q.front());
				q.pop();
				num++;
			}
			res += cur;
		}
		printf("%d\n", res);
	}
	return 0;
}

