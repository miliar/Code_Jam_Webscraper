#include<iostream>
using namespace std;
int C[510][510];
void Initial()
{
     memset(C,0,sizeof(C));
     for (int i=0;i<510;++i) C[i][0]=1;
     C[1][0]=C[1][1]=1;
     for (int i=2;i<510;++i)
     {
         C[i][0]=1;
         for (int j=1;j<=i;++j)
         C[i][j]=(C[i-1][j-1]+C[i-1][j]) % 100003;
     }
}
int f[510][510];
long long Calc(int n,int m)
{
     if (n<0 || m<0) return 0;
     if (m>n) return 0;
     return C[n][m];
}
int Work()
{
    memset(f,0,sizeof(f));
    f[2][1]=1;
    for (int n=3;n<=500;++n)
    {
        f[n][1]=1;
     for (int k=2;k<n;++k)
     {
        f[n][k]=0;
        for (int t=max(1,2*k-n);t<=k-1;++t)
        {
            long long tmp=f[k][t];
            tmp*=Calc(n-k-1,k-t-1);
            f[n][k]=(f[n][k] + tmp % 100003) % 100003 ;
        }
     }
    }
}
int Solve()
{
    int x;
    scanf("%d",&x);
    int Ans=0;
    for (int i=0;i<x;++i)
    Ans=(Ans+f[x][i]) % 100003;
    return Ans;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large-Ans.txt","w",stdout);
    Initial();
    Work();
    int Cases;
    scanf("%d",&Cases);
    for (int i=1;i<=Cases;++i)
    printf("Case #%d: %d\n",i,Solve());
    return 0;
}
