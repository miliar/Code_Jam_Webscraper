#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 22;
const int MaxS = 1 << MaxN;
int DP[MaxS], a[MaxN];
int N, M;

bool sol() {
	bool fd;
	for (int mask1 = 1; mask1 < M; mask1++) {
		int mask2 = (~mask1) & (M - 1);
		for (int ns = mask2; ns; ns = (ns - 1) & mask2) {
			if (DP[mask1] == DP[ns]) {
				fd = false;
				for (int i = 0; i < N; i++)
					if (mask1 & (1 << i)) {
						if (fd) putchar(' ');
						else fd = true;
						printf("%d", a[i]);
					}
				puts("");
				fd = false;
				for (int i = 0; i < N; i++)
					if (ns & (1 << i)) {
						if (fd) putchar(' ');
						else fd = true;
						printf("%d", a[i]);
					}
				puts("");
				return true;
			}
		}
	}
	return false;
}

int main() {
	int T;
	int cas = 1;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &a[i]);
		}
		printf("Case #%d:\n", cas++);
		M = 1 << N;
		DP[0] = 0;
		for (int mask = 1; mask < M; mask++) {
			int ns = mask & -mask;
			for (int j = 0; j < ns; j++) {
				if (ns & (1 << j)) {
					DP[mask] = DP[mask ^ ns] + a[j];
					break;
				}
			}
		}
		if (!sol()) {
			puts("Impossible");
		}
	}
	
	return 0;
}

