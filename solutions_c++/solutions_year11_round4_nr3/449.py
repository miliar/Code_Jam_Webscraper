#include<stdio.h>
int a[10000];
bool b[10001];
int n,tt,t;

int main()
{
    a[0]=0;
    for (int i=2;i<=1000;i++)
    if (!b[i])
    {
        a[0]++;
        a[a[0]]=i;
        int j=i+i;
        while (j<=1000)
        {
              b[j]=true;
              j+=i;
        }
    }
    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&tt);
    for (int t=1;t<=tt;t++)
    {
        scanf("%d",&n);
        int max,min;
        max=1;min=0;
        for (int i=1;i<=a[0];i++)
        if (a[i]<=n)
        {
                    min++;
                    int m=n;
                    while (m>=a[i]) {max++;m/=a[i];}
        }
        if (n==1) {max=0;}
        printf("Case #%d: %d\n",t,max-min);
    }
    return 0;
}
