#include <iostream>

using namespace std;

int testcase;
int n, l, h;
int a[ 100 ];

int main(int argc, char *argv[]) {
  cin >> testcase;
  for (int tn = 1; tn <= testcase; ++tn) {
    cin >> n >> l >> h;
    for (int j = 0; j < n; ++j)
      cin >> a[j];
    int ans = -1;
    for (int i = l; i <= h; ++i) {
      int flag = 0;
      for (int j = 0; j < n; ++j) {
        if (! (i % a[j] == 0 || a[j] % i == 0)) {
          flag = 1;
          break;
        }
      }
      if (flag == 0) {
        ans = i;
        break;
      }
    }
    if ( ans == -1) {
      cout << "Case #" << tn << ": " << "NO" << endl;
    } else {
      cout << "Case #" << tn << ": " << ans << endl;
    }
  }
  return 0;
}

