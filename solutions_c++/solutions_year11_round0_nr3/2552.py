#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int T;
  cin >> T;

  int C[1000];

  for (int i = 0; i < T; i++) {
    cout << "Case #" << (i + 1) << ": ";

    int N;
    cin >> N;

    int xval = 0;
    for (int j = 0; j < N; j++) {
      cin >> C[j];
      xval ^= C[j];
    }

    if (xval != 0) {
      cout << "NO" << endl;
      continue;
    }

    int m = C[0];
    int total = C[0];

    for (int j = 1; j < N; j++) {
      m = min(m, C[j]);
      total += C[j];
    }

    cout << (total - m) << endl;
  }

  return 0;
}

