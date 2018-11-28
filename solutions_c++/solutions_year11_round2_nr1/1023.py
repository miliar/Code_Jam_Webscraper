/* Rajat Goel (C++) */
#include <algorithm>
#include <iostream>
#include <iterator>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int>  pii;
typedef long long      LL;
typedef long double    LD;
const int  INF  =      INT_MAX / 2 - 1;
const LL   LINF =      LLONG_MAX / 2 - 1;
const LD   EPS  =      1e-7;
#define loop(i, n)     for (int i = 0; i < int(n); ++i)
#define foreach(i, a)  for (typeof((a).begin()) i = (a).begin();i != (a).end(); ++i)
template<typename T>
inline int fCMP(T x, T y = 0, T tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main(int argc, char *argv[]) {
	int T; scanf(" %d", &T);
	for (int X = 1; X <= T; ++X) {
    int N; scanf(" %d", &N);
    vector<string> arr;
    loop (i, N) {
      string s;
      cin >> s;
      arr.push_back(s);
    }

    vector<int> tm, wm;
    loop (i, N) {
      int total = 0, won = 0;
      loop (j, N) {
        if (arr[i][j] != '.') {
          total += 1;
        }

        if (arr[i][j] == '1') {
          won += 1;
        }
      }

      tm.push_back(total);
      wm.push_back(won);
    }

    vector<double> WP, OWP, OOWP;
    loop (i, N) {
      WP.push_back(wm[i] * 1.0 / tm[i]);
      cout << "WP " << i + 'A' << " = " << WP[i] << endl; 
    }

    loop (i, N) {
      vector<double> other_wp;
      loop (j, N) {
        if (arr[i][j] == '.') continue;

        int tmp_wm = wm[j], tmp_tm = tm[j];
        if (arr[j][i] != '.') {
          tmp_tm -= 1;
          if (arr[j][i] == '1') {
            tmp_wm -= 1;
          }

        }
        other_wp.push_back(tmp_wm * 1.0 / tmp_tm);
      }

      double sm = 0;
      foreach (it, other_wp) {
        sm += *it;
      }
      OWP.push_back(sm / other_wp.size());
      cout << "OWP " << i + 'A' << " = " << OWP[i] << endl; 
    }

    loop (i, N) {
      int t = 0;
      double sm = 0;
      loop (j, N) {
        if (arr[i][j] != '.') {
          t += 1;
          sm += OWP[j];
        }
      }

      OOWP.push_back(sm / t);
    }

    vector<double> rpi;
    loop (i, N) {
      rpi.push_back(0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
    }

		printf("Case #%d:\n", X);
    loop (i, N) {
      printf("%.9lf\n", rpi[i]);
    }
	}
	return 0;
}
