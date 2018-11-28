#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
using namespace std;

const double eps = 1e-10;

inline double min(double a,double b){return a<b?a:b;}
inline double max(double a,double b){return a>b?a:b;}
const long N =105,M=1005;
const long INF= 1<<28;
long n,m,q;
long ct[N],dp[M][N];
long K = 1;
inline void swap(double &a,double &b){double tt;tt=a,a=b,b=tt;}
char ss[N][M],qs[M][M];
void Init()
{
    scanf("%ld\n",&n);
    long i;
    for(i=0;i<n;i++)
    {
       // printf("%ld : \n",i);
        gets(ss[i]);
    }
    scanf("%ld\n",&q);
    for(i=1;i<=q;i++)
        gets(qs[i]);
}
void Solve()
{
    long i,j,k;
    long ans,qt;
    ans =INF;
    for(i=0;i<=q;i++)for(j=0;j<=n;j++)dp[i][j]=INF;
    for(i=0;i<n;i++)dp[0][i]=0;
    for(i=0;i<q;i++)
    {
        for(j=0;j<n;j++)
        {
            if(strcmp(qs[i+1],ss[j])==0)
            {
                for(k=0;k<n;k++)
                {
                    if(j!=k)dp[i+1][k]<?=dp[i][j]+1;
                  //  printf("a %ld : %ld %ld- %ld\n",i,j,k,dp[i+1][k]);
                }
            }
            else
            {
                for(k=0;k<n;k++)
                {
                    if(j!=k)dp[i+1][k]<?=dp[i][j]+1;
                    else dp[i+1][k]<?=dp[i][j];
                  //  printf("b %ld : %ld %ld- %ld\n",i,j,k,dp[i+1][k]);
                }
            }
        }
    }
    for(i=0;i<n;i++)ans<?=dp[q][i];
    printf("Case #%ld: ",K++);
    printf("%ld\n",ans);
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long T;scanf("%ld",&T);

    while(T--)
    {
        Init();
        Solve();
    }
    return 0;
}
