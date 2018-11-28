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


int main() {
  int T;
  scanf("%d", &T);
  
  rep (t, T) {
    int R, K, N, G[1010];
    
    scanf("%d%d%d", &R, &K, &N);
    rep (i, N) scanf("%d", &G[i]);

    int memr[1010];
    ll mems[1010];
    memset(memr, -1, sizeof(memr));
    memset(mems, -1, sizeof(mems));

    ll r = 0, h = 0, s = 0;
    while (r < R) {
      if (memr[h] != -1) break;
      memr[h] = r;
      mems[h] = s;

      int x = 0, i;
      for (i = 0; i < N; i++) {
        int j = (h + i) % N;
        if (x + G[j] > K) break;
        x += G[j];
      }
      
      h = (h + i) % N;
      s += x;
      r++;
    }

    ll cr = r - memr[h];
    ll m = (R - r) / cr;

    r += cr * m;
    s += (s - mems[h]) * m;

    while (r < R) {
      int x = 0, i;
      for (i = 0; i < N; i++) {
        int j = (h + i) % N;
        if (x + G[j] > K) break;
        x += G[j];
      }
      
      h = (h + i) % N;
      s += x;
      r++;
    }

    printf("Case #%d: %lld\n", t + 1, s);
  }
  
  return 0;
}
