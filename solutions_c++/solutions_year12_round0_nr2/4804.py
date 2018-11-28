#include<stdio.h>
int main()
{
	int test;
	int N;
	int S;
	int P;
	int temp;
	int count;
    
	int a[10010];
    	scanf("%d",&test);
    	for(int j=0; j<test; j++){
        	count=0;
        	scanf("%d %d %d",&N,&S,&P);
        	for(int i=0; i<N; i++){
            		scanf("%d",&a[i]);
        	}
        	if(P==0){
            		printf("Case #%d: %d\n",j+1,N);
            		continue;
        	}
		temp=P*3;

        	for(int i=0; i<N; i++){
            		if((a[i]+2)>=temp && a[i]>=1){
            			count++;
            		}else{
            			if(((a[i]+4)>=temp) && S>0 && a[i]>=2){
					count++;
					S--;
				}
			}
		}
        	printf("Case #%d: %d\n",j+1,count);
    	}
    return 0;
}
