#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main() {
  int T;
  int N, K;
  cin >> T;
  for (int test = 1; test <= T; test++) {
    cin >> N >> K;
    cout << "Case #" << test << ": ";
    unsigned int mod = 1 << N;
    K %= mod;
    if (K == mod - 1) {
      cout << "ON" << endl;
    }
    else {
      cout << "OFF" << endl;
    }
  }
  return 0;
}
