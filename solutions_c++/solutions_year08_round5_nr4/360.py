#include<stdio.h>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
using namespace std;

const int N=110;
const int P=10007;

int ans,f[N][N],n,m,L,a[N][N];
int main()
{
    int test,ncase=1,i,j,k,s;
    freopen("Asmall.in","r",stdin);
    freopen("Asmall.out","w",stdout);
    scanf("%d",&test);
    while (ncase<=test)
    {
       memset(f,0,sizeof(f));
       memset(a,0,sizeof(a));
       scanf("%d%d%d",&n,&m,&L);
       for (i=0;i<L;i++)
       {
           scanf("%d%d",&j,&k);
           a[j][k]=1;
       }
       f[1][1]=1;
       for (i=2;i<=n;i++)
        for (j=2;j<=m;j++)
        if (a[i][j]==0)
        {
           f[i][j]=f[i-2][j-1]+f[i-1][j-2];
           f[i][j]%=P;
        }
       printf("Case #%d: %d\n",ncase++,f[n][m]);
    }
    return 0;
}
