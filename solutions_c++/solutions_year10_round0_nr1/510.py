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

int main () {
  int t = 0; cin >> t;
  for (int _c = 1; _c <= t; _c++) {
    int n, k; cin >> n >> k;

    cout << "Case #" << _c << ": ";
    int m = k & ((1 << n) - 1);
    if (m == ((1 << n) - 1))
      cout << "ON";
    else
      cout << "OFF";
    cout << endl;
  }

  return 0;
}
