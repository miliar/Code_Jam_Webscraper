#include <iostream>
#include <vector>

using namespace std;

vector<int> a;

int main() {
  int tests;
  cin >> tests;
int n;
  for (int test = 0; test < tests; ++test) {
    cin >> n;
    a.resize(n);
    for (int i = 0; i  <n; ++i)
      cin >> a[i];

    int s1, s2, S;
    int ans = -1;
    for (int i = 1; i < (1<<n)-1; ++i) {
      s1 = s2 = S = 0;
      for (int j = 0; j < n; ++j) {
        if ((i>>j)&0x01) {
          s1 ^= a[j];
          S += a[j];
        } else
          s2 ^= a[j];
      }
      if (s1 == s2)
        ans = max(ans, S);
    }
    if (ans < 0)
      cout << "Case #" << test+1 << ": NO" << endl;
    else
      cout << "Case #" << test+1 << ": " << ans << endl;
  }
  return 0;
};
