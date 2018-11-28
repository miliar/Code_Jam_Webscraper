#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <sys/time.h>
#include <regex.h>

using namespace std;

#define DEBUG(x) cout << #x << ": " << x << endl

#define sz(a) int((a).size())

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define REPD(i,n) for(int i=(n)-1;i>=0;--i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACHD(it,c) for(typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)

#define ALL(c) (c).begin(),(c).end()

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

typedef pair<int,int> II;

typedef long long llong;

// twice SIGNED area of triangle represented by points a, b, c
long long area2( long long ax, long long ay,
                 long long bx, long long by,
                 long long cx, long long cy ) {
   return ax * by - ay * bx +
          ay * cx - ax * cy +
          bx * cy - cx * by;
}

struct Node {
   int leaf;
   int gate;
   bool changeable;
   Node(int _leaf, int _gate, int _change)
     : leaf(_leaf), gate(_gate), changeable(_change) {}
   Node() {}
};

#define INF 10000000

vector<Node> nodes;
int M;

int rec(int n, int v) {
   if (nodes[n].leaf >= 0)
      return v == nodes[n].leaf ? 0 : INF;

   int l0 = rec(n*2, 0);
   int l1 = rec(n*2, 1);

   int r0 = rec(n*2 + 1, 0);
   int r1 = rec(n*2 + 1, 1);

   if (v) {
      if (nodes[n].gate) {
         int res = l1 + r1;
         if (nodes[n].changeable)
            res = min(res, 1+min(l0 + r1, l1 + r0));
         return res;
      }
      else {
         return min(l1, r1);
      }
   }
   else {
      if (nodes[n].gate) {
         return min(l0, r0);
      }
      else {
         int res = l0 + r0;
         if (nodes[n].changeable)
            res = min(res, 1+min(l0 + r1, l1 + r0));
         return res;
      }
   }
}

int main(int argc, char *argv[]) {
   int TC;
   cin >> TC;

   for (int tc = 1; tc <= TC; ++tc) {
      int V;
      cin >> M >> V;
      nodes.clear();
      nodes.push_back(Node());
      REP(i,(M-1)/2) {
         int G, C;
         cin >> G >> C;
         nodes.push_back( Node(-1, G, C) );
      }
      REP(i,(M+1)/2) {
         int leaf;
         cin >> leaf;
         nodes.push_back( Node(leaf, 0, 0) );
      }
      int res = rec(1, V);
      if (res >= INF)
         cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
      else
         cout << "Case #" << tc << ": " << res << endl;
   }

   return 0;
}
