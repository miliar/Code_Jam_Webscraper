#include <stdio.h>

int a[1005];

int gcd(int x,int y)
{
    return y==0?x:gcd(y,x%y);    
}

int Min(int x,int y)
{
    return x<y?x:y;    
}

int main()
{
    freopen("cc.in","r",stdin);
    freopen("cc.out","w",stdout);
    int i,j,n,T,l,h,cnt;
    cnt=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d%d",&n,&l,&h);
        for (i=0;i<n;i++)
        {
            scanf("%d",&a[i]);    
        }         
        for (i=l;i<=h;i++)
        {
            for (j=0;j<n;j++)
            {
                if (gcd(a[j],i)!=Min(a[j],i)) break;    
            }
            if (j==n) break;
        }
        printf("Case #%d: ",cnt++);
        if (i>h) printf("NO\n");
        else printf("%d\n",i);
    }    
    return 0;
}
