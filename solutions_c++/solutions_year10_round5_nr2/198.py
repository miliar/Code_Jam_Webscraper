#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

const int imax=1000000000;
typedef long long lli;
int dp[10001];

void mkdp(const vector<int>& board)
{
  int len,i,n=board.size();
  for(i=1;i<=10000;++i) dp[i]=imax;
  dp[0]=0;
  for(i=0;i<n;++i)
    for(len=board[i];len<=10000;++len)
      if(dp[len]>dp[len-board[i]]+1) dp[len]=dp[len-board[i]]+1;
}

lli calc(lli exact,const vector<int>& board)
{
  int last,mx=*max_element(board.begin(),board.end());
  lli lmax = (1LL<<61);
  lli rv=lmax;
  mkdp(board);
  for(last=0;last<=10000&&last<=exact;++last) 
    if(dp[last]<imax&&(exact-last)%mx==0)
  { lli m=(exact-last)/mx+dp[last];
    if(rv>m) rv=m;
  }
  return rv>=lmax?-1:rv;
}

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { int i,n;
    lli exact;
    cin>>exact>>n;
    vector<int> board(n,0);
    for(i=0;i<n;++i) cin>>board[i];
    cout<<"Case #"<<ci<<": ";
    lli res = calc(exact,board);
    if(res<0) cout<<"IMPOSSIBLE"<<endl;
    else cout<<res<<endl;
  }
}
