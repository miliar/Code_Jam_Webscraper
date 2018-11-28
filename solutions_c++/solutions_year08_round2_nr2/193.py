#include <stdio.h>
#include <set>
using namespace std;

int i,j,k,pc,c;
long long A, B, P;
int s[1000];
int ns;
int p[1000], np;

int main() {
	np = 0;
	for (i = 2; i <= 1000; i++) {
		for (j = 2; j * j <= i; j++) {
			if (i % j == 0) break;
		}
		if (j * j > i) p[np++] = i; 
	}
	scanf("%d", &pc);
	for (c = 1; c <= pc; c++) {
		printf("Case #%d: ", c);
		scanf("%lld%lld%lld", &A, &B, &P);
		ns = 0;
		for (i = A; i <= B; i++) {
			s[ns++] = i;
		}
		for (i = A; i <= B; i++) {
			for (j = i + 1; j <= B; j++) {
				for (k = 0; k < np; k++) {
					if (i % p[k] == 0 && j % p[k] == 0 && p[k] >= P) {
//						printf("%d %d\n", i, j);
						if (s[i-A] != s[j-A]) {
							int q = s[i-A];
							for (int w = 0; w < ns; w++) {
								if (s[w] == q) s[w] = s[j-A];
							}
//							for (int w = 0; w < ns; w++) {
//								printf("%d ", s[w]);
//							}
//							printf("\n");
						}
					}
				}
			}
		}
		set<long long> y;
		y.clear();
		for (i = 0; i < ns; i++) y.insert(s[i]);
		printf("%d\n", y.size());
	}
	return 0;
}
