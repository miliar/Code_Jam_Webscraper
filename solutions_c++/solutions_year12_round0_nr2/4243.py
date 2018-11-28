#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, S, p;
    cin >> N >> S >> p;

    int atMostOneBelow = p - 1, atMostTwoBelow = p - 2;
    if (atMostOneBelow < 0) {
      atMostOneBelow = 0;
    }
    if (atMostTwoBelow < 0) {
      atMostTwoBelow = 0;
    }

    int lowestNormal = p + 2 * atMostOneBelow;
    int lowestSurprising = p + 2 * atMostTwoBelow;

    int ans = 0;
    for (int i = 0; i < N; i++) {
      int total;
      cin >> total;
      if (total >= lowestNormal) {
        ans++;
      } else if (total >= lowestSurprising && S > 0) {
        ans++;
        S--;
      }
    }
    cout << "Case #" << t << ": " << ans << '\n';
  }
  return 0;
}
