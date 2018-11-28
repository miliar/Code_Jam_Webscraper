#include<stdio.h>
#include<math.h>
long long arr1[40];
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("A-large (1).txt","w",stdout);
    long long test,cas,n,pd,pg,c1,p,b1,i,c2,pro,d,g,n1,d1,g1;
    scanf("%lld",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%lld%lld%lld",&n,&pd,&pg);
        if (!pd)
        {
            if (pg<100)
            {
                printf("Case #%lld: Possible\n",cas);
                continue;
            }
            else
            {
                printf("Case #%lld: Broken\n",cas);
                continue;
            }
        }
        if (!pg&&pd)
        {
            printf("Case #%lld: Broken\n",cas);
            continue;
        }
        c1=0;
        p=sqrt(pd*1.0);
        n1=pd;
        for (i=2;i<=p;i++)
        {
            if (!(n1%i))
            {
                while (!(n1%i))
                {
                    n1/=i;
                    arr1[c1++]=i;
                }
                p=sqrt(n1*1.0);
            }
        }
        if (n1>1)
        {
            arr1[c1++]=n1;
        }
        c2=0;
        for (i=0;i<c1;i++)
        {
            if (arr1[i]==2) c2++;
        }
        pro=1;
        while (c2<2)
        {
            pro*=2;
            c2++;
        }
        c2=0;
        for (i=0;i<c1;i++)
        {
            if (arr1[i]==5) c2++;
        }
        while (c2<2)
        {
            pro*=5;
            c2++;
        }
        if (pro>n)
        {
            printf("Case #%lld: Broken\n",cas);
            continue;
        }
        d=pro;
        for (i=0;i<c1;i++) pro*=arr1[i];
        pro/=100;
        d1=pro;
        c1=0;
        p=sqrt(pd*1.0);
        n1=pg;
        for (i=2;i<=p;i++)
        {
            if (!(n1%i))
            {
                while (!(n1%i))
                {
                    n1/=i;
                    arr1[c1++]=i;
                }
                p=sqrt(n1*1.0);
            }
        }
        if (n1>1)
        {
            arr1[c1++]=n1;
        }
        c2=0;
        for (i=0;i<c1;i++)
        {
            if (arr1[i]==2) c2++;
        }
        pro=1;
        while (c2<2)
        {
            pro*=2;
            c2++;
        }
        c2=0;
        for (i=0;i<c1;i++)
        {
            if (arr1[i]==5) c2++;
        }
        while (c2<2)
        {
            pro*=5;
            c2++;
        }
        g=pro;
        for (i=0;i<c1;i++) pro*=arr1[i];
        pro/=100;
        g1=g;
        //printf("%lld %lld\n",g1,g);
        if (g-g1<d-d1&&pg==100) printf("Case #%lld: Broken\n",cas);
        else printf("Case #%lld: Possible\n",cas);
    }
    return 0;
}
