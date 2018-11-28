#include <stdio.h>
#include <memory.h>
int t,ans;
bool fl;
int tests;
int n;
int v[2][110][110];
int x1,x2,y1,y2;
int main()
{
    freopen("csmall.in","r",stdin);
    freopen("csmall.out","w",stdout);
    scanf("%d",&tests);
    for (int t0=1;t0<=tests;t0++)
    {
        scanf("%d",&n);
        memset(v,0,sizeof(v));
        for (int i=1;i<=n;i++)
        {
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for (int j=x1;j<=x2;j++)
              for (int k=y1;k<=y2;k++) v[0][j][k]=1;
        }
        t=0;
        fl=true;

        ans=0;
        while (fl)
        {
            t=1-t;
            fl=false;            
            for (int i=1;i<=100;i++)
            {
                for (int j=1;j<=100;j++)
                {
                    if (v[1-t][i][j]==0&&v[1-t][i-1][j]==1&&v[1-t][i][j-1]==1) v[t][i][j]=1;
                    else
                        if (v[1-t][i][j]==1&&v[1-t][i-1][j]==0&&v[1-t][i][j-1]==0) v[t][i][j]=0;
                        else v[t][i][j]=v[1-t][i][j];
                    if (v[t][i][j]) fl=true;                    
                }                
            }
            ans++;            
        }
        printf("Case #%d: %d\n",t0,ans);
    }
}
