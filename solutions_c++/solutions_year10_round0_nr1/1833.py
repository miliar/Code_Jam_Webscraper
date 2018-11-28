# include <stdio.h>

int main (void){
	int tc = 1;
	int T, N, K;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &N, &K);
		printf("Case #%d: ", tc++);
		int cnt = 0;
		for(int i = 0;i<N;i++){
			if(K & (1<<i) ) cnt++;
		}
		if(cnt == N) printf("ON\n");
		else printf("OFF\n");
	}
}