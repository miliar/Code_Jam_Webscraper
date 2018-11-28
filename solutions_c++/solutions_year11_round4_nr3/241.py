#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

long long pri[2000000];
bool f[2000000];
long long n;


    
int main()
{
    freopen("c2.in","r",stdin);
    freopen("c2.out","w",stdout);
    memset(f,1,sizeof(f));
    int tot=0;
    for (int i=2;i<=1000000;i++)
        if (f[i])
        {
           // cout<<i<<endl;
            pri[++tot]=i;
            for (int j=i+i;j<=1000000;j+=i) f[j]=0;
        }
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%I64d",&n);
        int ans=0;
        for (int i=1;i<=tot;i++)
            if (pri[i]*pri[i]<=n)
            {
                  for (long long t=pri[i];t<=n;t*=pri[i]) ans++;
                  ans-=1;
            }
            else break;
       if (n==1) ans=-1;
       printf("Case #%d: %d\n",cas,ans+1);
    }
    return 0;
}
