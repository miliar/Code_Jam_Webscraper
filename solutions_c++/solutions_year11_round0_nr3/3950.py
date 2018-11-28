#include <iostream>
#include <cstdio>
#include <cmath>
#include <stack>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int bitadd (int a, int b) {
  return (a | b) - (a & b);
}

int reduceadd (vector<int>a) {
  int sum = 0;
  for (int i = -1; ++i < a.size() ; ) {
    sum = bitadd(sum, a[i]);
  }
  return sum;
}

int sum (vector<int>a) {
  int sum = 0;
  for (int i = -1; ++i < a.size() ; ) {
    sum = sum + a[i];
  }
  return sum;
}

void printvector (vector<int> a) {
  for (int i = -1; ++i < a.size() ; ) {
    cout << a[i] << ",";
  }
  cout << endl;
}



void solve (int* a, int n) {
  sort(a, a + n);
  int m = 0;
  int r;
  for (int i = -1; ++i < (1 << (n - 0)); ) {
    vector<int> p, q;
    for (int j = -1; ++j < n; ) {
      if ((1 << j) & i) p.push_back(a[j]);
      else q.push_back(a[j]);
    }
    if ((r = reduceadd(p)) == reduceadd(q) && r != 0) m = max(m, max(sum(p), sum(q)));
  }
  if (m == 0) cout << "NO";
  else cout << m;
}

int main () {
  int i = 0, j = 0, k = 0, l = 0;
  double x = 0, y = 0, z = 0;
  int a[10000];

  cin >> i;

  while (cin >> j) {
    for (k = -1; ++k < j; ) cin >> a[k];
    cout << "Case #" << ++l << ": ";
    solve(a, k);
    cout << endl;
  }

}

