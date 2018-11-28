#include <cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int N=105;
int f[N][N];

int t[N];
int n,s,p;

int sm[N];
int dp(int nn,int ss)
{
     int i,j,x,m;
     if(f[nn][ss]!=-1) return f[nn][ss];
     if(nn==0) return f[nn][ss]=0;
     int mx=0;
     x=t[nn]%3;
     if(x==0) m=t[nn]/3;
     if(x==1) m=(t[nn]+2)/3;
     if(x==2) m=(t[nn]+1)/3;
     if(sm[nn-1]>=ss) mx=max(mx,dp(nn-1,ss)+(m>=p?1:0));
     if(t[nn]>=2&&t[nn]<=28&&ss>0)
     {
      if(x==0) m=(t[nn]+3)/3;
     if(x==1) m=(t[nn]+2)/3;
     if(x==2) m=(t[nn]+4)/3;
      mx=max(mx,dp(nn-1,ss-1)+(m>=p?1:0));
     }
     return f[nn][ss]=mx;
}






int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k;
    int T;
    scanf("%d",&T);
    for(k=1;k<=T;k++)
    {
        scanf("%d%d%d",&n,&s,&p);
        memset(sm,0,sizeof(sm));
        for(j=1;j<=n;j++)
        {
            scanf("%d",&t[j]);
            sm[j]=sm[j-1];
            if(t[j]>=2&&t[j]<=28) sm[j]++;
        }

    memset(f,-1,sizeof(f));
     printf("Case #%d: %d\n",k,dp(n,s));
    }
    return 0;
}





