#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
const int maxn = 1001;
int L, t, N, C;
int sum[maxn];
int CC[maxn];
int tmp[maxn];


int main() {
	int T;
	scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		scanf("%d %d %d %d", &L, &t, &N, &C);
		for (int i = 0; i < C; i++)
			scanf("%d", &tmp[i]);
		int index = 0;
		sum[0] = 0;
		for (int i = 1; i <= N; i++) {
			CC[i] = tmp[index++] * 2;
			sum[i] = sum[i - 1] + CC[i];
			index %= C;
		}
		printf("Case #%d: ", k);
		if (L == 0) 
			printf("%d\n", sum[N]);
		else if (L == 1 || N == 1) {
			int maxx = 0;
			for (int i = 1; i <= N; i++) {
				int cmaxx;
				if (sum[i - 1] >= t) 
					cmaxx = CC[i] / 2;
				else {
					if (sum[i] >= t) 
						cmaxx = (sum[i] - t) / 2;
					else 
						cmaxx = 0;
				}
				if (cmaxx >= maxx)
					maxx = cmaxx;
			}
			printf("%d\n", sum[N] - maxx);
		}else {
			int maxx = 0;
			for (int i = 1; i < N; i++) {
				for (int j = i + 1; j <= N; j++) {
					int cmaxx;
					if (sum[i - 1] >= t) 
						cmaxx = CC[i] / 2;
					else {
						if (sum[i] >= t) 
							cmaxx = (sum[i] - t) / 2;
						else 
							cmaxx = 0;
					}
					int tmaxx;
					if (sum[j - 1] - cmaxx >= t) 
						tmaxx = CC[j] / 2;
					else {
						if (sum[j] - cmaxx >= t)
							tmaxx = (sum[j] - cmaxx - t) / 2;
						else
							tmaxx = 0;
					}
					if (cmaxx + tmaxx > maxx)
						maxx = cmaxx + tmaxx;
				}
			}
			printf("%d\n", sum[N] - maxx);
		}
	}
	return 0;
}
