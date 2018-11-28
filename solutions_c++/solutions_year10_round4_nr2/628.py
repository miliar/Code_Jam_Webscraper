#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int p;
int data[1000000];

int main() {
  int _t; cin >> _t;
  for (int _tt = 1; _tt <= _t; _tt++) {
    cout << "Case #" << _tt << ": ";
    cin >> p;
    for (int i = 0; i < (1 << p); i++)
      cin >> data[i];

    int tmp;
    for (int i = p - 1; i >= 0; i--)
      for (int j = 0; j < (1 << i); j++)
        cin >> tmp;

    int res = 0;
    int v = 1;
    for (int i = p - 1; i >= 0; i--) {
      for (int j = 0, c = 0; j < (1 << i); j++, c += 2 * v) {
        int a = data[c];
        int b = data[c + v];
        int r = min(a, b);

        if (!r) res++;
        else r--;

        data[c] = r;
      }
      v *= 2;
    }

    cout << res << endl;

  }

  return 0;
}