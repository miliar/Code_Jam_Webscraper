#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include<cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<bitset>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)
#define dbg(x) cout << __LINE__ << ' ' << #x << " = " << (x) << endl


typedef long long ll;

using namespace std;

const int N = 4;

class State{
public:
  char t[N][N];
  bool win(char c){
    rep(i, N){
      int cnt = 0;
      rep(j, N){
	if(t[i][j] == c)cnt++;
	if(t[i][j] == 'T')cnt++;
      }
      if(cnt >= 4)return true;
    }
    rep(i, N){
      int cnt = 0;
      rep(j, N){
	if(t[j][i] == c)cnt++;
	if(t[j][i] == 'T')cnt++;
      }
      if(cnt >= 4)return true;
    }
    int cnt = 0;
    rep(i, N){
      if(t[i][i] == c)cnt++;
      if(t[i][i] == 'T')cnt++;
    }
    if(cnt >= 4)return true;
    
    cnt = 0;
    rep(i, N){
      if(t[i][N-i-1] == c)cnt++;
      if(t[i][N-i-1] == 'T')cnt++;
    }
    if(cnt >= 4)return true;
    return false;
  }
  bool end(){
    int cnt = 0;
    rep(i, N){
      rep(j, N){
	if(t[i][j] != '.')cnt++;
      }
    }
    return N*N == cnt;
  }
  string solve(){
    bool O = win('O');
    bool X = win('X');
    assert(!(O && X));
    if(O)return "O won";
    if(X)return "X won";
    if(end())return "Draw";
    return "Game has not completed";
  }
};

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    State s;
    rep(i, N){
      rep(j, N){
	cin >> s.t[i][j];
      }
    }
    cout << "Case #" << tc+1 <<": " << s.solve() << endl;
  }
  return 0;
}
