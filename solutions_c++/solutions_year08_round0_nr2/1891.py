#include <cstdio>
#include <cstring>
using namespace std;

const int M = 1440;

int main() {
	int n, t, na, nb;
	int sta[M], stb[M], arva[M], arvb[M];
	scanf("%d", &n);
	for (int k = 1; k <= n; ++k) {
		int a, b, c, d;
		int reta = 0, retb = 0;
		int poola = 0, poolb = 0;
		memset(sta, 0, sizeof(sta));
		memset(stb, 0, sizeof(stb));
		memset(arva, 0, sizeof(arva));
		memset(arvb, 0, sizeof(arvb));
		scanf("%d%d%d", &t, &na, &nb);
		for (int i = 0; i < na; ++i) {
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			sta[a * 60 + b] ++;
			arvb[c * 60 + d + t] ++;
		}
		for (int i = 0; i < nb; ++i) {
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			stb[a * 60 + b] ++;
			arva[c * 60 + d + t] ++;
		}
		for (int i = 0; i < M; ++i) {
			if (arva[i] > 0) {
				poola += arva[i];
				arva[i] = 0;
			}
			if (arvb[i] > 0) {
				poolb += arvb[i];
				arvb[i] = 0;
			}
			if (sta[i] > 0) {
				if (poola >= sta[i]) {
					poola -= sta[i];
				} else {
					reta += sta[i] - poola;
					poola = 0;
				}
				sta[i] = 0;
			}
			if (stb[i] > 0) {
				if (poolb >= stb[i]) {
					poolb -= stb[i];
				} else {
					retb += stb[i] - poolb;
					poolb = 0;
				}
				stb[i] = 0;
			}
		}
		printf("Case #%d: %d %d\n", k, reta, retb);
	}
	return 0;
}

