// Solution made by Peter Zeman.
// {{{
// vim:filetype=cpp foldmethod=marker foldmarker={{{,}}}
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
#define debug(x) cout << ">>> " << x << endl;
// }}}

bool recycled(int n, int m)
{
  int a = 10, b = 1;
  while (b < m) b *= 10;
  b /= 10;
  while (b != 1) {
    if (n % a == m / b && n / a == m % b) return true;
    a *= 10;
    b /= 10;
  }
  return false;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int A, B, ans = 0;
    scanf("%d%d", &A, &B);
    for (int n = A; n <= B; n++)
      for (int m = n + 1; m <= B; m++)
        if (recycled(n, m)) ans++;
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
