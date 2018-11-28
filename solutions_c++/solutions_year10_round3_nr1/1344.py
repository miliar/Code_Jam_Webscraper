#include<stdio.h>
int main()
{
    freopen("jam.in","r",stdin);
    freopen("jam.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;++i)
    {
        int n,total=0;
        scanf("%d",&n);
        int a[n][2];
        for (int j=0;j<n;j++)
        {
            scanf("%d %d",&a[j][0],&a[j][1]);
        }
        for (int j=0;j<n;++j)
        {
            for (int k=j+1;k<n;++k)
            {
                if (((a[j][0]<a[k][0])&&(a[j][1]>a[k][1]))||((a[j][0]>a[k][0])&&(a[j][1]<a[k][1])))
                {total++;}
            }
        }
        printf("Case #%d: %d\n",i,total);
    }
}
