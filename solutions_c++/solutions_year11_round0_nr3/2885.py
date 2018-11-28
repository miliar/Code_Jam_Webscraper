#include <iostream>
#include <algorithm>
using namespace std;

int N;
int C[1000];
bool use[1000];

int rec(int p) {
  if(p == N) {
    int S[2] = {-1, -1};
    int sum = 0;
    for(int i = 0; i < N; ++i) {
      int k = (int)use[i];
      if(S[k] == -1) S[k] = C[i];
      else           S[k] ^= C[i];
      if(k) sum += C[i];
    }
    return S[0] == S[1] ? sum : -1;
  }

  int res;
  use[p] = false;
  res = rec(p+1);
  use[p] = true;
  res = max(res, rec(p+1));
  return res;
}

main() {
  int T;
  cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    cin >> N;
    for(int i = 0; i < N; ++i) cin >> C[i];
    int ans = rec(0);
    cout << "Case #" << tc << ": ";
    if(ans == -1) cout << "NO" << endl;
    else          cout << ans << endl;
  }
}
