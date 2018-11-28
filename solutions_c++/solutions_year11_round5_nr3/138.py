#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;

template<typename T> ostream& operator<<( ostream &os, const vector<T> &v ) { os << "{"; for ( typename vector<T>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " " << *vi; } os << " }"; return os; }
template<> ostream& operator<<( ostream &os, const vector<string> &v ) { os << "{"; for ( vector<string>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " \"" << *vi << "\""; } os << " }"; return os; }
template<typename T, typename U> ostream& operator<<( ostream &os, const pair<T, U> &P ) { return os << "(" << P.first << ", " << P.second << ")"; }
template<typename T> ostream& operator<<( ostream &os, const set<T> &S ) { return os << vector<T>( S.begin(), S.end() ); }
template<typename T, typename U> ostream& operator<<( ostream &os, const map<T, U> &M ) { for ( typename map<T, U>::const_iterator mi=M.begin(); mi!=M.end(); ++mi ) { os << mi->first << " => " << mi->second << endl; } return os; }

int R, C;
char board[105][105];
int COOKIE[105][105];

void move(int &x, int &y, int dir) {
  switch (board[y][x]) {
    case '\\':
      x += dir;
      y += dir;
      break;
    case '/':
      x += dir;
      y -= dir;
      break;
    case '|':
      y += dir;
      break;
    case '-':
      x += dir;
      break;
    default:
      abort();
  }

  if (x < 0) x = C-1; if (x == C) x = 0;
  if (y < 0) y = R-1; if (y == R) y = 0;
}

bool sim(int mask) {
  static int t = 0; ++t;

  // fprintf(stderr, "sim(%d)\n", mask);

  for (int y0=0; y0<R; ++y0) {
    for (int x0=0; x0<C; ++x0) {
      if (COOKIE[y0][x0] == t) {
        continue;
      }

      int y = y0, x = x0;
      // fprintf(stderr, "  y0 = %d, x0 = %d\n", y0, x0);

      while (1) {
        COOKIE[y][x] = t;
        int bit = (mask >> (y*C + x)) & 1;
        // fprintf(stderr, "    y = %d, x = %d, bit = %d\n", y, x, bit);
        move(x, y, bit ? 1 : -1);
        // fprintf(stderr, "    y = %d, x = %d\n", y, x);
        if (x == x0 && y == y0) {
          break;
        }
        if (COOKIE[y][x] == t) {
          return false;
        }
      }
    }
  }
  return true;
}

int main(void) {
  cin.sync_with_stdio(0);

  int CASES; cin >> CASES;
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    cin >> R >> C;
    for (int i=0; i<R; ++i) {
      cin >> board[i];
    }

    int res = 0;
    for (int mask=0; mask<(1<<R*C); ++mask) {
      res += sim(mask);
    }

    cout << "Case #" << tt << ": " << (res%1000003) << endl;
  }

  return 0;
}
