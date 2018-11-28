#include <stdio.h>

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,n,T,m,x,s,t,cnt;
    scanf("%d",&T);
    cnt=1;
    while(T--)
    {
        m=10000000;
        s=0;
        t=0;
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%d",&x);
            s=s^x;
            t+=x;
            if (x<m) m=x;   
        }    
        printf("Case #%d: ",cnt++);
        if (s!=0) printf("NO\n");
        else printf("%d\n",t-m);
    }
    return 0;
}
