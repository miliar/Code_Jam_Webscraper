#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    int n, s, p;
    cin >> n >> s >> p;

    int cnt = 0;
    for (int j = 0; j < n; j++) {
      int t;
      cin >> t;

      int a = t / 3;
      int b = t % 3;

      int d = a;
      int e = a;
      int f = a;
      
      if (d >= p && d <= 10) {
        cnt++;
        continue;
      }

      if (b > 0) {
        d++;
      }

      if (d >= p && d <= 10) {
        cnt++;
        continue;
      }

      if (s == 0) {
        continue;
      }

      if (b > 1) { // adding another
        d++;
        if (d >= p && d <= 10) {
          s--;
          cnt++;
          continue;
        }
      } else if (b == 0) { // take one
        d++;
        if (d >= p && d <= 10 && f > 0) {
          s--;
          cnt++;
          continue;
        }
      }
    }

    cout << "Case #" << (i+1) << ": " << cnt << endl;
  }

  return 0;
}
