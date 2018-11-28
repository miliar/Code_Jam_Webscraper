#include<iostream>
using namespace std;
const int maxn=75;
const int maxr=2500;
int cnt[maxn][maxn][maxr],a[maxn],dp[maxn][maxn][maxn][2],c[maxn][maxn];
int cases,b,tot,ans,tt;
long long n;
int mod=1000000007;
void add(int &x,int y)
{
     x+=y;
     if (x>=mod) x-=mod;
}

void prepare()
{
     memset(cnt,0,sizeof(cnt));
     cnt[0][0][0]=1;
     int i,j,k;
     for (i=0;i<=70;i++)
     {
         c[i][0]=1;
         for (j=1;j<=i;j++)
         c[i][j]=1LL*c[i][j-1]*(i+1-j)%mod;
     }
     for (i=0;i<70;i++)
         for  (j=0;j<=i+1;j++)
              for (k=0;k<maxr;k++)
              if (cnt[i][j][k]>0)
              {
                 add(cnt[i+1][j+1][k+i+1],cnt[i][j][k]);
                 add(cnt[i+1][j][k],cnt[i][j][k]);
              }
}

void init()
{
     scanf("%lld%d",&n,&b);
     tot=0;
     while (n>0)
     {
           a[tot]=n%b;
           n/=b;
           tot++;
     }     
}

void work()
{
     ans=0;
     int i,j,k,l,i1,j1,r,tmp,t,t1;
     memset(dp,0,sizeof(dp));
     dp[0][0][0][0]=1;
     for (i=0;i<tot;i++)
         for (j=0;j<=b/2+1;j++)
             for (k=0;k<=b+1;k++)
                 for (l=0;l<2;l++)
                 if (dp[i][j][k][l]>0)
                    for (i1=0;i1<=b/2+1;i1++)
                    {
                        tmp=i1*b+a[i]-j;
                        if (l==1) j1=1;
                        else j1=0;
                        if (i==0) r=b+1;
                        else r=k;
                        for (;j1<=r;j1++)
                        {
                            if (i==0) t=1;
                            else
                            if (l) t=1LL*j1*c[k-1][j1-1]%mod;
                            else t=c[k][j1];
                            t=1LL*t*dp[i][j][k][l]%mod;
                            t1=1LL*t*cnt[b-1][j1][tmp]%mod;
                            add(dp[i+1][i1][j1][0],t1);
                            t1=1LL*t*cnt[b-1][j1-1][tmp]%mod;
                            add(dp[i+1][i1][j1][1],t1);
                        }
                    }
     for (i=0;i<=b+1;i++)
     add(ans,dp[tot][0][i][0]);
}

void print()
{
     tt++;
     printf("Case #%d: %d\n",tt,ans);
}

int main()
{
    prepare();
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    tt=0;
    for (scanf("%d",&cases);cases;cases--)
    {
        init();
        work();
        print();
    }
    return 0;
}
