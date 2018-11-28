#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <iomanip>


using namespace std;
//#define DBG
 int n, t;
 long double g[300];
 long double w[300];
 long double wp[300], owp[300], oowp[300];
int main() {
#ifdef DBG
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
#endif
  cin >> t;
  for (int q = 0; q < t; ++q) {
    cin >> n;
    string s;
    vector <string> ss;
    getline (cin, s);
    for (int i = 0; i < n; ++i) {
      getline (cin, s);
      ss.push_back(s);
    }
    for (int i = 0; i < n; ++i) {
      w[i] = 0;
      g[i] = 0;
      for (int j = 0; j < n; ++j) {
        if (ss[i][j] == '1')
          w[i]++;
        if (ss[i][j] != '.') {
          g[i]++;
        }
      }
      wp[i] = w[i] / g[i];
    }
    for (int i = 0; i < n; ++i) {
      owp[i] = 0;
      for (int j = 0; j < n; ++j) {
        if (ss[i][j] != '.') {
          if (ss[i][j] == '1') {
            owp[i] += w[j] / (g[j] - 1);
          }  else {
            owp[i] += (w[j] - 1) / (g[j] - 1);
          }
        }
      }
      owp[i] /= g[i];
    }
    for (int i = 0; i < n; ++i) {
      oowp[i] = 0;
      for (int j = 0; j < n; ++j) {
        if (ss[i][j] != '.') {
          oowp[i] += owp[j];
        }
      }
      oowp[i] /= g[i];
    }
    cout << "Case #" << q + 1 << ':' << endl;
    for (int i = 0; i < n; ++i) {
      cout << fixed << setprecision(7) << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl; 
    }
  }
  return 0;
}