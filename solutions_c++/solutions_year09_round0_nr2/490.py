#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iomanip>
#include <memory>
#include <cstring>
#include <climits>
#include <cassert>
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBGN(x) cout << #x << " = " << x << endl;
#define DBG(x) cout << #x << " = " << x << ", ";
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl;
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl;

#define FIN "test.in"
#define FOUT "test.out"

#define MAXH 100
#define MAXW 100

int H, W;
int alt[MAXH][MAXW], a[MAXH][MAXW], minalt[MAXH][MAXW];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

inline bool ok(int x, int y) {
  if (x >= 0 && x < H && y >= 0 && y < W)
    return true;
  return false;
}

int main()
{
    freopen(FIN, "r", stdin);
    freopen(FOUT, "w", stdout);

    int T;
    cin >> T;
    REP(zzz, T) {
      cin >> H >> W;
      REP(i, H) REP(j, W) {
        scanf("%d", &alt[i][j]);
        a[i][j] = -1;
      }
      int basin_count = 0;
      queue<pair<int,int> > bfs;
      REP(i, H) REP(j, W) {
        int min_alt = alt[i][j];
        minalt[i][j] = -1;
        REP(k, 4) {
          int x = i + dx[k];
          int y = j + dy[k];
          if (ok(x, y)) {
            if (alt[x][y] < min_alt) {
              min_alt = alt[x][y];
              minalt[i][j] = k;
            }
          }
        }
        if (minalt[i][j] == -1) {
          a[i][j] = basin_count;
          ++basin_count;
          bfs.push(MP(i, j));
        }
      }
      while(!bfs.empty()) {
        pair<int,int> pii = bfs.front();
        bfs.pop();
        REP(k, 4) {
          int x = pii.first + dx[k];
          int y = pii.second + dy[k];
          /*if (ok(x, y)) {
            DBG(pii.first); DBG(pii.second); DBG(x); DBG(y); DBG(a[x][y]); DBG(k); DBGN(minalt[x][y]);
          }*/
          if (ok(x, y) && (a[x][y] == -1) && (minalt[x][y] == 3 - k)) {
            a[x][y] = a[pii.first][pii.second];
            bfs.push(MP(x, y));
          }
        }
      }
      string s(basin_count, '0');
      char current_letter = 'a' - 1;
      printf("Case #%d:\n", zzz + 1);
      REP(i, H) {
        REP(j, W) {
          assert(a[i][j] != -1);
          if (s[a[i][j]] == '0') {
            ++current_letter;
            s[a[i][j]] = current_letter;
          }
          // cout << a[i][j] << ' ';
          cout << s[a[i][j]] << ' ';
        }
        cout << endl;
      }
    }

    fflush(stdout);
    fclose(stdin);
    fclose(stdout);

    return 0;
}
