#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

bool is_reversed(const string &n) {
  for (int i = 1; i < n.size(); ++i)
    if (n[i] > n[i-1]) return false;
  return true;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string N;
    cin >> N;
    cout << "Case #" << t << ": ";
    if (is_reversed(N)) {
      N += "0";
      sort(N.begin(), N.end());
      for (int i = 0; i < N.size(); ++i) {
        if (N[i] != '0') {
          N[0] = N[i];
          N[i] = '0';
          break;
        }
      }
      cout << N << endl;
    } else {
      next_permutation(N.begin(), N.end());
      cout << N << endl;
    }
  }

  return 0;
}
