#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int data[2000];
long long vs[2000];
int add[2000];

int main () {
  int t = 0; cin >> t;
  cin.sync_with_stdio(false);
  for (int _c = 1; _c <= t; _c++) {
    int r, k, n;
    cin >> r >> k >> n;

    long long sum = 0;
    for (int i = 0; i < n; i++) {
      cin >> data[i];
      sum += data[i];
    }

    for (int i = 0; i < n; i++) {
      int j = 0;
      long long v = 0;
      if (k >= sum) v = sum;
      else {
        int ks = k;
        while (ks >= data[(i + j) % n]) {
          int _a = data[(i + j++) % n];
          v += _a;
          ks -= _a;
        }
      }
      vs[i] = v;
      add[i] = j;
    }

    int j = 0;
    sum = 0;
    for (int i = 0; i < r; i++) {
      sum += vs[j];
      j = (j + add[j]) % n;
    }


    cout << "Case #" << _c << ": ";
    cout << sum << endl;
  }

  return 0;
}
