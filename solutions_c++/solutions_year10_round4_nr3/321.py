#include <cstdio>
#include <cstring>
bool a[200][200];
int m;

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        memset(a,0,sizeof(a));
        scanf("%d",&m);
        for (int k=1;k<=m;k++)
        {
            int x1,x2,y1,y2;
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for (int i=x1;i<=x2;i++)
                for (int j=y1;j<=y2;j++)
                    a[i][j]=1;
        }
        int ans;
        for (ans=0;;ans++)
        {
            bool ok=0;
            for (int i=100;i;i--)
                for (int j=100;j;j--)
                    if (a[i][j])
                    {
                        ok=1;
                        if (!a[i-1][j]&&!a[i][j-1]) a[i][j]=0;
                    }
                    else
                        if (a[i-1][j]&&a[i][j-1]) a[i][j]=1;
            if (!ok) break;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
    
