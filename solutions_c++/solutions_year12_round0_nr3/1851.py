#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main() {

  int T;
  cin >> T;
  for (int CASE = 1; CASE <= T; CASE++) {
    int A, B;
    int res = 0;
    cin >> A >> B;
    vector<bool> met(B+1, false);
    for (int v = A; v <= B; v++) if (!met[v]) {
      int lower_bound = 1;
      for (int t = v; t >= 10; t /= 10, lower_bound *= 10);
      set<int> nums { v };
      for (int mod = 10, shift = lower_bound; mod <= lower_bound; mod *= 10, shift /= 10) {
        int nv = v / mod + (v % mod) * shift;
        if (nv >= lower_bound && nv >= A && nv <= B) {
          nums.insert(nv);
          met[nv] = true;
        }
      }
      res += nums.size() * (nums.size() - 1) / 2;
    }
    cout << "Case #" << CASE << ": " << res << endl;
  }

  return 0;
}
