#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn=10000+10;
int w[maxn],l[maxn];
int opt[maxn];
int n,t,id;

int main()
{
    for (scanf("%d",&t);t--;)
    {
        scanf("%d",&n);
        for (int i=1;i<=n;i++) scanf("%d%d",&w[i],&l[i]);
        scanf("%d",&w[n+1]);l[n+1]=0;
        for (int i=0;i<=n+1;i++) opt[i]=-1;
        opt[0]=0;
        
        opt[1]=w[1];
        for (int i=1;i<=n;i++)
        if (opt[i]>=0)
            for (int j=i+1;j<=n+1;j++)
            {
                if (w[j]-w[i]<=opt[i])
                    opt[j]=max(opt[j],min(l[j],w[j]-w[i]));
            }
        printf("Case #%d: ",++id);
        if (opt[n+1]>=0) printf("YES\n");
        else printf("NO\n");
    }
}

                
