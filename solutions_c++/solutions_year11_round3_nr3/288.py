#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main(){
	int T;
	int t,i,j,k;
	int N , L,H;
	int count=0;
	scanf("%d",&T);
	int other[20000];
	for(t=1;t<=T;t++){
		memset(other,0,sizeof(other));
		scanf("%d %d %d",&N,&L,&H);
			for(i=0;i<N;i++)
			scanf("%d",&other[i]);
		printf("Case #%d: ",t);
		for(i=L;i<=H;i++){
			for(j=0;j<N;j++){
				if(!(other[j]%i==0 || i%other[j]==0))
				break;
			}
			if(j==N){
				printf("%d\n",i);
				break;
			}
		}
		if(i==H+1){
			printf("NO\n");
		}
				

	}


	return 0;
}
