#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {

  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N, S, p;
    cin >> N >> S >> p;
    vector<int> v(N);
    for (int i = 0; i < N; ++i) {
      cin >> v[i];
    }
    int foo = 0;
    int bar = 0;
    for (int i = 0; i < N; ++i) {
      if ((v[i] + 2) / 3 >= p) {
        ++foo;
      }
      else if ((v[i] + 4) / 3 >= p && v[i] != 0) {
        ++bar;
      }
    }
    int ans = foo + min(bar, S);
    cout << "Case #" << t << ": " << ans << endl;
  }

  return 0;

}
