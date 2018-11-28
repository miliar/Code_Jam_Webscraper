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

#include<windows.h>
#include<process.h>

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
  int L , D , N;
  cin>>L>>D>>N;
  vector<string> dic(D);
  FOR(i,D) cin>>dic[i];
  FOR(i,N){
    int ans = 0;
    bool is_in=false;
    string s;
    cin>>s;
    vector<string> tokens;
    FOR(j,SZ(s)){
      char c = s[j];
      if(c=='(') {
        is_in = true;
        tokens.push_back("");
      }
      else if(c==')') is_in = false;
      else{
        if(is_in){
          tokens[SZ(tokens)-1] += c;
        }else{
          tokens.push_back(string(1,c));
        }
      }
    }
    assert(SZ(tokens)==L);
    FOR(j,SZ(dic)){
      bool ok = true;
      FOR(k,SZ(tokens)) {
        string& tok = tokens[k];
        if(tok.find(dic[j][k]) == string::npos){
          ok = false;
        }
      }
      if(ok) ans++;
    }

    printf("Case #%d: %d\n" , i+1 , ans);
  }
  return 0 ;
}
