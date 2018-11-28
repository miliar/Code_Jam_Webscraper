#include<iostream>
using namespace std;

const int mod=10007;
int rockr[10],rockc[10],rn;
int rows,cols;

bool norock(int r,int c) 
{ for(int i=0;i<rn;++i) if(rockr[i]==r&&rockc[i]==c) return false;
  return true;
}
int calc()
{
  int r,c;
  int dp[105][105]={}; dp[0][0]=1;
  for(r=0;r<rows;++r) for(c=0;c<cols;++c) 
  { int nr,nc;
    nr=r+1; nc=c+2;
    if(norock(nr,nc)) dp[nr][nc]=(dp[nr][nc]+dp[r][c])%mod;
    if(norock(r+2,c+1)) dp[r+2][c+1]=(dp[r+2][c+1]+dp[r][c])%mod;
  }
  return dp[rows-1][cols-1];
}
int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { cin>>rows>>cols>>rn;
    for(int i=0;i<rn;++i) 
    { cin>>rockr[i]>>rockc[i];
      rockr[i]--; rockc[i]--;
    }
    cout<<"Case #"<<ci<<": "<<calc()<<endl;
  }
}
