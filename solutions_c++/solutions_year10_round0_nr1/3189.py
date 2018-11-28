#include <iostream>

using namespace std;

int main() {
  int T, n, k;
  cin >> T;
  for(int i = 0; i < T; i++) {
    cin >> n >> k;
    cout << "Case #" << i+1 <<": ";
    if((k & ((1 << n) - 1)) == (1 << n) - 1) {
      cout << "ON";
    } else {
      cout << "OFF";
    }
    cout << endl;
  }
  return 0;
}
