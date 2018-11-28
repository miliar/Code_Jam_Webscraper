#include <iostream>
#include <cstring>
using namespace std;

long long a[2020], h[2020];
bool seen[2020];

bool verify(int n) {
  bool res = true;
  for (int i = 0; i < n-1; i++) {
    int see = i+1;
    for (int j = i+2; j < n; j++)
      if ((h[j]-h[i])*(see-i) > (h[see]-h[i])*(j-i))
        see = j;
    if (see != a[i]) {
      // cout << "PEAK " << i << " SEES " << see << " INSTEAD OF " << a[i] << endl;
      res = false;
    }
  }
  return res;
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n; cin >> n;
    memset(seen, 0, sizeof(seen));
    for (int i = 0; i < n-1; i++) { cin >> a[i]; a[i]--; seen[a[i]] = true; }

    memset(h, 0, sizeof(h));
    bool poss = true;
    int slope = 10000;
    for (int i = n-2; i >= 0; i--) {
      h[i] = h[i+1] + slope;
      for (int j = i+1; j < a[i]; j++)
        h[i] = max(h[i], (h[j]*a[i]-h[a[i]]*j+h[a[i]]*i-h[j]*i + a[i]-j) / (a[i]-j));

      slope--;
    }

    if (!verify(n)) cout << "Case #" << c << ": Impossible" << endl;
    else {
      cout << "Case #" << c << ":";
      for (int i = 0; i < n; i++) cout << " " << h[i];
      cout << endl;
    }
  }
  return 0;
}
