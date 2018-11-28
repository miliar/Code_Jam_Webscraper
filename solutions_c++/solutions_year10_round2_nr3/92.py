#include<iostream>
#include<algorithm>
using namespace std;
const int maxn=500+10;
const long long mod=100003;
int n;
long long f[maxn][maxn],c[maxn][maxn],s[maxn];
void prepare()
{
    memset(c,0,sizeof(c));
    c[0][0]=c[1][0]=c[1][1]=1;
    for (int i=2;i<maxn;i++)
    {
        c[i][0]=1;
        for (int j=1;j<=i;j++)
            c[i][j]=(c[i-1][j]+c[i-1][j-1])%mod;
    }
    memset(f,0,sizeof(f));
    for (int i=2;i<maxn;i++)
    {
        f[i][1]=1;
        for (int j=2;j<i;j++)
        {
            f[i][j]=0;
            for (int k=1;k<j;k++)
                f[i][j]=(f[i][j]+f[j][k]*c[i-j-1][j-k-1])%mod;
        }
    }
    for (int i=2;i<maxn;i++)
    {
        s[i]=0;
        for (int j=1;j<i;j++)
            s[i]+=f[i][j];
        s[i]%=mod;
    }
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    prepare();
    int t;
    cin >>t;
    for (int i=1;i<=t;i++)
    {
        cin >>n;
        cout <<"Case #"<<i<<": "<<s[n]<<endl;
    }
    return 0;
}
