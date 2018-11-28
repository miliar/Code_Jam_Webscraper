#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
 
typedef long long ll;

const int INF = 999999999;

map<string, int> cur;

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int S, Q;
    scanf("%d ", &S);

    cur.clear();

    rep (i, S) {
      string tmp;
      getline(cin, tmp);
      cur.insert(mp(tmp, 0));
    }

    scanf("%d ", &Q);

    rep (i, Q) {
      string tmp;
      getline(cin, tmp);

      int mi = INF;
      tr (cur, ite) {
        if (ite->first != tmp) mi <?= ite->second;
      }
      cur[tmp] = mi + 1;
    }

    
    int ans = INF;
    tr (cur, ite) ans <?= ite->second;
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
