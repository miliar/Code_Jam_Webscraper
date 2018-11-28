#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;


int main()
{
    freopen("C-large (1).in","r",stdin);
    freopen("outcl.txt","w",stdout);
    int T,N,i,sum,ans,minv,v;
    scanf("%d",&T);
    int ks=0;
    while(T--)
    {
        scanf("%d",&N);
        ans=0;
        sum=0;
        minv=999999999;
        for(i=0;i<N;i++)
        {
            scanf("%d",&v);
            sum+=v;
            ans^=v;
            minv=minv>v?v:minv;
        }
        printf("Case #%d: ",++ks);
        if(ans)
        {
            printf("NO\n");
        }
        else
        {
            printf("%d\n",sum-minv);
        }
    }
    return 0;
}
