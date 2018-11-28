#include <stdio.h>

unsigned int A[1010];

int main()
{
    int T,i,N,j;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d",&N);
        for(j=0;j<N;j++)
             scanf("%ud",&A[j]);
        int sum=0;
        int min=10000000;
        unsigned int xor_var=0;
        for(j=0;j<N;j++)
        {
            xor_var=xor_var ^ A[j];
            sum+=A[j];
            min=(A[j]<min)?A[j]:min;  
        }
        if (xor_var!=0)
        {
              printf("Case #%d: NO\n",i);               
        }
        else
        {
              printf("Case #%d: %d\n",i,sum-min); 
        }
                       
    }
    
    return 0;      
}
