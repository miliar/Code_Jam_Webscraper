#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int n, k;
    cin >> n >> k;
    k++;
    k %= 1 << n;
    cout << "Case #" << t << ": " << (k ? "OFF" : "ON") << endl;
  }
}
