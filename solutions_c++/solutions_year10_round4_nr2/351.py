#include <cstdio>
#include <cstring>

int a[1500],c[1500][1500],f[2500][30],bh[1500][1500];
int m,n;

int main()
{
    freopen("b1.in","r",stdin);
    freopen("b1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&m); n=1<<m;
        for (int i=1;i<=n;i++) scanf("%d",a+i);
        memset(f,0xff,sizeof(f));
        int num=0;
        for (int j=1;j<=n;j++) bh[m+1][j]=++num;
        for (int i=m;i;i--)
            for (int j=1;j<=1<<(i-1);j++)
            {
                scanf("%d",&c[i][j]);
                bh[i][j]=++num;
            }
        for (int i=1;i<=n;i++)
            for (int j=m-a[i];j<=m;j++) f[bh[m+1][i]][j]=0;
        for (int i=m;i;i--)
        {
            int q=bh[i+1][1];
            for (int j=1;j<=1<<(i-1);j++)
            {
                int p=bh[i][j];
                for (int k=0;k<=i-1;k++)
                {
                    if (f[q][k]!=-1&&f[q+1][k]!=-1) f[p][k]=f[q][k]+f[q+1][k];
                    if (f[q][k+1]!=-1&&f[q+1][k+1]!=-1)
                       if (f[p][k]==-1||f[q][k+1]+f[q+1][k+1]+c[i][j]<f[p][k])
                           f[p][k]=f[q][k+1]+f[q+1][k+1]+c[i][j];
                }
                q+=2;
            }
        }
        printf("Case #%d: %d\n",cas,f[bh[1][1]][0]);
    }
    return 0;
}
            
                       
        
    
