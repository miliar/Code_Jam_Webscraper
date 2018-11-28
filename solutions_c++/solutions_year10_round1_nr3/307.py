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
#define FOR3(i,a,b) for(int i=a,i##_end=b;i<i##_end;i++)
#define FOR_EACH(it,v) for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;

template<typename T> void debug(T v , string delimiter = "\n")
{ for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++) cout << *it << delimiter; cout << flush ;}

int dx[]  = {0,1,0,-1};
int dy[]  = {1,0,-1,0};
string ds = "SENW";

const double PI = 4.0*atan(1.0);

long long gcd (long long s , long long t) { return t ? gcd(t,s%t) : s ; }

bool ok(ll_t a , ll_t b){
  VI step ;
  while(a>0 && b>0){
    if(a > b) swap(a,b);
    int sub = b / a ; 
    b -= sub * a ; 
    step.push_back(sub);
  }
  bool a_turn = true;
  FOR(i,SZ(step)){
    if(step[i]>=2){
      return a_turn;
    }else{
      a_turn = !a_turn;
    }
  }
  return a_turn;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int ans = 0 ;
    int A1,A2,B1,B2;
    cin>>A1>>A2>>B1>>B2;
    FOR3(a,A1,A2+1) FOR3(b,B1,B2+1){
      if(ok(a,b)) ans++;
    }
    printf("Case #%d: %d\n" , case_no++ , ans);
  }
  return 0 ;
}
