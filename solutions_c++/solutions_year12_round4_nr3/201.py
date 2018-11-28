#include <iostream>
#include <iomanip>
#include <queue>
#include <cassert>

using namespace std;

const int MAXN = 2005;

int n, a[MAXN], b[MAXN], lim[MAXN], num[MAXN];

void solve() {
  cin >> n;
  for (int i = 0; i < n - 1; i++) {
    cin >> a[i];
    a[i]--;
  }

  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < a[i]; j++) {
      if (a[j] > a[i]) {
        cout << "Impossible\n";
        return;
      }
    }
  }

  for (int i = 0; i < n; i++)
    num[i] = 0;
  for (int i = 0; i < n; i++)
    num[a[i]]++;

  lim[n - 1] = MAXN;
  b[n - 1] = 1000000000;

  for (int i = n - 2; i >= 0; i--) {
    b[i] = b[a[i]] - lim[a[i]] * (a[i] - i);
    int old = lim[a[i]];
    lim[a[i]] = old - 1;
    lim[i] = old + num[i];
  }

  for (int i = 0; i < n; i++) {
    if (i > 0) cout << " ";
    cout << b[i];
  }
  cout << "\n";


  for (int i = 0; i < n - 1; i++) {
    int best = i + 1;
    for (int j = i + 1; j < n; j++) { 
      if ((long long)(b[j] - b[i]) * (long long)(best - i) > (long long)(b[best] - b[i]) * (long long)(j - i)) {
        best = j;
      }
    }
    if (best != a[i]) {
      cerr << "ERR";
      cerr << i << " " << best << " " << a[i] << "\n";
    }
    if (b[i] < 0) {
      cerr << "UNDER";
      cerr << i << " " << b[i] << "\n";
    }
  }

}

int main() {
  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
}




