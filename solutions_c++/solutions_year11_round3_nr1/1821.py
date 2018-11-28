#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// MACROS
#define PRunsigned(X, K) cout << "Case #" << X << ": " << K << endl;
#define FOR(i, a, b) for(unsigned i=(a); i<(b);++i)
#define FOREACH(T, I, J) for (T::iterator I = J.begin(); I != J.end(); ++I)
#define FOREACH_B(T, I, S, E) for (I = S; I != E; ++I)
#define FOREACH_CONST(T, I, J) for (T::const_iterator I = J.begin(); I != J.end(); ++I)
#define PRunsigned_COLLECTION(T, C) for(T::iterator it=C.begin(); it!=C.end(); ++it) cout << " " << *it;

#define PRINT_MAPPING(T, C) for(T::iterator it=C.begin(); it!=C.end(); ++it) cout << it->first << " : " << it->second << endl; cout << endl;

#define LIM 50

#define REPLACE '#'
#define ONE '1'
#define TWO '2'
#define THREE '3'
#define FOUR '4'

char mat[LIM][LIM];

int main() {
  
  unsigned T, R, C; cin >> T;
  char t;
  FOR(i, 0, T) {
  
    bool impossible = false;
    cout << "Case #" << i+1 << ": " << endl;

    cin >> R >> C;
    FOR(r, 0, R) { FOR(c, 0, C) { cin >> t; mat[r][c] = t; } }

    FOR(r, 0, R) {
      FOR(c, 0, C) {
        if (mat[r][c] == REPLACE) {
          if (r < R-1 && c < C-1) {
            mat[r][c] = ONE;
            if (mat[r][c+1] == REPLACE) { mat[r][c+1] = TWO; } else { impossible = true; }
            if (mat[r+1][c] == REPLACE) { mat[r+1][c] = THREE; } else { impossible = true; }
            if (mat[r+1][c+1] == REPLACE) { mat[r+1][c+1] = FOUR; } else { impossible = true; }
          } else {
            impossible = true;
          }
        }
        // --
        if (impossible) break;
      }
      if (impossible) break;
    }
    
    if (impossible) {
      cout << "Impossible" << endl;
    } else {
      FOR(r, 0, R) {
        FOR(c, 0, C) {
          switch (mat[r][c]) {
            case ONE: case FOUR: cout << '/'; break;
            case TWO: case THREE: cout << '\\'; break;
            default: cout << '.'; break;
          }
        }
        cout << endl;
      }
    }
  }

}

