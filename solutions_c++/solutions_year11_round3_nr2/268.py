#include<iostream>
#include<algorithm>
using namespace std;
int a[1005];
int dist[1000006];
int b[1000006];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    int i,j,n,l,ca,c,k;
    long long ans,x,t;
    scanf("%d",&ca);
    for(i=1;i<=ca;i++)
    {
        scanf("%d%lld%d%d",&l,&t,&n,&c);
        for(j=0;j<c;j++)
        scanf("%d",&a[j]);
        for(j=0;j<n;j++)
        dist[j]=a[j%c];
        x=0;
        for(j=0;j<n;j++)
        {
            x+=2*dist[j];
            if(x>=t) break;
        }
        int ww=j;
        if(j==n)
        {
            //printf("haha");
            printf("Case #%d: %lld\n",i,x);
            continue;
        }
        dist[j]=((int)(x-t))/2;
        for(k=j;k<n;k++)
        b[k-j]=dist[k];
        sort(b,b+n-j,greater<int>());
        for(k=j;k<n;k++)
        dist[k]=b[k-j];
        ans=t;
        for(j=ww;j<n;j++)
        {
                if(l>0)
                {
                    ans+=dist[j];
                    l--;
                }
                else ans+=dist[j]*2;
        }
        printf("Case #%d: %lld\n",i,ans);
    }
    return 0;
}

