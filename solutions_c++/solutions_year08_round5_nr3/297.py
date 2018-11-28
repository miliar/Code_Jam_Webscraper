#include<stdio.h>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
using namespace std;

const int N=11;
const int M=(1<<11);

int f[N][M],n,m,a[N],bn,v[M];
char ch[N][N];

int count(int k)
{
    int i=0;
    while (k>0)
    {
          i+=k%2;
          k/=2;
    }
    return i;
}
bool yes(int p,int q)
{
     int i,j,k;
     for (i=0;i<m;i++)
     if (((1<<i)&p)==(1<<i))
     {
         if (i>0)
         {
            j=(1<<(i-1));
            if ((q&j)>0) return 0;
         }
         if (i<m-1)
         {
            j=(1<<(i+1));
            if ((q&j)>0) return 0;
         }
     }
     return 1;
 }
int main()
{
    int test,ncase=1,i,j,k,ans,s,t;
    freopen("Csmall.in","r",stdin);
    freopen("Csmall.out","w",stdout);
    scanf("%d",&test);
    while (ncase<=test)
    {
          scanf("%d%d",&n,&m);
          memset(a,0,sizeof(a));
          for (i=0;i<n;i++)
          {
              scanf("%s",ch[i]);
              for (j=0;j<m;j++)
              if (ch[i][j]=='x') a[i]+=(1<<j);
          }
          bn=(1<<m);
          memset(v,0,sizeof(v));
          for (i=0;i<bn;i++)
          {
              for (j=0;j<m-1;j++)
              if (((1<<j)&i)==(1<<j) && ((1<<(j+1))&i)==(1<<(j+1)))
               break;
              if (j>=m-1) v[i]=1;
          }
//          for (i=0;i<vn;i++) printf("v[%d]=%d\n",i,v[i]);
          memset(f,0,sizeof(f));
          ans=0;
          for (i=0;i<bn;i++)
          if (v[i] && (i&a[0])==0) f[0][i]=count(i);
          for (i=0;i<bn;i++)
          if (f[0][i]>ans) ans=f[0][i];
          for (i=1;i<n;i++)
          {
              for (j=0;j<bn;j++)
              if (v[j] && (j&a[i])==0)
              {
               for (k=0;k<bn;k++)
               if (v[k] && (k&a[i-1])==0 && yes(j,k))
               {
                  s=f[i-1][k]+count(j);
                  if (s>f[i][j]) f[i][j]=s;
               }
//               printf("f[%d][%d]=%d\n",i,v[j],f[i][v[j]]);
               if (i==n-1 && f[i][j]>ans) ans=f[i][j];
              }
          }
          printf("Case #%d: %d\n",ncase++,ans);
    }
    return 0;
}
