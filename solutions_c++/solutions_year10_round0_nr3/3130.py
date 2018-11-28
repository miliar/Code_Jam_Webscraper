#include<stdio.h>
#include<math.h>

int main() 
{
    freopen("C-small-attempt0.in","rt",stdin);
   	freopen("C-small.out","wt",stdout);
	int T;	int i,j,sum,x,index,groupSum,startIndex;
	scanf("%d",&T);
	for (i=0; i<T; i++) {
		int R,k,n;
		scanf("%d",&R);
		scanf("%d",&k);
		scanf("%d",&n);
		int g[k];
		for (j=0; j<n; j++) 
          	scanf("%d",&g[j]); 
		printf("\nCase #%d: ",i+1);		
       	sum=0;
		x=0;index=0;
      
        for(x=0;x<R;x++){
            groupSum = 0;
            startIndex = index;
            while( (groupSum + g[index]) <= k){
                   groupSum += g[index];                                                        
                   index= (index+1)%n;
                   if(startIndex==index) break;
            }  
            sum += groupSum; 
        }
        printf("%d",sum);
	}
    return 0;
}
