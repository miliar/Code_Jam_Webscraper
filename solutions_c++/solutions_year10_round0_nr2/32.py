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

long long gcd (long long s , long long t) { return t ? gcd(t,s%t) : s ; }

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    vector<ll_t> dat(n);
    FOR(i,n) cin>>dat[i];
    sort(ALL(dat));
    ll_t g = 0;
    FOR(i,SZ(dat)-1){
      g = gcd(g , dat[i+1]-dat[i]);
    }
    if(g==0) g = 1;
    ll_t ans = 0 ;
    ans = (g - dat[0] % g) % g ;
    printf("Case #%d: %lld\n" , case_no++ , ans);
  }
  return 0 ;
}
