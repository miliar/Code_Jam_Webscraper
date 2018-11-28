#include <cstdio>

int main() {
	int C, N, K, B, T;
	int X[100], V[100];
	bool possible[100];
	scanf("%d", &C);
	for (int c=0;c<C;++c) {
		scanf("%d%d%d%d", &N, &K, &B, &T);
		for(int n=0;n<N;++n) scanf("%d",X+n);
		for(int n=0;n<N;++n) scanf("%d",V+n), possible[n] = (V[n]*T>=B-X[n]);
		int swaps = 0;
		for(int n=N-1;n>=0 && K>0;--n) {
			if(possible[n]) --K;
			else swaps+=K;
		}
		printf("Case #%d: ", c+1);
		if(K>0) printf("IMPOSSIBLE\n");
		else printf("%d\n",swaps);
	}
}