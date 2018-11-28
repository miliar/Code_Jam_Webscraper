#include<iostream>
#define maxn 50

char ss[maxn];
int a[maxn];
int n,i,j,k,tmp,ans,l,t;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(l=1;l<=t;++l)
    {
        scanf("%d",&n);
        for(i=1;i<=n;++i)
        {
            scanf("%s",ss);
            a[i]=1;
            for(j=n-1;j>=0;--j)if(ss[j]=='1')
            {
                a[i]=j+1;
                break;
            }
        }
        ans=0;
        for(i=1;i<=n;++i)
        {
            if(a[i]<=i)continue;
            for(j=i+1;j<=n;++j)if(a[j]<=i)break;
            ans+=j-i;
            tmp=a[j];
            for(k=j;k>i;--k)a[k]=a[k-1];
            a[i]=tmp;
        }
        printf("Case #%d: %d\n",l,ans);
    }
    return 0;
}
