#include<iostream>
#include<string>
using namespace std;

const string wel="welcome to code jam";
const int weln=wel.size();
const int mod=10000;

int calc(const string& s)
{
  int i,j,n=s.size();
  int dp[20][501];
  for(i=1;i<=weln;++i) dp[i][0]=0;
  for(j=0;j<=n;++j) dp[0][j]=1;
  for(i=1;i<=weln;++i) for(j=1;j<=n;++j)
  { dp[i][j]=dp[i][j-1];
    if(wel[i-1]==s[j-1]) dp[i][j]=(dp[i][j]+dp[i-1][j-1])%mod;
  }
  return dp[weln][n];
}

int main()
{
  int ci,cn;
  string s;
  cin>>cn; cin.ignore();
  for(ci=1;ci<=cn;++ci)
  { getline(cin,s);
    cout<<"Case #"<<ci<<": ";
    cout.width(4); cout.fill('0');
    cout<<calc(s)<<endl;
  }

}
