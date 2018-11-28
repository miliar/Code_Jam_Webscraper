#include <iostream>

#define rep(i, n) for(int i=0; i<(n); i++)

using namespace std;

int main(void) {
	int T, N;
	int c[15];
	int v1, v2;
	int s1, s2;
	int ret;

	scanf("%d", &T);
	rep(u, T) {
		scanf("%d", &N);
		rep(i, N) scanf("%d", &c[i]);

		ret = -1;
		rep(i, 1<<N) {
			v1 = 0; s1 = 0;
			v2 = 0; s2 = 0;
			rep(j, N) {
				if (i&(1<<j)) {
					v1 ^= c[j];
					s1 += c[j];
				} else {
					v2 ^= c[j];
					s2 += c[j];
				}
			}
			if (v1 == v2 && v1 > 0 && v2 > 0) {
				//printf("@@ %d %d %d %d\n", v1, v2, s1, s2);
				//printf("@@ %x %d\n", i, max(s1, s2));
				ret = max(ret, max(s1, s2));
			}
		}

		if (ret == -1) printf("Case #%d: NO\n", u+1);
		else printf("Case #%d: %d\n", u+1, ret);
	}

	return 0;
}
