#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <utility>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

typedef pair<int, int> PII;
typedef long long ll;
typedef vector<ll> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;

int n;

bool be(int row, ll num) {
  if (((ll(1)<<ll(n-row-1))-1) & num)
    return false;
  return true;
}

int main() {
  int tt;
  cin >> tt;
  for (int t=1; t<=tt; ++t) {
    cout << "Case #" << t << ": ";
    cin >> n;
    VI v(n, 0);
    for (int i=0; i<n; ++i) {
      string s;
      cin >> s;
      for (int j=0; j<n; ++j)
        if (s[j] == '1')
          v[i] |= (1<<(n-j-1));
    }
    int passos = 0;
    for (int i=0; i<n-1; ++i)
        for (int j=i+1; j<n; ++j)
          if (not be(i, v[i]) and be(i, v[j])) {
            for (int k=j; k>i; --k)
              swap(v[k], v[k-1]);
            passos += j-i;
          }
    cout << passos << endl;
  }
}