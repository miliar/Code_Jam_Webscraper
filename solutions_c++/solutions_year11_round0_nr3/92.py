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


int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int ans ;
    int N;
    cin>>N;
    VI dat(N);
    int b = 0 ;
    long long sum = 0 ;
    FOR(i,N){
      cin>>dat[i];
      b ^= dat[i];
      sum += dat[i];
    }
    sort(ALL(dat));
    printf("Case #%d: " , case_no++);
    if(b==0){
      printf("%lld\n" , sum-dat[0]);
    }else{
      printf("NO\n");
    }
  }
  return 0 ;
}
