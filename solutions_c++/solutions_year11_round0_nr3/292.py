#include <vector>
#include <algorithm>

#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

int main() {
	freopen("C-large.in", "r", stdin);
	int T;
	scanf("%d", &T);
	int b[50];
	for (int k = 1; k <= T; k++) {
		int n;
		scanf("%d", &n);
		int sum = 0, P = 1000001;
		memset(b, 0, sizeof(int) * 50);
		int num;
		while (n--) {
			scanf("%d", &num);
			sum += num;
			P = min(P, num);
			int i = 0;
			while (num) {
				b[i++] += num % 2;
				num /= 2;
			}
		}
		bool ok = true;
		for (int i = 0; i < 50; i++) if (b[i] % 2) {
			ok = false;
			break;
		}
		if (ok) 
			printf("Case #%d: %d\n", k, sum - P);
		else
			printf("Case #%d: NO\n", k);

	}
	return 0;
}
