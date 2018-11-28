#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#define sz(a) ((int)(a).size())
using namespace std;

int testcase;
int r,c,d;
vector<string> map;

int main(int argc, char *argv[]) {
  cin >> testcase;
  for (int tn = 1; tn < testcase+1; ++tn) {
    cin >> r >> c >> d;
    map.clear();
    for (int i = 0; i < r; ++i) {
      string stemp;
      cin >> stemp;
      map.push_back(stemp);
    }

    int ansflag = 0;
    for (int i = min(r,c); i >= 3 ; i--) {
      for (int j = 0; j <= r-i; ++j) {
        for (int k = 0; k <= c-i; ++k) {
          double mx=0, my=0;
          double cx=(j+(i-1)/2.0), cy = (k+(i-1)/2.0);
          for (int p = j; p < j+i; ++p) {
            for (int q = k; q < k+i; ++q) {
              if (p==j && q==k) continue;
              if (p==j && q==k+i-1) continue;
              if (p==j+i-1 && q==k) continue;
              if (p==j+i-1 && q==k+i-1) continue;
              mx += (d + (map[p][q] - '0')) * (p-cx);
              my += (d + (map[p][q] - '0')) * (q-cy);
            }
          }
          if (abs(mx) < 1e-8 && abs(my) < 1e-8) {
            cout << "Case #" << tn <<": " << i << endl;
            ansflag = 1;
            break;
          }
        }
        if (ansflag == 1) break;
      }
      if (ansflag == 1) break;
    }
    if (ansflag == 0) {
      cout << "Case #" << tn <<": IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
