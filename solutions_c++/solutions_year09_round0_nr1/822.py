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
#include <cassert>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb push_back
#define mp make_pair

string W[5010];
bool tbl[100][256];

int main() {
  int L, D, N;
  cin >> L >> D >> N;
  rep (i, D) cin >> W[i];

  rep (ca, N) {
    string tmp;
    cin >> tmp;

    memset(tbl, 0, sizeof(tbl));
    int p = 0;
    rep (i, L) {
      if (tmp[p] == '(') {
        p++;
        while (tmp[p] != ')') tbl[i][(int)tmp[p++]] = true;
        p++;
      }
      else {
        tbl[i][(int)tmp[p++]] = true;
      }
    }
    assert(p == (int)tmp.length());

    int ans = 0;
    rep (i, D) {
      rep (j, L) if (!tbl[j][(int)W[i][j]]) goto ng;
      ans++;
    ng:;
    }

    printf("Case #%d: %d\n", ca + 1, ans);
  }
}
