#include "stdio.h"
#include "stdlib.h"
#include "string.h"

long long g[1010],sum[1010][2];


int main()
{
  
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    long long T,R,k,N ,i,j,p;
    
    scanf("%I64d",&T);
    for (p = 0; p<T;p++)
    {
        scanf("%I64d%I64d%I64d",&R,&k,&N);
        memset(g,0,sizeof(g));
        memset(sum,0,sizeof(sum));
        
        for (i=0;i<N;i++)
        {
            scanf("%I64d",g+i);
        }
        for (i=0;i<N;i++)
        {
            for (j=i;j<i+N;j++)
            {
                if (sum[i][0]+g[j%N]<=k)
                {
                   sum[i][0]+=g[j%N];
                   sum[i][1]=(j+1)%N;
                }
                else
                break;
            }
        }
        long long total=0,index=0;
        for (i=0;i<R;i++)
        {
            total +=  sum[index][0];
            //printf("sum=%I64d\n",sum[index][0]);
            index = sum[index][1];
        }
        printf("Case #%I64d: %I64d\n",p+1,total);
        
        
    }
    
    

return 0;
}
