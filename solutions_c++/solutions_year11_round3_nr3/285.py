#include <cstdio>

const int N = 128;
int sd[N];

int main() {
	int t;
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		int n, l, h;
		scanf("%d%d%d", &n, &l, &h);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &sd[i]);
		}
		int ret = l;
		bool ok = false;
		for (ret = l; ret <= h; ++ret) {
			ok = true;
			for (int i = 0; i < n; ++i) {
				if (sd[i] % ret != 0 && ret % sd[i] != 0) {
					ok = false;
					break;
				}
			}
			if (ok) break;
		}
		printf("Case #%d: ", kase + 1);
		if (ok)
			printf("%d\n", ret);
		else
			printf("NO\n");
	}
	return 0;
}
