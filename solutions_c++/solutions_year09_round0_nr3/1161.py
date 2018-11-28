#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <numeric>

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,b,n) for(int i=(b);i<(int)(n);++i)

using namespace std;

const int N=1024;
const int MOD=10000;
int main(){
  const string gcj="welcome to code jam";

  int C; cin >> C;
  string s;
  getline(cin,s);
  REP(CC,C){
    getline(cin,s);
    static int result[24][N];
    memset(result,0,sizeof result);

    REP(j,s.size()) result[0][j]=(s[j]==gcj[0] ? 1 : 0);
    FOR(i,1,gcj.size()) REP(j,s.size()) if(gcj[i]==s[j]){
      result[i][j]+=accumulate(result[i-1],result[i-1]+j,0);
      result[i][j]%=MOD;
    }
    
    printf("Case #%d: %04d\n",CC+1,accumulate(result[18],result[18]+N,0)%MOD);
  }

}
