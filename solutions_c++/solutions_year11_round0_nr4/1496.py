#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <iomanip>


using namespace std;

int aa[1010];
int main() {
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int j = 1; j <= t; ++j) {
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i)
      cin >> aa[i];
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
      if (aa[i] != i) {
        int t = aa[i];
        while (t != i) {
          ++ans;
          int p = aa[t];
          aa[t] = t;
          t = p;
        }
        ++ans;
        aa[i] = i;
      }
    }
    cout << "Case #" << j << ": " << ans << ".000000" << endl;

  }
  return 0;
}