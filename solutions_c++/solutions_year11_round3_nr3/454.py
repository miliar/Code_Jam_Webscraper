#include<stdio.h>
#include<stdlib.h>
int f[10003];
int N,L,H;
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		scanf("%d %d %d",&N,&L,&H);
		for(int i=0;i<N;i++){
			scanf("%d",&f[i]);
		}
		int ans = -1;
		for(int i=L;i<=H;i++){
			int flag = 0;
			for(int j=0;j<N;j++){
				if(i % f[j] == 0 || f[j] % i == 0){
					continue;
				}
				flag = 1;
				break;
			}
			if(flag == 0){
				ans = i;
				break;
			}
		}
		printf("Case #%d: ",t + 1);
		if(ans == -1){
			printf("NO\n");
		}else{
			printf("%d\n",ans);
		}
	}
}
