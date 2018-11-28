#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define max(a,b)    a>b?a:b;
#define min(a,b)    a<b?a:b;
#define INF 0x3fffffff

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    long long n,pd,pg;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        scanf("%I64d%I64d%I64d",&n,&pd,&pg);
        int mark=0;
        if(pg==0)
        {
            if(pd==0)   mark=1;
        }
        else if(pg==100)
        {
            if(pd==100) mark=1;
        }
        else if(n>=100)
        {
            mark=1;
        }
        else
        {
            for(long long i=1;i<=n;i++)
            {
                long long ans=i*pd;
                if(ans%100==0)
                {
                    mark=1;
                    break;
                }
            }
        }
        if(mark)    printf("Case #%d: Possible\n",cas);
        else        printf("Case #%d: Broken\n",cas);
    }
    return 0;
}
