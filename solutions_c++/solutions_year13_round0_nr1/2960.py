#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>

using namespace std;

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); k++)
#define FORE(k,a,b) for(typeof(a) k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define EXIST(s,e) ((s).find(e)!=(s).end())

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1e+9;
const double EPS = 1e-10;
const double PI = acos(-1.0);

bool valid(char c, char mark) {
  return c == mark || c == 'T';
}

bool check_row(string board[], int r, char mark) {
  if((board[r][0] == mark || board[r][0] == 'T') && 
     (board[r][1] == mark || board[r][1] == 'T') && 
     (board[r][2] == mark || board[r][2] == 'T') &&
     (board[r][3] == mark || board[r][3] == 'T')) {
    return true;
  }
  return false;
}

bool check_col(string board[], int c, char mark) {
  if((board[0][c] == mark || board[0][c] == 'T') && 
     (board[1][c] == mark || board[1][c] == 'T') && 
     (board[2][c] == mark || board[2][c] == 'T') &&
     (board[3][c] == mark || board[3][c] == 'T')) {
    return true;
  }
  return false;
}

bool check_skew(string board[], char mark) {
  if(valid(board[0][0], mark) && 
     valid(board[1][1], mark) &&
     valid(board[2][2], mark) &&
     valid(board[3][3], mark)) {
    return true;
  }
  else if(valid(board[0][3], mark) &&
          valid(board[1][2], mark) &&
          valid(board[2][1], mark) &&
          valid(board[3][0], mark)) {
    return true;
  }
  return false;
}

int main()
{
  int T;
  cin >> T;

  REP(turn, T) {
    char mark = '.';
    string board[4];
    REP(i, 4) { cin >> board[i]; }

    REP(r, 4) {
      if(check_row(board, r, 'X')) { mark = 'X'; break; }
      else if(check_row(board, r, 'O')) { mark = 'O'; break; }
    }
    
    if(mark == '.') {
      REP(c, 4) {
        if(check_col(board, c, 'X')) { mark = 'X'; break; }
        else if(check_col(board, c, 'O')) { mark = 'O'; break; }
      }
    }

    if(mark == '.') {
      if(check_skew(board, 'X')) { mark = 'X'; }
      else if(check_skew(board, 'O')) { mark = 'O'; }
    }

    if(mark != '.') {
      printf("Case #%d: %c won\n", turn+1, mark);
    }
    else {
      bool finished = true;
      REP(r, 4) REP(c, 4) {
        if(board[r][c] == '.') {
          finished = false; break;
        }
      }

      if(finished) {
        printf("Case #%d: Draw\n", turn+1);
      }
      else {
        printf("Case #%d: Game has not completed\n", turn+1);
      }
    }
  }
  
  return 0;
}
