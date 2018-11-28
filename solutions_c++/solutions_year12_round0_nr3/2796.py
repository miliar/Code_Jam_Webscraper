#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int MIN_A = 1;
const int MAX_B = 2000000;

int p10[9];

int digits(int n) {
  int ret = 1;
  for (; n >= 10; n /= 10) {
    ++ret;
  }
  return ret;
}

inline int back_to_front(int n, int m) {
  return (n%p10[m])*p10[digits(n)-m]+n/p10[m];
}

int main() {
  p10[0] = 1;
  for (int i = 1; i < 9; ++i) {
    p10[i] = 10*p10[i-1];
  }
  
  vector<vector<int> > recycled(MAX_B+1);
  for (int n = 1; n <= MAX_B; ++n) {
    for (int i = 1; i < digits(n); ++i) {
      int m = back_to_front(n, i);
      if (n < m && m <= MAX_B) {
        recycled[n].push_back(m);
      }
    }
    sort(recycled[n].begin(), recycled[n].end());
    recycled[n].resize(unique(recycled[n].begin(), recycled[n].end())-recycled[n].begin());
  }
  
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int A, B;
    cin >> A >> B;
    int ans = 0;
    for (int n = A; n <= B; ++n) {
      ans += int(upper_bound(recycled[n].begin(), recycled[n].end(), B)-recycled[n].begin());
    }
    cout << "Case #" << ca << ": " << ans << endl;
  }
}
