#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int T;
  cin >> T;

  int P[100];
  char R[100];

  int N;
  for (int i = 0; i < T; i++) {
    cin >> N;
    for (int j = 0; j < N; j++) {
      cin >> R[j] >> P[j];
    }

    int total = 0;
    int blue = 1;
    int orange = 1;
    int last = -1;
    int dist = -1;
    for (int j = 0; j < N; j++) {

      dist = abs(P[j] - (R[j] == 'O' ? orange : blue));
      if (j != 0 && R[j] != R[j-1]) {
        int mth = max(dist - last, 0) + 1;
        last = mth;
        total += last;

        if (R[j] == 'O') {
          orange = P[j];
        } else {
          blue = P[j];
        }

        continue;
      }

      if (j == 0) {
        last = dist + 1;
      } else {
        last += dist + 1;
      }
      total += dist + 1;

      if (R[j] == 'O') {
        orange = P[j];
      } else {
        blue = P[j];
      }
    }

    cout << "Case #" << (i + 1) << ": " << total << endl;
  }

  return 0;
}
