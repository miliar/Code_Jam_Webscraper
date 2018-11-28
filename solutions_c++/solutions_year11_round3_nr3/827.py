#include <cstdio>
#include <algorithm>
#define MAXN 105
using namespace std;

int T, N, L, H;
int f[MAXN];
int lowf;

int main() {
	scanf("%d ", &T);
	for(int i = 0; i < T; i++) {
		scanf("%d%d%d", &N, &L, &H);
		for(int j = 0; j < N; j++) {
			scanf("%d", &f[j]);
		}
		for(lowf = L; lowf <= H; lowf++) {
			bool good = true;
			for(int j = 0; j < N && good; j++) {
				if(lowf % f[j] != 0 && f[j] % lowf != 0) {
					good = false;
				}
			}
			if(good) {
				break;
			}
		}
		if(lowf > H) {
			printf("Case #%d: NO\n", i + 1);
		} else {
			printf("Case #%d: %d\n", i + 1, lowf);
		}
	}
	return 0;
}
