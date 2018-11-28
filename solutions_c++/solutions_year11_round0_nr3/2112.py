#include<cstdio>
int T, N, sum, min, xr;
int main(){
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		min = 999999999;
		sum = xr = 0;
		scanf("%d", &N);
		for(int i = 0; i < N; i++){
			int tmp;
		    scanf("%d", &tmp);
		    if(tmp < min)min = tmp;
		    sum += tmp;
		    xr ^= tmp;
		}
		printf("Case #%d: ", t);
		if(xr)puts("NO");
		else printf("%d\n", sum - min);
	}
}
