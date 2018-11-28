#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

double safediv(double a, int b) {
  return b == 0 ? 0 : a / b;
}

int main() {
  cin.sync_with_stdio(0);
  int CASES; cin >> CASES;

  for (int tt=1; tt<=CASES; ++tt) {
    int n; cin >> n;
    string table[n];
    for (int i=0; i<n; ++i) {
      cin >> table[i];
    }

    vector<double> wp(n), owp(n), oowp(n);

    vector<int> wpa(n, 0), wpb(n, 0);
    for (int i=0; i<n; ++i) {
      for (int j=0; j<n; ++j) {
        wpa[i] += table[i][j] == '1';
        wpb[i] += table[i][j] != '.';
      }
      wp[i] = safediv(wpa[i], wpb[i]);
    }

    for (int i=0; i<n; ++i) {
      int owpb = 0;
      for (int j=0; j<n; ++j) {
        if (table[i][j] == '.') {
          continue;
        }
        int a = wpa[j], b = wpb[j];
        a -= table[j][i] == '1';
        b -= table[j][i] != '.';
        owp[i] += safediv(a, b);
        owpb += 1;
      }
      owp[i] = safediv(owp[i], owpb);
    }

    for (int i=0; i<n; ++i) {
      int oowpb = 0;
      for (int j=0; j<n; ++j) {
        if (table[i][j] == '.') {
          continue;
        }
        oowp[i] += owp[j];
        oowpb += 1;
      }
      oowp[i] = safediv(oowp[i], oowpb);
    }

    printf("Case #%d:\n", tt);
    for (int i=0; i<n; ++i) {
      printf("%.12f\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
    }
  }

  return 0;
}
