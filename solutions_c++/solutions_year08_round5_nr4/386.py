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
  for (int _caseN = 1; _caseN <= T; _caseN++) {
    int H, W, R; cin >> H >> W >> R;
    bool bad[200][200]; memset(bad, 0, sizeof bad);
    for (int i = 0; i < R; i++) {
      int r, c; cin >> r >> c;
      bad[c - 1][r - 1] = true;
    }

    int data[200][200]; memset(data, 0, sizeof data);
    data[0][0] = 1;
    for (int line = 0; ; line++) {
      bool ok = false;
      int x = line, y = 0;
      while (x >= 0) {
        if (x < W && y < H && !bad[x][y]) {
          ok = true;
          data[x + 1][y + 2] = (data[x + 1][y + 2] + data[x][y]) % 10007;
          data[x + 2][y + 1] = (data[x + 2][y + 1] + data[x][y]) % 10007;
        }
        x--; y++;
      }
      if (!ok) break;
    }
    

    cout << "Case #" << _caseN << ": ";
     cout << data[W - 1][H - 1];
    cout << endl;
  }

  return 0;
}