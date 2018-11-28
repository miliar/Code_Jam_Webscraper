#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    int n;
    cin >> n;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int e;
      cin >> e;
      if (e != i+1) ++ans;
    }
    cout << "Case #" << ca << ": " << ans << endl;
  }
}
