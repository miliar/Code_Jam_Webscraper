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
int main() {
#ifdef DBG
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
#endif
  int t;
  cin >> t;
  for (int qq = 1; qq <= t; ++qq) {
    int n, x;
    cin >> n;
    vector <int> a;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
      cin >> x;
      sum += x;
      a.push_back(x);
    }
    int k = 0;
    for (int i = 0; i < n; ++i)
      k = k^a[i];
    cout << "Case #" << qq << ": ";
    if (k != 0) {
      cout << "NO";
    } else {
      sort(a.begin(), a.end());
      sum -= a[0];
      cout << sum;
    }
    cout << endl;
  }
  return 0;
}