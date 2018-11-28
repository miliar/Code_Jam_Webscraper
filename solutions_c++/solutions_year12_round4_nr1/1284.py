#include<cstdio>
using namespace std;
int p[10005],q[10005],t[10005];
int nn,n,d,now,hei;
bool dfs(int i)
{
    if(hei>=d-now)
        return true;
    if(i>n)
        return false;
    int tmpnow,tmphei;
    for(int j=i; j<=n; ++j)
    {
        if(hei>=p[j]-now)
        {
            tmpnow=now;
            tmphei=hei;
            if(q[j]>=p[j]-now)
                hei=p[j]-now;
            else
                hei=q[j];
            now=p[j];
            if(hei>t[j])
            {
                t[j]=hei;
                if(dfs(j+1))
                    return true;
            }
            now=tmpnow;
            hei=tmphei;
        }
    }
    return false;
}
int main ()
{
    freopen("A-large.in","r",stdin);
    freopen("xx.out","w",stdout);
    scanf("%d",&nn);
    for(int i=1; i<=nn; ++i)
    {
        scanf("%d",&n);
        for(int j=1; j<=n; ++j)
        {
            scanf("%d%d",&p[j],&q[j]);
            t[j]=0;
        }
        scanf("%d",&d);
        printf("Case #%d: ",i);
        now=hei=p[1];
        if(dfs(2))
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}
