/* GCJ' 10 Theme Park
 * Radar798
 */
#include<stdio.h>
	int T;
    int R[55],k[55],N[55];
	long g[55][21];

void init(){
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		scanf("%d %d %d",&R[i],&k[i],&N[i]);
		for(int j=1;j<=N[i];j++)scanf("%ld",&g[i][j]);
	}
}

void roller(int m){
	int max=0,sum=0,total=0;
	for(int j=1,s=1;max<R[m];j++){
		if(j>20)j-=20;
		sum+=g[m][j];
		if(sum<=k[m]&&s<=N[m]){
			if((N[m]+j)>20){
			g[m][N[m]+j-20]=g[m][j];
            total+=g[m][j];
			s++;
			}
			else{
			g[m][N[m]+j]=g[m][j];
            total+=g[m][j];
			s++;
			}
		}
		else{
			max++;
            sum=0;
			s=1;
			j--;
		}
		
	}
	printf("Case #%d: %ld\n",m,total);
}

int main(void){
    freopen("C-small-attempt6.in","r",stdin);
    freopen("C-small-attempt6.out","w",stdout);
	init();
	for(int w=1;w<=T;w++)roller(w);
    return 0;
}	
