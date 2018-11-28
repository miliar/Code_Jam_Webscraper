#include <stdio.h>
int tests;
int p;
int f[1100][12][12];
int m[1100];
int price[1100][12];
int min(int a,int b)
{
    if (a>b) return b; 
    return a;
}
int main()
{
    freopen("blarge.in","r",stdin);
    freopen("blarge.out","w",stdout);
    scanf("%d",&tests);
    for (int t0=1;t0<=tests;t0++)
    {
        scanf("%d",&p);
        for (int i=0;i<(1<<p);i++) 
        {
            scanf("%d",&m[i]);
            if (m[i]>p) m[i]=p;
        }
        for (int j=1;j<=p;j++)
        {
            for (int i=0;i<(1<<p);i+=(1<<j))            
                scanf("%d",&price[i][j]);
        }
        for (int i=0;i<(1<<p);i++)
        {
            for (int j=0;j<=p;j++)            
               for (int k=p+1;k>=0;k--) f[i][j][k]=1000000000;
            for (int k=0;k<=m[i];k++) f[i][0][k]=0;
        }
            
        

        for (int j=1;j<=p;j++)
        for (int i=0;i<(1<<p);i++)
        {
            {
                if (i%(1<<j)==0)
                {
                    for (int k=p;k>=0;k--)
                    {
                        f[i][j][k]=min(price[i][j]+f[i][j-1][k]+f[i+(1<<j>>1)][j-1][k],f[i][j-1][k+1]+f[i+(1<<j>>1)][j-1][k+1]);                        
                        if (f[i][j][k]>1000000000) f[i][j][k]=1000000000;
                        if (k!=p&&f[i][j][k]>f[i][j][k+1]) f[i][j][k]=f[i][j][k+1];
                    }
                }

            }
        }
        printf("Case #%d: %d\n",t0,f[0][p][0]);
    }
}
