#include <iostream>

using namespace std;

int main() {
  int A[32], a[32];
  for (int i = 1; i < 31; i++) {
    A[i] = 1 << i;
    a[i] = A[i] - 1;
  }
  int T, N, K;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cin >> N >> K;
    cout << "Case #" << i << ": ";
    if ((K - a[N]) % A[N] == 0)
      cout << "ON";
    else
      cout << "OFF";
    cout << endl;
  }
  return 0;
}
