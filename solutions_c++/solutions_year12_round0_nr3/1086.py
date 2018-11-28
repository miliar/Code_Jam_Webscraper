#include<stdio.h>

typedef struct Pair {
	int a, b;
	Pair() {}
	Pair(int x, int y):a(x), b(y) {}
}Pair;

int nCase;
int A, B, nP, G[1<<21], TEN[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
int K[1<<21];
Pair P[1<<25];

int main() {
	for(int i = 1; i < 10; ++i) G[i] = 1;
	for(int i = 10; i < 100; ++i) G[i] = 2;
	for(int i = 100; i < 1000; ++i) G[i] = 3;
	for(int i = 1000; i < 10000; ++i) G[i] = 4;
	for(int i = 10000; i < 100000; ++i) G[i] = 5;
	for(int i = 100000; i < 1000000; ++i) G[i] = 6;
	for(int i = 1000000; i <= 2000000; ++i) G[i] = 7;
	for(int i = 1; i <= 2000000; ++i) {
		for(int j = 1; j < G[i]; ++j) {
			int t = i/TEN[j] + (i%TEN[j]) * TEN[G[i]-j];
			if(t <= 2000000 && i < t && G[t] == G[i] && K[t] != i) {
				P[nP++] = Pair(i, t);
				K[t] = i;
			}
		}
	}
	//fprintf(stderr, "np = %d\n", nP);
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d %d", &A, &B);
		int ans = 0;
		for(int i = 0; i < nP; ++i) {
			if(A <= P[i].a && P[i].b <= B) {
				++ans;
			//	printf("%d %d\n", P[i].a, P[i].b);
			}
		}
		printf("Case #%d: %d\n", cs, ans);
	}
}



