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

int solve(int e){
  if(e == 1) return 0;
  return e ; 
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    double ans = 0 ;
    int n;
    cin>>n;
    VI dat(n);
    FOR(i,n) cin>>dat[i];    
    FOR(i,n) dat[i]--;
    FOR(i,n){
      int p = i ;
      int e = 1;
      while(dat[p] != p){
        int np = dat[p];
        swap(dat[p],dat[np]);
        e++;
      }
      ans += solve(e);
    }

    printf("Case #%d: %.10f\n" , case_no++ , (double)ans);
  }
  return 0 ;
}
