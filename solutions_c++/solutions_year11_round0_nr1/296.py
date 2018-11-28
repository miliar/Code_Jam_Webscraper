#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	char buf[3];
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		int n;
		scanf("%d", &n);
		int res = 0, o = 1, b = 1;
		int obuf = 0, bbuf = 0;
		int tmp;
		for (int i = 0; i < n; i++) {
			scanf("%s %d", buf, &tmp);
			if (buf[0] == 'O') {
				int dis = abs(o - tmp);
				if (obuf < dis) {
					res += (dis - obuf);
					bbuf += (dis -obuf);
				}
				o = tmp;
				obuf = 0;
				res++; bbuf++;
			}else {
				int dis = abs(b - tmp);
				if (bbuf < dis) {
					res += (dis - bbuf);
					obuf += (dis -bbuf);
				}
				b = tmp;
				bbuf = 0;
				res++; obuf++;
			}
		}
		printf("Case #%d: %d\n", k, res);
	}
	return 0;
}
