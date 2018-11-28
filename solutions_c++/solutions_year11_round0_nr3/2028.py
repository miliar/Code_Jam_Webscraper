#include <cstdio>
#include <cstring>

int candy[1010], min, sum, N, T, cnt[20];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	for(int cc=1; cc<=T; cc++) {
		min = 1000000000;
		sum = 0;
		memset(cnt, 0, sizeof(cnt));
		scanf("%d", &N);
		for(int i=0; i<N; i++) {
			scanf("%d", candy+i);
			sum += candy[i];
			for(int j=candy[i], k=0; j; j>>=1, k++) {
				cnt[k] += (j&1);
			}
			if(min > candy[i]) min = candy[i];
		}
		int can = true;
		for(int i=0; i<20; i++) {
			if(cnt[i]%2) can = false;	
		}
		printf("Case #%d: ", cc);
		if(!can) puts("NO");
		else printf("%d\n", sum-min);
	}
}
