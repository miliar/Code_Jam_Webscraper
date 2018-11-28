#include<iostream>
#include<algorithm>
using namespace std;

const int mod=100003;
int ncr[501][501];
void mkncr()
{
  ncr[0][0]=1;
  for(int n=1,r;n<=500;++n)
  { ncr[n][0]=ncr[n][n]=1;
    for(r=1;r<n;++r) ncr[n][r]=(ncr[n-1][r]+ncr[n-1][r-1])%mod;
  }
}
int dp[501][501], res[501];

void precalc()
{
  int n,m,l;
  for(n=2;n<=500;++n) 
  { dp[n][1]=res[n]=1;
    for(m=2;m<n;++m)
    { dp[n][m]=0;
      for(l=1;l<m;++l) if(n-m>=m-l)
        dp[n][m]=(dp[n][m]+dp[m][l]*1LL*ncr[n-m-1][m-l-1])%mod;
      res[n]=(res[n]+dp[n][m])%mod;
    }
  }
}

int main()
{
  mkncr();
  precalc();
  int cn,ci,n;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { cin>>n;
    cout<<"Case #"<<ci<<": "<<res[n]<<endl;
  }
}
