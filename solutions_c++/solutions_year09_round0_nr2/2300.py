// BEGIN CUT HERE
// #define _GLIBCXX_DEBUG
#include "cout.h"
// END CUT HERE
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <cmath>
#include <queue>
#include <list>
#include <complex>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long LL;
typedef complex<double> CMP;
#define Fill(a, b) memset((a), (b), sizeof(a))
#define REP(a, b) for (size_t (a) = 0; (a)<(size_t)(b); ++(a))
#define sz size()
#define Tr(c, i) for(typeof((c).begin()) i= (c).begin(); (i) != (c).end(); ++(i))
#define All(c) (c).begin(), (c).end()
#define Present(c, x) ((c).find(x) != (c).end()) // for Map or Set
#define CPresent(c, x) (find(All(c), x) != end()) // for vector

int main(void)
{
  int T;
  cin >> T;
  int dx[4] = {0, -1, 1, 0};
  int dy[4] = {-1, 0, 0, 1};
  int rev[4] = {3, 2, 1, 0};
  REP(t, T) {
    int  H, W;
    cin >> H >> W;
    int m1[H][W];
    vector<int> m2[H][W];
    char ans[H][W];
    REP(i, H) REP(j, W) {
      ans[i][j] = '.';
    }

    REP(i, H) {
      REP(j, W) {
        int c;
        cin >> c;
        m1[i][j] = c;
      }
    }
    vector <pair <int, int> > sinks;
    REP(i, H) {
      REP(j, W) {
        int c = m1[i][j];
        int minalt = c;
        int r = -1;

        int x, y;
        REP(k, 4) {
          x = j + dx[k];
          y = i + dy[k];
          if (x >= 0 && (x < W) &&
              y >= 0 && y < H) {
            if (minalt > m1[y][x]) {
              minalt = m1[y][x];
              r = k;
            }
          }
        }
        if (r < 0) {
          sinks.push_back(make_pair(i, j));
        } else {
          x = j + dx[r];
          y = i + dy[r];
          m2[y][x].push_back(rev[r]);
        }
      }
    }

    vector<pair <pair<int, int>, pair<int, int> > > sink_nws;

    REP(i, sinks.sz) {
      pair<int, int> sink = sinks[i];
      int sy = sink.first, sx = sink.second;
      vector<pair<int, int> > w;
      w.push_back(sink);
      int nwx = sx, nwy = sy;
      
      while(w.sz > 0) {
        vector<pair <int, int> > nw;
        REP(j, w.sz) {
          int tsy = w[j].first;
          int tsx = w[j].second;
          if (tsy < nwy || (tsy == nwy && tsx < nwx)) {
            nwy = tsy;
            nwx = tsx;
          }
          vector<int> dirs = m2[tsy][tsx];
          REP(k, dirs.sz) {
            int ny = tsy+dy[dirs[k]], nx = tsx+dx[dirs[k]];
            nw.push_back(make_pair(ny, nx));
          }
        }
        w = nw;
      }
      sink_nws.push_back(make_pair(make_pair(nwy, nwx), make_pair(sy, sx)));
    }
    sort(All(sink_nws));
    char mark = 'a';
    REP(i, sink_nws.sz) {
      int sy = sink_nws[i].second.first;
      int sx = sink_nws[i].second.second;
      vector<pair<int, int> > w;
      w.push_back(make_pair(sy, sx));
      while(w.sz > 0) {
        vector<pair <int, int> > nw;
        REP(j, w.sz) {
          int tsy = w[j].first;
          int tsx = w[j].second;
          ans[tsy][tsx] = mark;
          vector<int> dirs = m2[tsy][tsx];
          REP(k, dirs.sz) {
            int ny = tsy + dy[dirs[k]];
            int nx = tsx + dx[dirs[k]];
            nw.push_back(make_pair(ny, nx));
          }
        }
        w = nw;
      }
      mark++;
    }

    cout << "Case #" << (t+1) << ":" << endl;
    REP(i, H) {
      REP(j, W) {
        cout << ans[i][j];
        if ((int)j < W-1) {
          cout << ' ';
        }
      }
      cout << endl;
    }

    // print the answer
  }
  return 0;
}

