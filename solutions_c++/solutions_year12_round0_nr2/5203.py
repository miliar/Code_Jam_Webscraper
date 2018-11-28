#include<stdio.h>

int main(){
	int T;
	int N, S, P;
	int i;
	int num[110];
	int ans;
	int count =0;
	scanf("%d", &T);
	while(T--){
		ans = 0;
		scanf("%d%d%d", &N, &S, &P);
		for(i = 0; i < N; i++){
			scanf("%d", &num[i]);
			if(num[i] >= (P-1)*2+P) ans++;
			else if(num[i] > 1 && S > 0 && num[i] >= 2*(P-2)+P){
				S--;
				ans++;
			}
		}
		printf("Case #%d: %d\n", ++count, ans);
		
	}
	return 0;
}
