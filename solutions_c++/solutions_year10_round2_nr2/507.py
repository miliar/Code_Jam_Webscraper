#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
using namespace std;

int v[100], X[100], V[100];

int main() {
	int _42=1, C, N, K, B, T;
	scanf(" %d", &C);
	while (C--) {
		scanf(" %d %d %d %d", &N, &K, &B, &T);
		for (int i=0;i<N;i++) {
			scanf(" %d", &X[i]);
		}
		for (int i=0;i<N;i++) {
			scanf(" %d", &V[i]);
		}
		memset(v, 0, sizeof(v));
		for (int i=0;i<N;i++) {
			if (((double)B - (double)X[i])/(double)V[i] > (double)T) {
				v[i] = -1;
			}
		}
		// qnts precisa pular
		for (int i=N-1;i>=0;i--) if (v[i] != -1) {
			for (int j=i+1;j<N;j++) {
				if (v[j] == -1) v[i]++;
			}
		}

		sort(v, v+N);
		//for (int i=0;i<N;i++) printf("%d ", v[i]);
		int cont = N;
		for (int i=0;i<N;i++) {
			if (v[i] > -1) {
				cont = i;
				break;
			}
		}
		int ans = 0;
		int tot = 0;
		for (int i=cont;i<N && i<cont+K;i++) {
			tot++;
			ans += v[i];
		}
		printf("Case #%d: ", _42++);
		if (tot < K)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
}
