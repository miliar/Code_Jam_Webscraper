#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int table[100][100];
int n;

double wp[100];
double owp[100];

double compWPex(int team, int ex) {
  int total = 0;
  int won = 0;
  for (int i = 0; i < n; ++i) {
    if (i != ex && table[team][i] != - 1) {
      ++total;
      won += table[team][i];
    }
  }
  return (double) won / (double) total;
}

void compWPs() {
  for (int t = 0; t < n; ++t)
    wp[t] = compWPex(t, -1);
}

void compOWPs() {
  for (int i = 0; i < n; ++i) {
    double res = 0.0;
    int nopps = 0;
    for (int j = 0; j < n; ++j) {
      if (table[i][j] != -1) {
        ++nopps;
        res += compWPex(j, i);
      }
    }
    owp[i] = res / nopps;
  }
}


double score(int i) {
  double oowp = 0.0;
  int nopps = 0;
  for (int j = 0; j < n; ++j) {
    if (table[i][j] != -1) {
      oowp += owp[j];
      ++nopps;
    }
  }
  oowp /= nopps;
  return 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp;
}

int main() {
  int ntests = 0;
  cin >> ntests;
  for (int t = 1; t <= ntests; ++t) {

    cin >> n;
    for (int i = 0; i < n; ++i) {
      string s;
      cin >> s;
      for (int j = 0; j < n; ++j) {
        switch (s[j]) {
          case '1':
            table[i][j] = 1;
            break;
          case '0':
            table[i][j] = 0;
            break;
          default:
            table[i][j] = -1;
        }
      }
    }

    compWPs();
    compOWPs();
    
    cout << "Case #" <<t << ": " << endl;
    for (int i = 0; i < n; ++i)
      printf("%.10lf\n", score(i));
  }
  return 0;
}
