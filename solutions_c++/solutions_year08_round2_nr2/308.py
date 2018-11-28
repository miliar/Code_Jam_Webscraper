#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cmath>
#include <cctype>

#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

#define FOREACH(iter, cont) for(__typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
#define FOR(i, begin, end) for(int i = (begin); i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

const int maxn = 1000010;

vector<int> s[maxn];

bool vis[maxn];

void dfs(int x) {
  vis[x] = true;
  FOREACH(y, s[x])
    if (!vis[*y])
      dfs(*y);
}

int main() {
  int cases;
  cin >> cases;
  for (int cs = 1; cs <= cases; cs++) {
    long long a, b, k;
    cin >> a >> b >> k;

    int n = b-a+1;
    FOR(i, 0, n)
      s[i].clear();


    for (long long p = k; p+a <= b; p++) {
      bool prime = true;
      for (int i = 2; i*i <= p; i++)
        if (p % i == 0) {
          prime = false;
          break;
        }
      if (prime) {
        long long x = (a/p)*p;
        while (x < a)
          x += p;
        while (x+p <= b) {
          s[x-a].push_back(x+p-a);
          s[x+p-a].push_back(x-a);
          x += p;
        }
      }
    }

    CLEAR(vis);
    int r = 0;
    FOR(i, 0, n)
      if (!vis[i]) {
        r++;
        dfs(i);
      }

    cout << "Case #" << cs << ": " << r << endl;
  }
}
