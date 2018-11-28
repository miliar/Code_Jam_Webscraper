#include <iostream>
#include <vector>
using namespace std;

vector<int> recycle(int k) {
  vector<int> ret;
  int m = 10;
  while (m <= k) {
    m *= 10;
  }
  if (k >= 10) {
    int p = k % 10;
    p = p * (m / 10) + k / 10;
    if (p > k && p >= m / 10) {
      ret.push_back(p);
    }
  }
  if (k >= 100) {
    int p = k % 100;
    p = p * (m / 100) + k / 100;
    if (p > k && p >= m / 10) {
      ret.push_back(p);
    }
  }
  return ret;
}

vector<vector<int> > f(1001);

int main() {
  for (int i = 1; i <= 1000; ++i) {
    f[i] = recycle(i);
    continue;
    cerr << i;
    for (int j = 0; j < f[i].size(); j++)
      cerr << '\t' << f[i][j];
    cerr << endl;
  }

  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    int a, b;
    cin >> a >> b;
    int s = 0;
    for (int j = a; j <= b; ++j) {
      for (int k = 0; k < f[j].size(); k++) {
        if (f[j][k] <= b) {
          s++;
        }
      }
    }
    cout << "Case #" << i << ": " << s << endl;
  }
  return 0;
}
