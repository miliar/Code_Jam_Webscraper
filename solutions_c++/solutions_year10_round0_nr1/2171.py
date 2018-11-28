#include <iostream>

using namespace std;

int main () {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    unsigned int N, K;
    cin >> N >> K;
    unsigned int pow = 1 << N;
    if ((K + 1) % pow == 0 && K > 0) {
      cout << "Case #" << i + 1 << ": ON" << endl;
    } else {
      cout << "Case #" << i + 1 << ": OFF" << endl;
    }
  }
  return 0;
}

