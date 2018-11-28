#include <iostream>
#include <vector>

using namespace std;

const int INF = 1000000000;

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    int n;
    cin >> n;
    int mnc = INF, wsum = 0, sum = 0;
    for (int i = 0; i < n; ++i) {
      int c;
      cin >> c;
      sum += c;
      wsum ^= c;
      if (c < mnc) mnc = c;
    }
    cout << "Case #" << ca << ": ";
    if (wsum != 0) cout << "NO" << endl;
    else cout << sum-mnc << endl;
  }
}
