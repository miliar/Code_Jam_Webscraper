#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int d[10022];
int l[19002];
int p[10002];
int main()
{
    int T;
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
    scanf("%d",&T);
    int D;
    for(int cas=1;cas<=T;cas++)
    {
        memset(p,0,sizeof(p));
        printf("Case #%d: ",cas);
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&d[i],&l[i]);
        }
        scanf("%d",&D);
        int t=0,a=0;
        int tmp=min(d[0],l[0]);
        int flag=0;
        l[0]=d[0];
        p[0]=l[0];
        d[n]=D;
        for(int i=1;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                if(d[j]+p[j]>=d[i])
                p[i]=max(p[i],min(d[i]-d[j],l[i]));
            }
        }
        for(int i=0;i<n;i++)
        {
            if(d[i]+p[i]>=D)
            flag=1;
        }
        if(flag)
        printf("YES\n");
        else printf("NO\n");
    }
}
