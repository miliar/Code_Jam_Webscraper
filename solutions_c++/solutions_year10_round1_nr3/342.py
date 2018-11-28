#include<stdio.h>
bool win[1003];
int m1[1003],c1;
void gcd(int a,int b)
{
    while (true)
    {
        m1[c1++]=a/b;
        if (!(a%b)) return ;
        a%=b;
        m1[c1++]=b/a;
        if (!(b%a)) return ;
        b%=a;
    }
}
int main()
{
    freopen("inc.txt","r",stdin);
    freopen("outc.txt","w",stdout);
    int test,cas,a1,b1,b2,a2,sum,i,j,k;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
        sum=0;
        for (i=a1;i<=a2;i++)
        {
            for (j=b1;j<=b2;j++)
            {
                c1=0;
                if (i<j) gcd(j,i);
                else gcd(i,j);
                if (m1[c1-1]==1) win[c1-1]=0;
                else win[c1-1]=1;
                for (k=c1-2;k>=0;k--)
                {
                    if (m1[k]==1) win[k]=!win[k+1];
                    else win[k]=1;
                }
                if (win[0]) sum++;
            }
        }
        printf("Case #%d: %d\n",cas,sum);
    }
    return 0;
}
