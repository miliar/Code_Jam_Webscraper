#include <cstdio>

const int inf=2147483647;
int f[200][300];
int a[300];
int n,m,ca,cb;

int abs(int x)
{
    if (x>0) return x;
    else return -x;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    scanf("%d",&T);    
    for (int run=1;run<=T;run++)
    {
        scanf("%d%d%d%d",&ca,&cb,&m,&n);
        for (int i=1;i<=n;i++)
            scanf("%d",a+i);
        printf("Case #%d: ",run);
        for (int i=0;i<256;i++) f[1][i]=abs(a[1]-i);
        for (int i=2;i<=n;i++)
            for (int j=0;j<256;j++)
            {
                f[i][j]=f[i-1][j]+ca;
                int t=inf;
                if (m)
                for (int k=0;k<256;k++)
                {
                    int z=abs(j-k)/m;
                    if (abs(j-k)%m==0&&z>0) z--;
                    t<?=f[i-1][k]+cb*z;
                }
                else t=f[i-1][j];
                f[i][j]<?=t+abs(a[i]-j);
            }
        int ans=inf;
        for (int i=0;i<256;i++) ans<?=f[n][i];
        printf("%d\n",ans);
    }
    return 0;
}
                    
                    
