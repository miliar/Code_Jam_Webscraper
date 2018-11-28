#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<functional>
#define maxn 110
using namespace std;

int cas,ncas,n,h,w,c,a[maxn][maxn],i,j,k,l;

int main()
{
    scanf("%d",&ncas);
    for (cas = 1; cas <= ncas; cas++)
    {
        printf("Case #%d: ",cas);
        scanf("%d%d%d",&h,&w,&c);
        memset(a,0,sizeof(a));
        for (i=0;i<c;i++)
        {
            scanf("%d%d",&j,&k);
            a[j][k]=-1;
        }
        a[1][1]=1;
        for (i=1;i<=h;i++)
          for (j=1;j<=w;j++) if (a[i][j]!=-1)
          {
              for (k=i-5;k<=i;k++) if (k>0 && k<=h)
                for (l=j-5;l<=j;l++) if (l>0 && l<=w)
                if ((i-k)*(i-k) + (j-l)*(j-l) == 5  && a[k][l]!=-1) 
                   a[i][j]=(a[i][j]+a[k][l])%10007;
          }
        printf("%d\n",a[h][w]%10007);
    }
    return 0;
}
