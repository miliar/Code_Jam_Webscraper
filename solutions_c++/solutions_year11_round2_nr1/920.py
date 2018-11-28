#include <iostream>
#include <cstdio>

using namespace std;

const int N = 100;

string s[N];
double wp[N];
double owp[N];
double oowp[N];

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    int n; cin >> n;
    for (int i = 0; i < n; i++) cin >> s[i];

    for (int i = 0; i < n; i++) {
      int w = 0, g = 0;
      for (int j = 0; j < n; j++) {
        if (s[i][j] == '1') w++, g++;
        else if (s[i][j] == '0') g++;
      }
      wp[i] = double(w) / g;
    }

    for (int j = 0; j < n; j++) {
      int g = 0, w = 0;
      owp[j] = 0;
      for (int i = 0; i < n; i++) {
        if (s[i][j] == '.') continue;
        g++;
        int ww = 0, gg = 0;
        for (int k = 0; k < n; k++) if (k != j) {
          if (s[i][k] == '.') continue;
          gg++;
          if (s[i][k] == '1') ww++;
        }
        owp[j] += double(ww) / gg;
      }
      owp[j] /= g;
    }

    for (int i = 0; i < n; i++) {
      oowp[i] = 0;
      int g = 0;
      for (int j = 0; j < n; j++) {
        if (s[i][j] == '.') continue;
        oowp[i] += owp[j];
        g++;
      }
      oowp[i] /= g;
    }

    cout << "Case #" << tt << ":" << endl;
    for (int i = 0; i < n; i++) {
      printf("%.9lf\n", wp[i] / 4 + owp[i] / 2 + oowp[i] / 4);
    }
  }
  return 0;
}

