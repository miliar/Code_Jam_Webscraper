#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cmath> 
#include <ctime> 
#include <float.h> 

using namespace std; 

#define REP(i, from, to) for (int i = (from); i < (to); ++i) 
#define FOR(i, n) REP(i, 0, (n)) 
#define ALL(x) x.begin(), x.end() 
#define SIZE(x) (int)x.size() 
#define PB push_back 
#define MP make_pair 

typedef long long i64; 
typedef vector<int> VI; 
typedef vector<VI> VVI; 
typedef vector<string> VS; 
typedef vector<VS> VVS; 
typedef pair<int, int> PII; 

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int t;
  cin >> t;

  FOR (tt, t) {
    int const SIZE = 4;
    VS board(SIZE);
    FOR (i, SIZE) cin >> board[i];

    set<string> res;
    bool hasEmpty = false;
    FOR (i, SIZE) FOR (j, SIZE) {
      hasEmpty |= board[i][j] == '.';
      
      if (board[i][j] == '.') continue;

      int const DI[] = {0, 1, 1, -1};
      int const DJ[] = {1, 1, 0, 1};

      FOR (k, 4) {
        string line;
        FOR (d, 4) {
          int const ni = i + d * DI[k];
          int const nj = j + d * DJ[k];

          if (ni < SIZE && nj < SIZE && ni >= 0 && nj >= 0) {
            line += board[ni][nj];
          }
        }

        sort(ALL(line));
        bool const hasLine = SIZE(line) == 4 && (line[0] == line[3] || line[0] == 'T' || line[3] == 'T') && (line.find('X') != -1 || line.find('O') != -1);
        if (hasLine) {
          if (line[3] == 'X')
            res.insert("X" + string(" won"));
          else
            res.insert("O" + string(" won"));
        }
      }
    }

    string final;
    if (hasEmpty && res.empty()) {
        final = "Game has not completed";
    }
    else if (SIZE(res) != 1) {
        final = "Draw";
    } else {
        final = *res.begin();
    }

    cout << "Case #" << tt + 1 << ": " << final << endl;
  }

  return 0;
}