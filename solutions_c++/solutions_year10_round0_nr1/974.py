
#include <iostream>

using namespace std;

int main() {
  int z, N, K;
  cin >> z;
  for (int i = 1; i <= z; i++) {
    cin >> N >> K;
    cout << "Case #" << i << ": " << ((K + 1)%(1 << N) == 0 ? "ON" : "OFF") << "\n";
  }
}
