// compile with "g++ XXX.cc -O2" in Cygwin (gcc version 4.5.3 (GCC))

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
#include<bitset>
#include<cassert>

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

int n;
ll_t D[20000];
ll_t L[20000];
ll_t endD;

bool solve()
{
  vector<ll_t> maxL(n,-1);
  if(L[0] < D[0]) return false;
  maxL[0] = D[0];
  //queue<pair<int,int> > 
  FOR(i,n) {
    ll_t len = maxL[i];
    if(len == -1) continue;
    ll_t reach = D[i] + len;
    //cout<<i<<" "<<D[i]<<" "<<len<<" "<<endD<<endl;
    if(reach >= endD) return true;
    for(int j=i+1;j<n;j++){
      if(D[j] <= reach && D[j] - D[i] <= L[i] + L[j]){
        maxL[j] = max(maxL[j] , min(D[j] - D[i] , L[j]));
      }
    }
  }
  return false;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    cin>>n;
    FOR(i,n){
      cin>>D[i]>>L[i];
    }
    cin>>endD;
    
    printf("Case #%d: %s\n" , case_no++ , solve()?"YES":"NO");
    
    
  }
  return 0 ;
}
