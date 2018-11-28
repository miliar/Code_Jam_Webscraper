#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
const int maxn=500+10;
const int m=19;
const int mod=10000;
const string s0="welcome to code jam";
int n,ans,f[maxn][m];
char s[maxn];
void solve()
{
    gets(s);
    n=strlen(s);
    memset(f,0,sizeof(f));
    if (s[0]==s0[0])
        f[0][0]=1;
    for (int i=1;i<n;i++)
        if (s[i]==s0[0])
            f[i][0]=f[i-1][0]+1;
        else
            f[i][0]=f[i-1][0];
    for (int i=1;i<n;i++)
        for (int j=1;j<m;j++)
            if (s[i]==s0[j])
                f[i][j]=(f[i-1][j]+f[i-1][j-1])%mod;
            else
                f[i][j]=f[i-1][j];
    ans=f[n-1][m-1];
}
void out(int test)
{
    printf("Case #%d: ",test);
    if (ans<1000)
        printf("0");
    if (ans<100)
        printf("0");
    if (ans<10)
        printf("0");
    printf("%d\n",ans);
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int t;
    scanf("%d",&t);
    gets(s);
    for (int i=1;i<=t;i++)
    {
        solve();
        out(i);
    }
    return 0;
}
