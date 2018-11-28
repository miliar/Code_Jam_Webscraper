//Authored by dolphinigle
//GCJ Q3 2011
//Jun 4 2011

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

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))
#define RESET(Z,Y) memset(Z,Y,sizeof(Z))

#define SZ(Z) ((int)Z.size())
#define ALL(W) W.begin(), W.end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define INF 1023123123
#define EPS 1e-8

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;
typedef vector<ll> vll;

vint adj[500];
int bfs[500];
pair<int, int> dp[450][450][450];
int done[450][450][450];
int adjm[450][450];

pair<int, int> solve(int node, int prev1, int prev2) {

  if (done[node][prev1][prev2]) return dp[node][prev1][prev2];
  // hitung threaten
  int threaten = 0;
  FORN(i, SZ(adj[node])) {
    int target = adj[node][i];
    if (adjm[prev1][target] || adjm[prev2][target]) continue;
    if (target == prev1 || target == prev2) continue;
    ++threaten;
  }

  if (bfs[node] == 0) {
    // sudah di pojok ei...
    return MP(0, -1 * threaten);
  } else {
    --threaten;
    dp[node][prev1][prev2] = MP(INF, 0);
    FORN(i, SZ(adj[node])) {
      int target = adj[node][i];
      if (bfs[target] != bfs[node] - 1) continue;
      pair<int,int> rec = solve(target, node, prev1);
      MN(dp[node][prev1][prev2], MP(rec.A + 1, -1 * (-rec.B + threaten)));
    }
    done[node][prev1][prev2] = true;
    return dp[node][prev1][prev2];
  }
}

int main() {

  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    printf("Case #%d: ", itc+1);

    int nplanet, nworm;
    cin >> nplanet >> nworm;

    FORN(i, nplanet+1) adj[i] = vint();

    FORN(i, nworm) {
      int x, y;
      scanf("%d,%d", &x, &y);
      adj[x].PB(y);
      adj[y].PB(x);
    }

    FORN(i, nplanet) bfs[i] = -1;
    queue<int> q;
    FORN(i, SZ(adj[1])) {
      bfs[adj[1][i]] = 0;
      q.push(adj[1][i]);
    }

    while (!q.empty()) {
      int top = q.front();
      q.pop();
      FORN(i, SZ(adj[top])) {
        int node = adj[top][i];
        if (bfs[node] == -1) {
          bfs[node] = bfs[top] + 1;
          q.push(node);
        }
      }
    }

    FORN(i, nplanet+2) FORN(j, nplanet+2) adjm[i][j] = 0;
    FORN(i, nplanet) FORN(j, SZ(adj[i])) adjm[i][adj[i][j]] = 1;

    FORN(i, nplanet+2) FORN(j, nplanet+2) FORN(k, nplanet+2) done[i][j][k] = 0;

    pair<int,int> ret = solve(0, nplanet, nplanet);
    cout << ret.A << " " << -ret.B << endl;
  }


  return 0;
}
