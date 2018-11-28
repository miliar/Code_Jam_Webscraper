#include<stdio.h>
#include<stdlib.h>
int N;
int d[10021];
int l[10021];
int D;
int lowest[10021];
int max(int a,int b){
	if(a > b)return a;
	return b;
}
int min(int a,int b){
	if(a < b)return a;
	return b;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++){
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			scanf("%d %d",&d[i],&l[i]);
			lowest[i] = -1;
		}
		lowest[0] = d[0];
		scanf("%d",&D);

		int idx = 0;
		int flag = 0;
		for(int i=0;i<N;i++){
			int nowHL = lowest[i];
			int Limit = d[i] + nowHL;
			if(Limit >= D){
				flag = 1;
				break;
			}
			for(;idx < N && d[idx] <= Limit;idx++){
				lowest[idx] = min(l[idx],d[idx] - d[i]);
			}
		}
		printf("Case #%d: ",ca);
		if(flag == 1){
			printf("YES\n");
		}else{
			printf("NO\n");
		}
	}
	return 0;
}
