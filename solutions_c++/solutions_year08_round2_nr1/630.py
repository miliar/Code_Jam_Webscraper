#include <stdio.h>

int main()
{
    __int64 x[200],y[200],a,b,c,d,m;
    int i,j,k,n,t,sum,q=1;
    
    for (scanf("%d",&t);t>0;t--)
    {
        scanf("%d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&a,&b,&c,&d,&x[0],&y[0],&m);
        for (i=1;i<n;i++)
        {
            x[i]=(a*x[i-1]+b)%m;
            y[i]=(c*y[i-1]+d)%m;
        }
        sum=0;
        for (i=0;i<n;i++)
        {
            for (j=i+1;j<n;j++)
            {
                for (k=j+1;k<n;k++)
                {
                    if ((x[i]+x[j]+x[k])%3==0&&(y[i]+y[j]+y[k])%3==0)
                    sum++;
                }
            }
        }
        printf("Case #%d: %I64d\n",q++,sum);
    }
    return 0;
}                       

        
