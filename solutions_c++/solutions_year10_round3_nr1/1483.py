#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int main() 
{
    freopen("A-small-attempt2.in","rt",stdin);
   	freopen("A-small-2.out","wt",stdout);
	int T;	int i,x,flag;
	scanf("%d",&T);

	for (i=0; i<T; i++) {
		int n, k;
		scanf("%d",&n);
		printf("\nCase #%d: ",i+1);		
        
        int A[n],B[n];
        int j=0;
        for(j=0;j<n;j++)
           scanf("%d %d",&A[j],&B[j]);     
   
        int count =0;
        for(j=0;j<n;j++)
           for(k=j;k<n;k++)
               if( abs(A[j]-A[k]) !=  abs(B[j]-B[k]) ) // not parallel
                 {
                   if( A[j]<A[k] && B[j]>B[k] )
                       count++;
                   else if (A[j]>A[k] && B[j]<B[k])
                       count++;                   
                 }
        printf("%d", count);               
	}
    return 0;
}

