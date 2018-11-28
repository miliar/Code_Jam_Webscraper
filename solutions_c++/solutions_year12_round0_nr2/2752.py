#include <iostream>
#include <vector>

using namespace std;

inline int highest_best(int t, int mn_dif, int mx_dif) {
  int ret = -1;
  for (int a = max(0, (t+2)/3-mx_dif); a <= min(10, t/3); ++a) {
    for (int b = max(a, max(t-2*a-mx_dif, t-a-10)); b <= 10 && b <= t-2*a-mn_dif && b <= a+mx_dif && b <= (t-a)/2; ++b) {
      ret = max(ret, t-a-b);
    }
  }
  return ret;
}

int main() {
  vector<int> h_surp(31, -1), h_no_surp(31, -1);
  for (int i = 0; i <= 30; ++i) {
    h_surp[i] = highest_best(i, 2, 2);
    h_no_surp[i] = highest_best(i, 0, 1);
  }
  
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int n, s, p;
    cin >> n >> s >> p;
    int can_surp = 0, can_no_surp = 0, can_both = 0;
    for (int i = 0; i < n; ++i) {
      int t;
      cin >> t;
      if (h_surp[t] >= p && h_no_surp[t] >= p) ++can_both;
      else if (h_surp[t] >= p) ++can_surp;
      else if (h_no_surp[t] >= p) ++can_no_surp;
    }
    int cant = n-can_surp-can_no_surp-can_both;
    if (s <= can_surp) can_surp = s;
    else {
      s -= can_surp;
      if (s <= can_both) can_both = s;
      else {
        s -= can_both;
        if (s > cant) {
          s -= cant;
          can_no_surp -= s;
        }
      }
    }
    int ans = can_surp+can_no_surp+can_both;
    cout << "Case #" << ca << ": " << ans << endl;
  }
}
