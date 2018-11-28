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

int X[100],Y[100],R[100];

double solve(int p1 , int p2){
  double dx=X[p1]-X[p2];
  double dy=Y[p1]-Y[p2];
  double dis = sqrt(dx*dx+dy*dy);
  return (dis + R[p1] + R[p2])/2.0;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    double ans = 1e100 ;
    int N ; 
    cin>>N;
    FOR(i,N){
      cin>>X[i]>>Y[i]>>R[i];
    }
    if(N==1){
      ans = R[0];
    }else if(N==2){
      ans = max(R[0],R[1]);
    }else if(N==3){
      ans = 1<<28;
      ans = min(ans , max(0.0+R[0] , solve(1,2)));
      ans = min(ans , max(0.0+R[1] , solve(2,0)));
      ans = min(ans , max(0.0+R[2] , solve(0,1)));
    }else assert(N<=3);
    printf("Case #%d: %.6f\n" , case_no++ , ans);
  }
  return 0 ;
}
