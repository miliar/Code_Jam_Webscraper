#include <iostream>
#include <sstream>
using namespace std;

int but[110][2];

int main() {
  int t; cin >> t;
  string tmp;
  for (int c = 1; c <= t; c++) {
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
      char c;
      cin >> c >> but[i][0];
      but[i][1] = c;
    }

    int lp[2], lt[2], curt = 0;
    lp[0] = lp[1] = 1;
    lt[0] = lt[1] = 0;
    for (int i = 0; i < n; i++) {
      if (but[i][1] == 'O') {
        lt[0] += abs(lp[0] - but[i][0]);
        lt[0] = max(lt[0], curt)+1;
        lp[0] = but[i][0];
      } else {
        lt[1] += abs(lp[1] - but[i][0]);
        lt[1] = max(lt[1], curt)+1;
        lp[1] = but[i][0];
      }
      curt = max(lt[0], lt[1]);
    }
    cout << "Case #" << c << ": " << curt << endl;
  }
  return 0;
}
