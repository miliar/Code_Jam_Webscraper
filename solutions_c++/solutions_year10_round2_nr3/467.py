#include<iostream>
using namespace std;
#define mod 100003
long long combine[600][600],f[600][600],ans[600];
int ss,n,tc;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    combine[0][0]=1;
    for (int i=1;i<=500;++i)
    {
        combine[i][0]=1;
        for (int j=1;j<=i;++j)
            combine[i][j]=(combine[i-1][j-1]+combine[i-1][j]) % mod;
    }
    f[2][1] = 1;
    ans[2]=1;
    for (int i=3;i<=500;++i)
    {
        f[i][1]=1;
        ans[i] = 1;
        for (int j=2;j<=i-1;++j)
        {
            f[i][j]=f[j][j-1];
            ss = 1;
            for (int k=j-2;k>=1;--k)
            {
                f[i][j] = (f[i][j] + f[j][k] * combine[i-j-1][ss]) % mod;
                ss++;
            }
            ans[i] =(ans[i]+f[i][j])%mod;
        }
    }
    cin>>tc;
    for (int t=1;t<=tc;++t)
    {
        cin>>n;
        printf("Case #%d: %I64d\n",t,ans[n]);
    }
    return 0;
}

