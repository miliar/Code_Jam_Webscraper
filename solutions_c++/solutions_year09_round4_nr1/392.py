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

bool ok(int row , string& s)
{
  for(int i=row+1;i<SZ(s);i++){
    if(s[i]=='1') return false;
  }
  return true;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    vector<string> dat(n);
    FOR(i,n) cin>>dat[i];
    int ans = 0 ; 
    FOR(i,n){
      for(int j=i;j<n;j++){
        if(ok(i,dat[j])){
          //cout << " " << i << " " << j << endl;
          for(int k=j;k>i;k--){
            swap(dat[k],dat[k-1]);
            ans++;
          }
          break;
        }
        if(j==n-1) assert(1);
      }
      //FOR(i,n) cout << dat[i] << endl; cout << endl;
    }
    printf("Case #%d: %d\n" , case_no++ , ans);
  }
  return 0 ;
}
