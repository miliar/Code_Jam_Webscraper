// compile with "g++ XXX.cc -mno-cygwin -O2" in Cygwin

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
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
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;

const double PI = 4.0*atan(1.0);

double memo[50][50][50];

ll_t memo_comb[50][50];

ll_t comb(int s , int t){
  if(s < t) return 0 ;
  if(t==0 || s==t) return 1;
  ll_t& ret = memo_comb[s][t];
  if(ret != -1) return ret;
  return ret = comb(s-1 , t) + comb(s-1 , t - 1);
}

double dfs(int C , int N , int rem) // rem / C -> N
{
  if(rem==0) return 0.0;
  double &ret = memo[C][N][rem];
  if(!isnan(ret)) return ret;
  double val = 0;
  ll_t all = 0;
  ll_t p0 = 0;
  for(int i=0;i<=min(N,rem);i++){
    ll_t pattern = comb(rem , i) * comb(C-rem , N-i);
    all += pattern;
    if(i==0){
      p0 = pattern;
    }else{
      val += (dfs(C , N , rem-i)+1) * pattern; 
    }
    // N in  (rem / C)
  }
  assert(all == comb(C, N));
  // dfs(rem) = (val + (dfs(rem)+1)*p) / (all))
  // X = (val+(X+1)*p) / all;
  // all * X = val + X*p + p
  // (all-p) * X = val+ p
  // X = (val+p) / (all-p);
  val = (val+p0) / (all-p0);
  return ret = val ;
}

int main() {
  int t,case_no=1;
  cin>>t;
  memset(memo , -1 , sizeof(memo));
  memset(memo_comb , -1 , sizeof(memo_comb));
  while(t--){
    double ans = 0;
    int C,N;
    cin>>C>>N;
    ans = dfs(C,N,C);
    printf("Case #%d: %.7f\n" , case_no++ , ans);
  }
  return 0 ;
}
