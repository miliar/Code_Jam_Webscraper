#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int t, D, I, M, N, a[101], c[101][256];
	
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++) {
		scanf("%d %d %d %d", &D, &I, &M, &N);
		for (int j = 1; j <= N; j++)
			scanf("%d", &a[j]);
		
		for (int novo = 0; novo < 256; novo++) {
			c[0][novo] = 0;
			c[1][novo] = abs(novo - a[1]);
		}
		
		for (int j = 2; j <= N; j++) {
			for (int novo = 0; novo < 256; novo++) {
				c[j][novo] = abs(novo - a[j]);
				
				int custo = N * 256;
				
				for (int old = max(novo - M, 0); old <= min(novo + M, 255); old++) {
					custo = min(custo, c[j - 1][old]);
					custo = min(custo, c[j - 2][old] + D);
				}
				
				if (M > 0)
					for (int old = 0; old < 256; old++) {
						int insercoes = abs(novo - old) / M;
						if (insercoes > 0)
							insercoes -= (abs(novo - old) % M == 0);
						custo = min(custo, c[j - 1][old] + insercoes * I);
					}
				
				c[j][novo] += custo;
			}
		}
		
		/*for (int k = 0; k < 50; k++) {
			for (int j = 0; j <= N; j++)
				printf(" %d", c[j][k]);
			printf("\n");
		}*/
		
		int result = N * 256;
		
		for (int old = 0; old <= 255; old++) {
			result = min(result, c[N][old]);
			result = min(result, c[N - 1][old] + D);
		}
		
		printf("Case #%d: %d\n", i + 1, result);
	}
	
	return 0;
}
