#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
#include<stack>
#include<deque>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<fstream>
#include<complex>
#include<cassert>
#include<climits>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
const double PI = 3.14159265;

const string S = "welcome to code jam"; // 19
int main()
{
  string s;
  int N, dp[510][21];
  // inputをi文字つかってj個照合に成功した数
  cin >> N;
  getline(cin, s);
  REP(turn, N){
    getline(cin, s);
    memset(dp, 0, sizeof(dp));
//    REP(j, S.size())
    REP(i, s.size()) dp[i][0] = 1;
    for(int i=1; i<=s.size(); ++i){
      for(int j=1; j<=S.size(); ++j){
        if(s[i-1] == S[j-1]){
          dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % 10000;
        }else{
          dp[i][j] = dp[i-1][j];
        }
      }
    }
    printf("Case #%d: %04d\n", turn+1, dp[s.size()][S.size()]);
    //cout << dp[s.size()][S.size()] << endl;
  }
  return 0;
}

