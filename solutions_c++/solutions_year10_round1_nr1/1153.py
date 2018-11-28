#include<iostream>
#include<vector>
#include<string>
#include <algorithm>
#include <utility>

using namespace std;

#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair

char field[64][64];
char rot[64][64];




string solve(int N, int K)
{
  // rotate
  REP(i, N) {
    REP(j, N) {
      rot[i][j] = field[N-j-1][i];
    }
  }

  // REP(i, N) {
  //   REP(j, N) {
  //     cout << rot[i][j];
  //   }
  //   cout << endl;
  // }
  // cout << endl;
  // gravity
  REP(j, N) {
    for (int i = N-1; i >= 0; ) {
      if (rot[i][j] == '.') {
        int dottop = i-1;
        while (dottop >= 0 && rot[dottop][j] == '.') dottop--;
        if (dottop >= 0) {
          for (int k = i; k > 0; k--) {
            swap(rot[k][j], rot[k-1][j]);
          }
        } else {
          i--;
        }
      } else {
        i--;
      }
    }
  }

  // REP(i, N) {
  //   REP(j, N) {
  //     cout << rot[i][j];
  //   }
  //   cout << endl;
  // }
  
  // search
  int dx[] = {-1, 0, 1, 1, 1, 0, -1, -1};
  int dy[] = {-1, -1, -1, 0, 1, 1, 1, 0};
  bool red = false;
  bool blue = false;
  REP(i, N) {
    REP(j, N) {
      if (rot[i][j] == '.') continue;
      char col = rot[i][j];
      REP(k, 8) {
        int length = 1;
        int ni = i;
        int nj = j;
        for (;;) {
          ni += dy[k];
          nj += dx[k];
          if (ni < 0 || nj < 0 || ni >= N || nj >= N || rot[ni][nj] != col) break;
          length++;
        }
        if (length >= K) {
          if (col == 'R') red = true;
          else if (col == 'B') blue = true;
          break;
        }
      }
    }
  }

  //cout << "red:" << red << " blue:" << blue << endl;
  if (red && blue) return "Both";
  else if (red) return "Red";
  else if (blue) return "Blue";
  else return "Neither";
}


int main()
{
  int T, K, N;
  cin >> T;
  REP(cs, T) {
    cin >> N >> K;
    REP(i, N) REP(j, N) cin >> field[i][j];
    cout << "Case #" << cs+1 << ": " << solve(N, K) << endl;
  }
  return 0;
}
