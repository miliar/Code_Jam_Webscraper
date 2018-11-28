#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int sol[1000010];

bool win(int lo, int hi) {
  vector<int> v;
  while(lo) {
    int m = hi / lo;
    v.push_back(m);
    hi -= lo * m;
    swap(lo, hi);
  }
  bool w = v.back() > 1;
  for(int i = v.size() - 2; i >= 0; i--) {
    if(v[i] == 1) {
      w = !w;
    } else {
      w = true;
    }
  }
  return w;
}

int solve(int lo, int hi, int x) {
  if(x < lo) return hi - lo + 1;
  if(hi < x) return 0;
  return hi - x + 1;
}

int main() {
/*
  for(int i = 1; i < 70; i++) {
    for(int j = 1; j < 70; j++) {
      cout << (win(min(i, j), max(i, j)) ? 1 : 0);
    }
    cout << endl;
  }
*/

  for(int mn = 1; mn <= 1000000; mn++) {
    int lo = mn + 1;
    int hi = 1000001;
    while(lo < hi) {
      int md = (lo + hi) / 2;
      if(win(mn, md)) {
        hi = md;
      } else {
        lo = md + 1;
      }
    }
    sol[mn] = lo;
  }

  int T; cin >> T;
  for(int t = 1; t <= T; t++) {
    int A1, A2, B1, B2;
    cin >> A1 >> A2 >> B1 >> B2;
    long long res = 0;
    for(int a = A1; a <= A2; a++) res += solve(B1, B2, sol[a]);
    for(int b = B1; b <= B2; b++) res += solve(A1, A2, sol[b]);
    cout << "Case #" << t << ": " << res << endl;
  }
}
