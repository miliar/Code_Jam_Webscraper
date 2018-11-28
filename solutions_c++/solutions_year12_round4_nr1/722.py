// A.cc
// Wentao Han (wentao.han@gmail.com)

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int x = 1; x <= T; x++) {
    int N;
    cin >> N;
    vector<int> d(N);
    vector<int> l(N);
    for (int i = 0; i < N; i++) {
      cin >> d[i] >> l[i];
    }
    int D;
    cin >> D;
    vector<int> m(N, 0);
    m[0] = d[0];
    bool success = false;
    for (int i = 0; i < N; i++) {
      if (d[i] + m[i] >= D) {
        success = true;
        break;
      }
      for (int j = i + 1; j < N && d[j] <= d[i] + m[i]; j++) {
        int t = min(d[j] - d[i], l[j]);
        m[j] = max(m[j], t);
      }
    }
    cout << "Case #" << x << ": " << (success ? "YES" : "NO") << endl;
  }
}
