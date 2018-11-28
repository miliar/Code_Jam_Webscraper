#include <iostream>

using namespace std;

int main() {
  int T, N, S, p, g1, g2, x;
  cin >> T;

  for (int i = 1; i <= T; i++) {
    g1 = 0;
    g2 = 0;
    cin >> N >> S >> p;
    int judge1 = 3 * p - 2;
    int judge2 = judge1 - 2;
    for (int j = 0; j < N; j++) {
      cin >> x;
      if (x >= judge1) {
        g1++;
      } else if (x >= 2 && x >= judge2) {
        g2++;
      }
    }
    if (S >= g2) {
      g1 += g2;
    } else {
      g1 += S;
    }
    cout << "Case #" << i << ": ";
    cout << g1; 
    cout << endl;
  }
  return 0;
}
