#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std;
const long N = 1000,INF=1e16,D=1e11;
const double eps = 1e-10;
inline long max(long a,long b){return a>b?a:b;}
inline long min(long a,long b){return a<b?a:b;}
inline void swap(__int64 &a,__int64 &b){__int64 tt;tt=a,a=b,b=tt;}
long n,m;
__int64 a[N],b[N];
__int64 w[N][N];
__int64 x[N],y[N],lx[N],ly[N],match[N];
bool dfs(__int64 v)
{
 lx[v]=1;
 __int64 i,j,k;
 for(i=0;i<n;i++)
 {
  if(ly[i])continue;
  if(w[v][i]==x[v]+y[i])
  {
   ly[i]=1;
   if(match[i]==-1||dfs(match[i]))
   {
    match[i]=v;
    return 1;
   }
  }
 }
 return 0;
}

__int64 KM()
{
    __int64 i,j,k,d;
    for(i=0;i<n;i++)
    {
        x[i]=y[i]=0;match[i]=-1;
        for(j=0;j<n;j++)
        {
            x[i]>?=w[i][j];
        }
    }
    for(i=0;i<n;i++)
    {
//  printf("I: %ld\n",i);
        while(1)
        {
            for(j=0;j<n;j++)lx[j]=ly[j]=0;
            if(dfs(i))break;
            d=INF;
            for(k=0;k<n;k++)
            {
                if(lx[k])
                {
                    for(j=0;j<n;j++)
                    {
                        if(!ly[j])
                        {
                            d<?=x[k]+y[j]-w[k][j];
                        }
                    }
                }
            }

            for(k=0;k<n;k++)
            {
                if(lx[k])x[k]-=d;
                if(ly[k])y[k]+=d;
            }
            }
        }
    __int64 ans = 0;
    for(i=0;i<n;i++)
        ans+=-(w[match[i]][i]-D);
    return ans;

}

void Init()
{
    __int64 i,j,k;
    scanf("%ld",&n);
    for(i=0;i<n;i++)
    {
        scanf("%I64d",a+i);
       // printf("%I64d\n",a[i]);
    }
    sort(a,a+n);
    for(i=0;i<n;i++)
        scanf("%I64d",b+i);
    sort(b,b+n);
    for(i=0;i<n/2;i++)swap(b[i],b[n-i-1]);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            w[i][j]=a[i]*b[j];
          //  printf("%I64d ",w[i][j]);
            w[i][j]=-w[i][j]+D;
        }
       // printf("\n");
    }
    //printf("%I64d\n",D);
   // printf("%I64d\n",KM());
   __int64 ans = 0;
   for(i=0;i<n;i++)ans+=a[i]*b[i];
   printf("%I64d\n",ans);

}

void Solve()
{
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long T,K=1;scanf("%ld",&T);
    while(T--)
    {
        printf("Case #%ld: ",K++);
        Init();
        Solve();
    }
    return 0;
}
