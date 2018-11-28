#include <iostream>
#include <cstdio>

#define DBG(x) cout << #x << " = " << x << endl

using namespace std;

int main() {
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  int tests;
  cin >> tests;
  for (size_t z = 1; z <= tests; ++z) {
    int N, K;
    cin >> N >> K;
    int mask = (1 << N) - 1;
    cout << "Case #" << z << ": ";
    if ((K & mask) == mask) {
      cout << "ON";
    } else {
      cout << "OFF";
    }
    cout << endl;
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
