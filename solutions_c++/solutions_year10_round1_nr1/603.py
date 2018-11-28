#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
using namespace std;

#define REP(i, n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i, a, b) for (int i = (a); i < (int)(b); ++i)
#define FOREACH(i, c) for (__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

char field[100][100];
char roteted[100][100];

int main()
{
  int T;
  scanf("%d", &T);
  REP(testcase, T) {
    int N, K;
    scanf("%d%d", &N, &K);
    REP(y, N) {
      REP(x, N) {
        scanf(" %c", &field[y][x]);
      }
    }

    REP(y, N) {
      REP(x, N) {
        roteted[y][x] = field[N-x-1][N-y-1];
      }
    }

    REP(x, N) {
      REP(y, N) {
        int j = 0;
        REP(k, N) {
          if (roteted[k][x] != '.') {
            roteted[j][x] = roteted[k][x];
            ++j;
          }
        }
        FOR(k, j, N) {
          roteted[k][x] = '.';
        }
      }
    }

    static const int dy[] = {1, 0, 1, 1};
    static const int dx[] = {0, 1, -1, 1};

    int win[2] = {0, 0};
    REP(k, 4) {
      REP(y, N) {
        REP(x, N) {
          REP(c, 2) {
            static const char color[] = {'R', 'B'};
            int xx = x, yy = y;
            int j;
            for (j = 0; j < K; ++j) {
              if (xx < 0 || xx >= N || yy < 0 || yy >= N) {
                break;
              }
              if (roteted[yy][xx] != color[c]) {
                break;
              }
              xx += dx[k], yy += dy[k];
            }
            if (j == K)
              win[c] = 1;
          }
        }
      }
    }

    static const char* answer[] = {"Neither", "Red", "Blue", "Both"};
    printf("Case #%d: %s\n", testcase+1, answer[win[0]+2*win[1]]);
  }
}
