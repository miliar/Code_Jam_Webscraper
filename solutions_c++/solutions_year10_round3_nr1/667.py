#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#define MAXN 1005

int T,N,A[MAXN],B[MAXN];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int i,j,k,sum=0;
    
    scanf("%d",&T);
    
    for (i=0;i<T;i++)
    {
        sum = 0; 
        scanf("%d",&N);
        for (j=0;j<N;j++)
        {
            scanf("%d%d",A+j,B+j);
            for (k=0;k<j;k++)
            {
                if ((A[j]>A[k]&&B[j]<B[k])||(A[j]<A[k]&&B[j]>B[k]))
                sum++;
            }
        }
        printf("Case #%d: %d\n",i+1,sum);
    }

return 0;
}
