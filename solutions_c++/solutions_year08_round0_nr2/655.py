#include <cstdio>
#include <cstring>
const int maxn = 410;
int i,j,k,t,m,n,na,nb,hh,mm,interval,N;
int g[maxn][maxn];
int goes[maxn],st[maxn],en[maxn],maxmatch;
bool visit[maxn];

void build()
{
    memset(g,0,sizeof(g));
    n = na + nb;
    for (i = 1;i <= na; ++i)
        for (j = na+1; j <= na+nb; ++j)
            if (st[j] - en[i] >= interval)
                g[i][j] = 1;
            else if (st[i] - en[j] >= interval)
                g[j][i] = 1;
}

bool tryp(int j)
{
    if (visit[j])
        return false;
    visit[j] = true;
    for (int i = 1; i <= n; ++i)
        if (g[j][i] && (!goes[i] || tryp(goes[i])))
        {
            goes[i] = j;
            return true;
        }
    return false;
}

void match()
{
    memset(goes,0,sizeof(goes));
    maxmatch = 0;
    for (i = 1;i <= n; ++i) 
    {
        memset(visit,0,sizeof(visit));
        if (tryp(i))
            maxmatch ++;
    }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        scanf("%d",&interval);
        scanf("%d%d",&na,&nb);
        for (i = 1;i <= na + nb; ++i)
        {
            scanf("%d:%d",&hh,&mm);
            st[i] = hh * 60 + mm;
            scanf("%d:%d",&hh,&mm);
            en[i] = hh * 60 + mm;
        }
        build();
        match();
        int ans = 0;
        for (i = 1;i <= na; ++i)
            if (!goes[i])
                ans++;
        printf("Case #%d: %d",T,ans);
        ans = 0;
        for (i = na+1; i <= n; ++i)
            if (!goes[i])
                ans ++;
        printf(" %d\n",ans);
    }
    return 0;
}
