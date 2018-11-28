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

int dx[]  = {0,1,1,1};
int dy[]  = {1,1,0,-1};
string ds = "SENW";

const double PI = 4.0*atan(1.0);

vector<string> rot_drop(vector<string> dat)
{
  vector<string> ret(dat);
  int n = SZ(dat);
  FOR(i,n){
    string s = dat[i];
    int cnt = SZ(s) ;
    s.erase(remove(ALL(s),'.'),s.end()) ; 
    cnt -= SZ(s);
    s = string(cnt , '.') + s;
    dat[i] = s;
  }
  FOR(i,n) FOR(j,n){
    ret[j][n-1-i] = dat[i][j];
  }  
  
  return ret;
}

bool check(vector<string> dat , char c , int kk){
  int n = SZ(dat);
  FOR(i,n) FOR(j,n){
    if(dat[i][j]!=c) continue;
    FOR(k,4){
      int py = i ; 
      int px = j ;
      int step = 0 ; 
      while(BET(0,px,n) && BET(0,py,n) && dat[py][px]==c){
        step++;
        px += dx[k];
        py += dy[k];
      }
      if(step >= kk) return true;
    }
  }
  return false;
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    int n,k;
    cin>>n>>k;
    vector<string> dat(n);
    FOR(i,n) cin>>dat[i];
    
    dat = rot_drop(dat);
    //FOR(i,n) cout << dat[i] << endl;
    string ans ;
    bool red = check(dat , 'R' , k);
    bool blue = check(dat , 'B' , k);
    if(red && blue) ans = "Both";
    else if(red) ans = "Red";
    else if(blue) ans = "Blue";
    else ans = "Neither";
    printf("Case #%d: %s\n" , case_no++ , ans.c_str());
  }
  return 0 ;
}
