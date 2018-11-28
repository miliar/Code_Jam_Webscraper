#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define rep(x,n) for(int x = 0; x < n; ++x)
#define print(x) cout << x << endl
#define dbg(x) cerr << #x << " == " << x << endl
#define _ << " , " <<
#define mp make_pair
#define x first
#define y second

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;
typedef pair<int,int> pii;

int main() {
  int T; cin>>T;
  for(int testcase=1;testcase<=T;testcase++) {
    static char board[5][5];
    rep(i,4) cin>>board[i];
    int isX=0, isO=0, isIncomplete=0;
    rep(i,4) rep(j,4) if(board[i][j]=='.') isIncomplete=1;
    map<char,int> diagonal1, diagonal2;
    rep(i,4) {
      map<char,int> line, column;
      rep(j,4) line[board[i][j]]++, column[board[j][i]]++;
      if(line['X']+line['T']>=4||column['X']+column['T']>=4) isX=1;
      if(line['O']+line['T']>=4||column['O']+column['T']>=4) isO=1;
      diagonal1[board[i][i]]++;
      diagonal2[board[i][3-i]]++;
    }
    if(diagonal1['X']+diagonal1['T']>=4||diagonal2['X']+diagonal2['T']>=4) isX=1;
    if(diagonal1['O']+diagonal1['T']>=4||diagonal2['O']+diagonal2['T']>=4) isO=1;
    assert(!isX||!isO);
    printf("Case #%d: ",testcase);
    if(isX) puts("X won");
    else if(isO) puts("O won");
    else if(isIncomplete) puts("Game has not completed");
    else puts("Draw");
  }
  return 0;
}
