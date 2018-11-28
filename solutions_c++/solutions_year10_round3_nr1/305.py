#include <stdio.h>


	int a[10000];

	int b[10000];


int isInter(int i,int j){
	long long  M = (long long )(a[i]-a[j]);
	long long  N = (long long )(b[i]-b[j]);
	if(M*N>0) return 0;
	return 1;

}
int main(){
	int T,N;
	scanf("%d",&T);


	for(int Case = 1;Case<=T;Case++){
		scanf("%d",&N);
		for(int i =0;i<N;i++){
			scanf("%d %d",&(a[i]),&(b[i]));
		}
		long long resp = 0;
		for(int i =0;i<N;i++){
			for(int j = 0;j<N;j++){
				if(isInter(i,j) && i!=j){
					resp++;
				}
			}
		}
		printf("Case #%d: %Ld\n",Case,resp/2LL);
	}
	return 0;
}
