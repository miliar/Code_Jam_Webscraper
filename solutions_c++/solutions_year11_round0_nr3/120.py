#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int T; cin >> T;
  for (int cNum = 1; cNum <= T; ++cNum) {
    int N; cin >> N;

    int runXOR = 0, total = 0, minC = 10000001;

    for (int i = 0; i < N; ++i) {
      int c; cin >> c;
      runXOR ^= c;
      total += c;
      minC = min(minC, c);
      }

    cout << "Case #" << cNum << ": ";
    if (runXOR)
      cout << "NO\n";
    else
      cout << (total - minC) << '\n';

    }
  }
