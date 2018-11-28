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
#include<bitset>

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

ll_t dfs(VVI& price , VI& miss , int n , int p , int sp , int ep , int rpos = 0 , int cpos=0)
{
  if(sp+2==ep) {
    if(miss[sp] > 0 && miss[sp+1] > 0) return 0;
    return price[rpos][cpos] ; 
  }
  ll_t ret = 0 ;   
  int sz = (ep - sp) / 2;
  {
    ll_t v1=1LL<<60,v2=1LL<<60;
    
    v1 = dfs(price , miss , n , p , sp , sp + sz , rpos + 1 , 2*cpos);
    v2 = dfs(price , miss , n , p , sp + sz , ep , rpos + 1 , 2*cpos+1);
    ret = v1 + v2 + price[rpos][cpos]; 
  }
  
  bool ng = false;
  FOR3(i,sp,ep) {
    miss[i]--; 
    if(miss[i]<0) ng = true;
  }
  if(ng==false){
    ll_t v1=1LL<<60,v2=1LL<<60;
    v1 = dfs(price , miss , n , p , sp , sp + sz , rpos + 1 , 2*cpos);
    v2 = dfs(price , miss , n , p , sp + sz , ep , rpos + 1 , 2*cpos+1);
    ret = min(ret,v1 + v2);
  }
  FOR3(i,sp,ep) {
    miss[i]++;
  }
  return ret;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    ll_t ans = 0 ;
    int p ; 
    cin>>p;
    int team = 1<<p;
    VI miss = VI(team);
    FOR(i,team){
      cin>>miss[i] ; 
    }
    VVI price(p);
    for(int i=p-1;i>=0;i--){
      int m = (1<<i);
      VI list(m);
      FOR(j,m){
        int price; 
        cin>>price;
        list[j] = price;
      }
      price[i] = list;
    }
    ans = dfs(price , miss , team , p , 0 , team ) ; 
    printf("Case #%d: %lld\n" , case_no++ , ans);
  }
  return 0 ;
}
