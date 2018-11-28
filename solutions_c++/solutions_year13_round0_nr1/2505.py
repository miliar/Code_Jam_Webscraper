#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <complex>
#include <numeric>
#include <ext/numeric>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <functional>
#include <utility>
#include <vector>
#include <list>
#include <queue>
#include <bitset>

using namespace std;
using namespace __gnu_cxx;

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

char grid[8][8];

enum Status {
  X_WON, O_WON, DRAW, INCOMPLETE
};

bool won(Status st) {
  return st == X_WON || st == O_WON;
}

bool match(char x, char y) {
  return x == y || x == 'T' || y == 'T';
}


int main() {
  
  int n_cases;
  scanf("%d", &n_cases);

  for (int ctr = 0; ctr < n_cases; ++ctr) {
    for (int i = 1; i <= 4; ++i) {
      scanf("%s", grid[i] + 1);
    }

    Status status = DRAW;
    // check for incomplete or draw
    for (int i = 1; status == DRAW && i <= 4; ++i) {
      for (int j = 1; j <= 4; ++j) {
        if (grid[i][j] == '.') {
          status = INCOMPLETE;
          break;
        }
      }
    }

    // Due to laziness, I shall copy-paste :)) Forgive me.
    // rows
    for (int i = 1; !won(status) && i <= 4; ++i) {
      char fsym = grid[i][1];
      if (fsym != '.') {
        bool straight = true;
        for (int j = 2; j <= 4; ++j) {
          if (!match(grid[i][j], fsym)) {
            straight = false;
            break;
          } else if (grid[i][j] != 'T') {
            fsym = grid[i][j];
          }
        }
        if (straight) {
          if (fsym == 'X') status = X_WON;
          else status = O_WON;
        }
      }
    }

    // cols
    for (int i = 1; !won(status) && i <= 4; ++i) {
      char fsym = grid[1][i];
      if (fsym != '.') {
        bool straight = true;
        for (int j = 2; j <= 4; ++j) {
          if (!match(grid[j][i], fsym)) {
            straight = false;
            break;
          } else if (grid[j][i] != 'T') {
            fsym = grid[j][i];
          }
        }
        if (straight) {
          if (fsym == 'X') status = X_WON;
          else status = O_WON;
        }
      }
    }

    // ldiag
    if (!won(status)) {
      char fsym = grid[1][1];
      if (fsym != '.') {
        bool straight = true;
        for (int i = 2; i <= 4; ++i) {
          if (!match(grid[i][i], fsym)) {
            straight = false;
            break;
          } else if (grid[i][i] != 'T') {
            fsym = grid[i][i];
          }
        }
        if (straight) {
          if (fsym == 'X') status = X_WON;
          else status = O_WON;
        }
      }
    }

    // ldiag
    if (!won(status)) {
      char fsym = grid[1][4];
      if (fsym != '.') {
        bool straight = true;
        for (int i = 2; i <= 4; ++i) {
          if (!match(grid[i][5-i], fsym)) {
            straight = false;
            break;
          } else if (grid[i][5-i] != 'T') {
            fsym = grid[i][5-i];
          }
        }
        if (straight) {
          if (fsym == 'X') status = X_WON;
          else status = O_WON;
        }
      }
    }

    printf("Case #%d: ", ctr+1);
    
    switch (status) {
      case X_WON:
        printf("X won\n");
        break;
      case O_WON:
        printf("O won\n");
        break;
      case DRAW:
        printf("Draw\n");
        break;
      case INCOMPLETE:
        printf("Game has not completed\n");
        break;
    }
  }



  return 0;
}
