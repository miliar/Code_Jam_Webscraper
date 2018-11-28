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
    int ans = 0 ;
    int n;
    cin>>n;
    int orange = 0 , blue = 0 ;
    int orange_pos = 1 , blue_pos = 1;
    FOR(i,n){
      char c; int pos;
      cin>>c>>pos;
      if(c=='O') {
        int time = abs(orange_pos - pos) + 1;
        orange_pos = pos;
        orange += time;
        orange = max(orange , blue + 1);
      }else{
        int time = abs(blue_pos - pos) + 1;
        blue_pos = pos;
        blue += time;
        blue = max(blue , orange + 1);
      }
    }
    ans = max(orange , blue);
    printf("Case #%d: %d\n" , case_no++ , ans);
  }
  return 0 ;
}
