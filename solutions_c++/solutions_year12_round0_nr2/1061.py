#include<stdio.h>

int nCase;
int N, S, P, C[32], M[32][2];

int main() {
	for(int i = 0; i <= 10; ++i)
		for(int j = i; j <= 10 && j <= i+2; ++j)
			for(int k = i; k <= j; ++k) {
				int t = i + j + k, b = (j-i==2) ? 1 : 0;
				if(M[t][b] < j) M[t][b] = j;
			}
//	for(int i = 0; i <= 30; ++i)
//		fprintf(stderr, "%4d %4d %4d\n", i, M[i][0], M[i][1]);
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d %d %d", &N, &S, &P);
		for(int i = 0; i < 32; ++i) C[i] = 0;
		for(int i = 0; i < N; ++i) {
			int a;
			scanf("%d", &a);
			++C[a];
		}
		int ans = 0;
		for(int i = 30; i >= 0; --i) {
			if(C[i] == 0) continue;
			if(M[i][0] >= P) ans += C[i];
			else if(M[i][1] >= P) {
				int m = (S<C[i]) ? S : C[i];
				ans += m;
				S -= m;
				//fprintf(stderr, "\t%d %d %d\n", i, m, ans);
			}
		}
		printf("Case #%d: %d\n", cs, ans);
	}
}


