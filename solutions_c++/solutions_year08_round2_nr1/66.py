#include <vector>
#include <list>
#include <map>
#include <set>
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

int T;

int main() {
  cin >> T;
  for (int nn = 1; nn <= T; nn++) {
    long long n, A, B, C, D, x0, y0, M;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    long long rem[3][3]; memset(rem, 0, sizeof rem);

    long long X = x0, Y = y0;
    rem[X % 3][Y % 3]++;
    for (int i = 1; i <  n; i++) {
      X = (A * X + B) % M;
      Y = (C * Y + D) % M;
      rem[X % 3][Y % 3]++;
    }

    long long res = 0;
    for (int x1 = 0; x1 < 3; x1++) for (int y1 = 0; y1 < 3; y1++)
      for (int x2 = 0; x2 < 3; x2++) for (int y2 = 0; y2 < 3; y2++) {
        long long r1 = rem[x1][y1], r2 = rem[x2][y2], r3;
        int x3 = (6 - x1 - x2) % 3, y3 = (6 - y1 - y2) % 3;
        r3 = rem[x3][y3];
        if (x1 == x2 && y1 == y2) {
          r2 = r1 - 1;
          if (x3 == x2 && y3 == y2) r3 = r2 - 1;
        } else {
          if (x3 == x1 && y3 == y1) r3 = r1 - 1;
          if (x3 == x2 && y3 == y2) r3 = r2 - 1;
        }

        res += r1 * r2 * r3;
      }

    cout << "Case #" << nn << ": " << (res / 6) << endl;
  }
  return 0;
}