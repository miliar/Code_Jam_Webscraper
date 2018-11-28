#include<stdio.h>

inline int min(int a, int b) {return a<b ? a : b; }

int nCase;
int N, D[16384], L[16384], M[16384], X;

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d", &N);
		for(int i = 0; i < N; ++i)
			scanf("%d %d", &D[i], &L[i]);
		scanf("%d", &X);
		D[N] = X;
		L[N] = 0;
		char ok = 0;
		M[0] = D[0];
		for(int i = 0, j = 1; i < N && !ok; ++i) {
			while(j <= N && D[i]+M[i] >= D[j]) {
				M[j] = min(D[j]-D[i], L[j]);
				++j;
			}
			if(j > N) ok = 1;
		}

		printf("Case #%d: %s\n", cs, ok?"YES":"NO");
	}
}

