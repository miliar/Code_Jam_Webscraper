#include<iostream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>

using namespace std;

#define BET(a,i,b) (((a)<=(i))&&((i)<(b)))
#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;
ll_t mod = 10007;
int dx[] = {2,1};
int dy[] = {1,2};
bool block[110][110];
ll_t dp[110][110];
void solve()
{
  int H,W,R;
  cin>>H>>W>>R;
  ll_t ans = 0;
  memset(block , 0 , sizeof(block));
  memset(dp , 0 , sizeof(dp));
  FOR(i,R){
    int r,c;
    cin>>r>>c;
    r--; c--;
    block[r][c]=true;
  }
  dp[0][0]=block[0][0]?0:1;
  FOR(i,H) {
    FOR(j,W){
      if(block[i][j]) continue;
      FOR(k,2){
        int nr = i - dy[k];
        int nc = j - dx[k];
        if(0<=nr && 0<=nc){
          dp[i][j] += dp[nr][nc];
          dp[i][j] %= mod;
        }
      }
      //cout << " " << dp[i][j] ;
    }
    //cout << endl;
  }
  ans = dp[H-1][W-1];
  cout << ans << endl;
}

int main()
{
  int t; 
  cin>>t;
  FOR(case_no,t)
    {
      printf("Case #%d: " , case_no + 1 );
      solve();
    }
  return 0 ;
}
