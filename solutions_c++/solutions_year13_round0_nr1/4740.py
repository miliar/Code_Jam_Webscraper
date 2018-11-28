#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <cassert>
#include <string>
#include <memory.h>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <cctype>
#include <iomanip>
#include <sstream>
#include <cctype>
#include <fstream>
#include <cmath>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define ITER(c) __typeof((c).begin())
#define PB(e) push_back(e)
#define FOREACH(i, c) for(ITER(c) i = (c).begin(); i != (c).end(); ++i)
#define MP(a, b) make_pair(a, b)
#define PARITY(n) ((n) & 1)

typedef long long ll;
typedef pair<ll, ll> P;
const int INF = 1000 * 1000 * 1000 + 7;
const double EPS = 1e-10;

bool win(char board[4][4]){
  REP(i, 4){
    int count = 0;
    REP(j, 4) if(board[i][j] == 'O' || board[i][j] == 'T') count++;
    if(count == 4) return true;
  }
  REP(j, 4){
    int count = 0;
    REP(i, 4) if(board[i][j] == 'O' || board[i][j] == 'T') count++;
    if(count == 4) return true;
  }
  int count1 = 0, count2 = 0;
  REP(i, 4) if(board[i][i] == 'O' || board[i][i] == 'T') count1++;
  REP(i, 4) if(board[i][3-i] == 'O' || board[i][3-i] == 'T') count2++;
  return count1 == 4 || count2 == 4;
}

string solve(){
  char board[4][4];
  REP(i, 4)REP(j, 4) cin >> board[i][j];

  if(win(board)) return "O won";
  
  REP(i, 4)REP(j, 4){
    switch(board[i][j]){
    case 'X':
      board[i][j] = 'O';
      break;
    case 'O':
      board[i][j] = 'X';
      break;
    }
  }
  
  if(win(board)) return "X won";
  
  REP(i, 4)REP(j, 4) if(board[i][j] == '.') return "Game has not completed";
  return "Draw";
}

int main(){
  int T;
  cin >> T;
  REP(t, T){
    printf("Case #%d: %s\n", t + 1, solve().c_str());
  }
  return 0;
}
