#include <stdio.h>
#include <memory.h>
int ans;
long long f[510][510],c[510][510];
int n0,t0;
const int m0=100003;

int main()
{
    freopen("c2.in","r",stdin);
    freopen("c2.out","w",stdout);
    scanf("%d",&t0);
        memset(c,0,sizeof(c));
        memset(f,0,sizeof(f));
        for (int i=0;i<=500;i++)
          for (int j=0;j<=i;j++)
          {
                if (j==0||j==i) c[i][j]=1;
                else c[i][j]=c[i-1][j-1]+c[i-1][j];
          }
          
        f[1][1]=1;
        for (int n=2;n<=500;n++)
        {
            f[n][1]=1; 
            for (int k=2;k<n;k++)
            {
                for (int j=1;j<k;j++)
                  f[n][k]=(f[n][k]+f[k][j]*c[n-k-1][k-j-1])%m0;
            }           
        }
        
    for (int t1=1;t1<=t0;t1++)
    {
        scanf("%d",&n0);
        ans=0;
        for (int i=1;i<=n0;i++) ans+=f[n0][i];
        printf("Case #%d: %d\n",t1,ans%m0);
    }
}
