#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    __int64 i,j,k,l,t,kase=1,pd,pg,n,p[109],a,b;
    p[0]=0;
    for (i=1;i<101;i++)
    {
        a=i;
        b=100;
        for (j=1;j<=i;j++)
        {
            if (a%j==0 && b%j==0)
            {
                a=a/j;
                b=b/j;
                j=1;
            }
        }
        //if(i==80)
        //printf("a%d b%d\n",a,b);
        p[i]=b;
    }
    scanf("%I64d",&t);
    while (t--)
    {
        scanf("%I64d %I64d %I64d",&n,&pd,&pg);
        //printf(">>%d\n",p[pd]);
        if (p[pd]<=n)
        {
            if ((pg==100 && pd<100)||(pg==0 && pd>0))
                printf("Case #%I64d: Broken\n",kase++);
            else
                printf("Case #%I64d: Possible\n",kase++);
        }
        else
            printf("Case #%I64d: Broken\n",kase++);
    }
    return 0;
}
