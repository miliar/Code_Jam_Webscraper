#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

double wp[110], owp[110];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n; cin >> n;
    vector<string> wins;
    for (int i = 0; i < n; i++) {
      string s; cin >> s;
      wins.push_back(s);
    }

    for (int i = 0; i < n; i++) {
      int nw = 0, nt = 0;
      for (int j = 0; j < n; j++) {
        nw += wins[i][j] == '1';
        nt += wins[i][j] != '.';
      }
      wp[i] = (1.0*nw)/nt;

      double owp_tot = 0;
      for (int j = 0; j < n; j++) {
        if (wins[i][j] == '.') continue;
        int onw = 0, ont = 0;
        for (int k = 0; k < n; k++) {
          if (i == k) continue;
          onw += wins[j][k] == '1';
          ont += wins[j][k] != '.';
        }
        owp_tot += (1.0*onw)/ont;
      }
      owp[i] = owp_tot/nt;
    }

    cout << "Case #" << c << ":" << endl;
    cout.setf(ios::fixed); cout << setprecision(7);
    for (int i = 0; i < n; i++) {
      double rpi = 0.25 * wp[i] + 0.50 * owp[i];
      double oowp_tot = 0; int nt = 0;
      for (int j = 0; j < n; j++) {
        if (wins[i][j] == '.') continue;
        oowp_tot += owp[j]; nt++;
      }
      rpi += 0.25*oowp_tot/nt;
      cout << rpi << endl;
    }
  }
  return 0;
}
