#include <iostream>
#include <cmath>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas,t,n;
    int a[15000],b[15000];
    int i,j,cou;
    scanf("%d",&cas);
    for (t=1;t<=cas;t++)
    {
        scanf("%d",&n);
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        for(i=0;i<n;i++) scanf("%d %d",&a[i],&b[i]);
        cou=0;
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if((a[i]-a[j])*(b[i]-b[j])<0) cou++;
            }
        }
        printf("Case #%d: ",t);
        printf("%d\n",cou);
    }
    return 0;
}
