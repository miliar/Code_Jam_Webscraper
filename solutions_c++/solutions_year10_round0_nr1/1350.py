#include <iostream>


using namespace std;


int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; ++i) {
    int N, K;
    cin >> N >> K;
    cout << "Case #" << i+1 << ": ";

    if (K % (1 << N) == (1 << N) - 1) {
      cout << "ON";
    } else {
      cout << "OFF";
    }
    cout << "\n";
  }

  return 0;
}
