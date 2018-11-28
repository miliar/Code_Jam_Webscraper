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

char combine[255][255];
bool oppose[255][255];

string reform(vector<char> list){
  string ret = "[";
  FOR(i,SZ(list)){
    if(i>0) ret += ", " ; 
    ret += list[i];
  }
  return ret + "]";
}

int main() {
  int t,case_no=1;
  cin>>t;
  while(t--){
    memset(combine , 0 , sizeof(combine));
    memset(oppose , 0 , sizeof(oppose));
    int C,D,N;
    cin>>C;
    FOR(i,C){
      string s;
      cin>>s;
      combine[s[0]][s[1]]=s[2];
      combine[s[1]][s[0]]=s[2];
    }
    cin>>D;
    FOR(i,D){
      string s;
      cin>>s;
      oppose[s[0]][s[1]] = oppose[s[1]][s[0]] = true;
    }
    cin>>N;
    string e;
    cin>>e;
    vector<char> ans;
    FOR(i,N){
      ans.push_back(e[i]);
      bool combined = false;
      while(SZ(ans) >= 2){
        char c = combine[ans[SZ(ans)-1]][ans[SZ(ans)-2]];
        if(c != 0){
          ans.pop_back();
          ans.pop_back();
          ans.push_back(c);
        }else{
          break;
        }
      }
      FOR(j,SZ(ans)-1){
        bool oppose_flg = oppose[ans.back()][ans[j]]; 
        if(oppose_flg){
          ans.clear();
        }
      }
    }
    printf("Case #%d: %s\n" , case_no++ , reform(ans).c_str());
  }
  return 0 ;
}
