#include <cstdio>
#include <ctime>

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

const int maxn = (int)2e+6 + 1;
int factor[maxn] = {1, };

inline int next( int x, int shift_factor ) {
  return shift_factor * (x % 10) + x / 10;
}

int main()
{
  long st = clock();
  for (int x = 1; x < maxn; x *= 10) {
    int lastx = min(maxn, 10 * x);
    for (int i = x; i < lastx; ++i) {
      factor[i] = x;
    }
  }

  int T;
  cin >> T;
  vector<int> id(maxn, -1);
  for (int ti = 1; ti <= T; ++ti) {
    fill(id.begin(), id.end(), -1);

    int a, b;
    cin >> a >> b;

    int next_id = 0;
    long long ans = 0;
    for (int x = a; x <= b; ++x) {
      if (id[x] == -1) {
        int shift_factor = factor[x];
        int lastx = x;
        int cnt = 0;
        while (true) {
          if (a <= x && x <= b) {
            id[x] = next_id;
            ++cnt;
          }

          if ((x = next(x, shift_factor)) == lastx) {
            break;
          }
        }

        ++next_id;
        ans += (long long)cnt * (cnt - 1) / 2;
      }
    }

    cout << "Case #" << ti << ": " << ans << "\n";
    fprintf(stderr, "#%0d time: %.2lf\n", ti, (double)(clock() - st) / CLOCKS_PER_SEC);
  }

  return 0;
}
