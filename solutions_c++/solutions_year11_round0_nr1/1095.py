#include <iostream>
#include <vector>

using namespace std;

int abs(int n) {
  if (n < 0) return -n;
  return n;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    int n;
    cin >> n;
    vector<int> pp(2, 1), pt(2, 0);
    int t = 0;
    for (int i = 0; i < n; ++i) {
      char R;
      int r, p;
      cin >> R >> p;
      if (R == 'B') r = 0;
      else r = 1;
      t = max(t, pt[r]+abs(pp[r]-p));
      ++t;
      pp[r] = p;
      pt[r] = t;
    }
    cout << "Case #" << ca << ": " << t << endl;
  }
}
