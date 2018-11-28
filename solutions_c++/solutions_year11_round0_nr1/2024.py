#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  freopen("output.txt", "w", stdout);
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int n;
    cin >> n;
    int time = 0;
    int lastO = 0, lastB = 0, O = 1, B = 1;
    for (int i = 0; i < n; ++i) {
      char c;
      cin >> c;
      int k;
      cin >> k;
      if (c == 'B') {
        time = max(time, lastB + abs(B - k));
        ++time;
        lastB = time;
        B = k;
      } else {
        time = max(time, lastO + abs(O - k));
        ++time;
        lastO = time;
        O = k;
      }
    }

    cout << "Case #" << t << ": " << time << endl;
  }
}