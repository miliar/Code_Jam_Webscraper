//Authored by dolphinigle
//Google Code Jam Qual 1
//May 21

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
#include <assert.h>

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

vint adj[2200];

int n,m;

void clear_all() {
  FORN(i, 2200) adj[i].clear();
}

int compute_dif(int dulu, int sekarang) {
  // rumus = dulu - sekarang
  if (dulu >= sekarang) return dulu - sekarang;
  return dulu + n - sekarang;
}

int mc = 0;
int color[2200];

vector< vector<int> > cycles;

pair<int,int> getAdj(int node1, int node2) {
  int firstmatch = -1;
  int secmatch = -1;
  FORN(i, SZ(cycles)) {
    FORN(j, SZ(cycles[i])) {
      int k = (j+1)%SZ(cycles[i]);
      if ((cycles[i][j] == node1 && cycles[i][k] == node2) ||
          (cycles[i][j] == node2 && cycles[i][k] == node1)) {
        if (firstmatch == -1) firstmatch = i; else secmatch = i;
        break;
      }
    }
  }
  return MP(firstmatch, secmatch);
}

void solve(int cyc_cnt, int from) {
  // cout << cyc_cnt << " " << from << endl;
  vint c = cycles[cyc_cnt];
  FORN(i, SZ(c)) if (color[c[i]] != -1 && color[c[(i+1)%SZ(c)]] != -1) {
    // found
    //cout << c[i] << " " << c[(i+1)%SZ(c)] << endl;

    vint awalcc(mc, 0);
    FORN(j, SZ(c)) if (color[c[j]] != -1) awalcc[color[c[j]]]++;

    vint colorcand;
    FORN(j, mc) if (awalcc[j] == 0) colorcand.PB(j);

    int pos = (i+2)%SZ(c);
    // cout << c[pos] << endl;
    int lastcolor = color[c[(i+1)%SZ(c)]];
    FORN(j, SZ(c)-3) {
      lastcolor += 1;
      lastcolor %= mc;
      if (!colorcand.empty()) {
        lastcolor = colorcand.back();
        colorcand.pop_back();
      }
      color[c[pos]] = lastcolor;
      ++pos;
      pos %= SZ(c);
    }

    int lastpos = pos-1;
    if (pos < 0) pos += SZ(c);

    vint occ(mc, 0);
    FORN(j, SZ(c)) if (color[c[j]] != -1) occ[color[c[j]]]++;

    FORN(j, mc) if (j != color[c[lastpos]] && j != color[c[i]]) {
      color[c[pos]] = j;
      if (occ[j] == 0) break;
    }

    FORN(j, SZ(c)) {
      if (c[(j+1)%SZ(c)] == (c[j] + 1) % n) continue;
      pair<int,int> pii = getAdj(c[(j+1)%SZ(c)], c[j]);
      if (pii.A != cyc_cnt && pii.A != from) solve(pii.A, cyc_cnt);
      if (pii.B != cyc_cnt && pii.B != from) solve(pii.B, cyc_cnt);
    }

    break;
  }
}

int done[2200][2200];

int main() {

  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    printf("Case #%d: ", itc + 1);
    cin >> n >> m;

    clear_all();

    vint startnodes;

    FORN(i, m) {
      int s;
      cin >> s;
      --s;
      startnodes.PB(s);
    }
    FORN(i, m) {
      int e;
      cin >> e;
      --e;
      adj[startnodes[i]].PB(e);
      adj[e].PB(startnodes[i]);
    }

    // compute the cycles
    cycles.clear();

    FORN(i, n) FORN(j, n) done[i][j] = 0;

    FORN(i, n) {
      adj[i].PB((i+1)%n);
      adj[i].PB((i+n-1)%n);
    }

    FORN(i, n) FORN(z, SZ(adj[i])) {
      int k = adj[i][z];
      if (i == (k+1)%n) continue;
      if (done[i][k]) continue;
      done[i][k] = 1;
      int pos = k;
      int from = i;
      vint newcyc;
      newcyc.PB(i);
      while (pos != i) {
        newcyc.PB(pos);
        // determine the next one
        int best = (pos+1)%n;
        FORN(j, SZ(adj[pos])) {
          if (adj[pos][j] == from) continue;
          if (compute_dif(from, best) > compute_dif(from, adj[pos][j])) {
            best = adj[pos][j];
          }
        }
        from = pos;
        pos = best;
        done[from][pos] = 1;
      }
      cycles.PB(newcyc);

      /*FORN(j, SZ(newcyc)) {
        cout << newcyc[j] << " ";
      }
      cout << endl;*/
    }

    FORN(i,n) color[i] = -1;
    mc = INF;
    FORN(i, SZ(cycles)) MN(mc, SZ(cycles[i]));

    FORN(i, SZ(cycles)) if (SZ(cycles[i]) == mc) {
      // do here

      color[cycles[i][0]] = 0;
      color[cycles[i][1]] = 1;
      solve(i, -1);

      break;
    }

    // verifier
    FORN(i, SZ(cycles)) {
      vint ccc(mc, 0);
      FORN(j, SZ(cycles[i])) ccc[color[cycles[i][j]]]++;
      FORN(j, mc) if (ccc[j] == 0) {
        cout << "test case " << itc+1 << " failed\n";
      }
    }

    cout << mc << endl;
    FORN(i, n) {
      if (i) printf(" ");
      printf("%d", color[i] + 1);
    }
    cout << endl;

  }

  return 0;
}

