#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

#define sz(c) ((int)(c).size())
#define all(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;

int n;
vector<int> y, ne;

bool solve(int first, int last, int mh)
{
  if (first >= last)
    return true;

  int pos = first;
  for (; pos != last; ++pos)
    if (ne[pos] == last)
      break;
  if (pos == last)
    return false;
  y[pos] = mh;
  if (!solve(pos + 1, last, mh - 1))
    return false;
//  fprintf(stderr, "%d %d %d y[last] = %d y[pos] = %d\n", first, pos, last, y[last],  y[pos]);
  int h = int(y[last] - ll(y[last] - y[pos]) * (last - first) / (last - pos) - 1);
  assert(h >= 0);
  if (!solve(first, pos, min(mh - 1, h)))
    return false;
  return true;
}

void test_case()
{
  if (scanf("%d", &n) != 1) {
    exit(0);
  }
  ne.assign(n, -1);
  y.assign(n, 0);
  for (int i = 0; i < n - 1; ++i)
  {
    scanf("%d", &ne[i]);
    --ne[i];
  }

  int mh = int(1e+9);
  y[n - 1] = mh;
  if (!solve(0, n - 1, mh - 1))
    printf("Impossible\n");
  else
  {
    for (int i = 0; i < n; ++i)
      printf("%d%c", y[i], (i + 1 == n ? '\n' : ' '));
  }
}

int main() {
//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
  int T = 0;
  scanf ("%d", &T);
  for (int ti = 1; ti <= T; ++ti) {
    printf ("Case #%d: ", ti);
    test_case();
  }
  return 0;
}
