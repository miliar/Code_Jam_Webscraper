#include <iostream>
using namespace std;

int main() {
  int T, N, K;
  cin >> T;
  for(int i = 1 ; i <= T ; i++) {
    cin >> N;
    cin >> K;
    cout << "Case #" << i << ": ";
    if(K % (1 << N) == (1 << N) - 1)
      cout << "ON";
    else
      cout << "OFF";
    cout << endl;
  }
  return 0;
}
