#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

  int ncases;
  cin >> ncases;

  for (int i=0;i<ncases;i++) {
    int n, pd, pg;
    cin >> n;
    cin >> pd;
    cin >> pg;
    bool t = true;
    if (pd > 0) {
      if (pg == 0) {
        t = false;
      };
    };
    if (pd < 100) {
      if (pg == 100) {
        t = false;
      };
    };
    if (t) {
      t = false;
      for (int j=1;j<=min(100,n);j++) {
        if ((pd*j % 100) == 0) {
          t = true;
          break;
        };
      };
    };
    cout << "Case #" << i+ 1 << ": ";
    if (t) {
      cout << "Possible";
    } else {
      cout << "Broken";
    };
    cout << endl;
  };

  return 0;

};
