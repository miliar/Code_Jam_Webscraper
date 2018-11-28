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

//#define DBG
int a[3000];
int main() {
#ifdef DBG
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
#endif
  int t;
  cin >> t;
  for (int qq = 1; qq <= t; ++qq) {
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i)
      cin >> a[i];
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
      if (a[i] != i) {
        int t = a[i];
        while (t != i) {
          ++ans;
          int p = a[t];
          a[t] = t;
          t = p;
        }
        ++ans;
        a[i] = i;
      }
    }
    cout << "Case #" << qq << ": " << ans << ".0000000000" << endl;

  }
  return 0;
}