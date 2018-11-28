#include <cstdio>
#include <algorithm>
using namespace std;

int n;

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d", &n);
		int posB = 1, b = 0, posO = 1, o = 0;
		int ret = 0, d = 0;
		for (int i = 1; i <= n; ++i) {
			char c[10]; int x;
			scanf("%s%d", c, &x);
			if (c[0] == 'B') {
				b += abs(x - posB);
				if (b <= o) {
					ret += o;
					b = o = 0;
				}
				++b;
				posB = x;
			} else {
				o += abs(x - posO);
				if (o <= b) {
					ret += b;
					b = o = 0;
				}
				++o;
				posO = x;
			}
		}
		ret += max(o, b);
		printf("Case #%d: ", cas);
		printf("%d\n", ret);
	}
	return 0;
}
