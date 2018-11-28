#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAX = 1200;
int a[MAX];

int main() {
	int T, cas = 1;
	int n, s, mi;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", cas++);
		mi = 0x3f3f3f3f;
		scanf("%d", &n);
		s = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			s ^= a[i];
			mi = min(mi, a[i]);
			if (i)
				a[i] += a[i - 1];
		}
		if (s) {
			puts("NO");
		} else {
			printf("%d\n", a[n - 1] - mi);
		}
	}

	return 0;
}
