#include<iostream>
using namespace std;
int i,j,a,b,l,l1,l2,ans,n,k;

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("c1.out","w",stdout);
    scanf("%d",&n);
    for (i=1;i<=n;i++)
    {
        ans=0;
        scanf("%d %d",&a,&b);
        for (j=a;j<=b;j++)
            for (k=j+1;k<=b;k++)
            {
                if (j/1000>0)
                {
                    l=(j%1000)*10+j/1000;
                    l1=(l%1000)*10+l/1000;
                    l2=(l1%1000)*10+l1/1000;
                    if (l==k||l1==k||l2==k) ans++;
                }
                else if ((j/100>0)&&(k/1000==0))
                {
                     l=(j%100)*10+j/100;
                     l1=(l%100)*10+l/100;
                     if (l==k||l1==k) ans++;
                }
                else if ((j/10>0)&&(k/1000==0)&&(k/100==0))
                {
                     l=(j%10)*10+j/10;
                     if (l==k) ans++;
                }
            }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
