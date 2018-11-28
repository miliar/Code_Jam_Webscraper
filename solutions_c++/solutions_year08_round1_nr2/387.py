#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

const int N=101;
const int M=1<<11;

int f[N][M],n,m,ans;
vector<int> a[N];

int cnt(int k)
{
    int i=0;
    while (k>0)
    {
         i+=k%2;
         k/=2;
    }
    return i;
}
void dfs()
{
     int i,j,t,st;
     
     vector<int>::iterator it;
     for (st=0;st<(1<<m);st++)
     {
         for (i=0;i<n;i++)
         {
           for (it=a[i].begin();it!=a[i].end();it++)
           {
              j=*it;
              t=j/m;j=j%m;
              if ((st&(1<<j))==(t<<j)) break;
           }
           if (it==a[i].end()) break;
         }
         if (i<n) continue;
         if (ans<0) ans=st;
         else
         if (cnt(st)<cnt(ans)) ans=st;
     }
}
int main()
{
    int t=1,test,i,j,T,k;
    freopen("Bsmall.in.txt","r",stdin);
    freopen("Bsmall.out","w",stdout);
    scanf("%d",&test);
    while (t<=test)
    {
          scanf("%d%d",&m,&n);
          for (i=0;i<N;i++) a[i].clear();
          for (i=0;i<n;i++)
          {
              scanf("%d",&T);
              while (T--)
              {
                    scanf("%d%d",&j,&k);
                    a[i].push_back(m*k+j-1);
              }
          }
          ans=-1;
          dfs();
          printf("Case #%d:",t++);
          if (ans<0) printf(" IMPOSSIBLE");
          else 
          for (i=0;i<m;i++)
          if ((ans&(1<<i))==(1<<i)) printf(" 1");
          else printf(" 0");
          printf("\n");
    }
}
