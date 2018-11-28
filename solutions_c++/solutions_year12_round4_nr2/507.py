#include <iostream>
#include <sstream>
#include <string>
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
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <climits>

using namespace std;

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); k++)
#define FORE(k,a,b) for(typeof(a) k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define SZ size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define EXIST(s,e) ((s).find(e)!=(s).end())

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1000 * 1000 * 1000;
const double EPS = 1e-10;

int T;
int W, L;
int N;
int rs[1000];

inline ll dist2(int x1, int y1, int x2, int y2) {
  ll dx = x1 - x2, dy = y1 - y2;
  return dx*dx + dy*dy;
}

int main()
{
  cin >> T;
  REP(ncase, T) {
    dump(ncase);
    
    cin >> N >> W >> L;
    REP(i, N) cin >> rs[i];

    srand(time(NULL));

    VI xs, ys;
    int count = 0;
    
    xs.push_back(0); ys.push_back(0);
    for(int i = 1; i < N; i++) {

      while(true) {

        int bestx = INF*2, besty = INF*2;
        double mind = INF*2;
        REP(k, 10) {
          int rx = rand() % (W+1), ry = rand() % (L+1);
          bool ok = true;
          double md = 0;
          REP(j, xs.size()) {
            double d2 = sqrt(dist2(rx, ry, xs[j], ys[j]));
            double r2 = (double)rs[i] + rs[j];
            md = max(d2, md);
            if(d2 < r2) { ok = false; break; }
          }

          if(ok) {
            if(md < mind) {
              bestx = rx;
              besty = ry;
              mind = md;
            }
          }
        }

        int rx = bestx, ry = besty;

        bool ok = true;
        REP(j, xs.size()) {
          double d2 = sqrt(dist2(rx, ry, xs[j], ys[j]));
          double r2 = (double)(rs[i] + rs[j]);
          //cerr << d2 << ", " << r2 << endl;
          if(d2 <= r2) { ok = false; break; }
          }
        
        if(ok) {
          xs.push_back(rx);
          ys.push_back(ry);
          
          count = 0;
          break; 
        }
        else if(count++ > 10) {
          // reset
          // cerr << "reset!" << endl;
          xs.clear(); ys.clear();
          xs.push_back(0); ys.push_back(0);
          i = 1;
          count = 0;
        }         
      }
    }
     
    assert(xs.size() == N);

    REP(i, N) {
      assert(0 <= xs[i] && xs[i] <= W && 0 <= ys[i] && ys[i] <= L);
    }

    REP(i, N) FOR(j, i+1, N) {
      double d2 = sqrt(dist2(xs[i], ys[i], xs[j], ys[j]));
      double r2 = (double)rs[i] + rs[j];
      assert(d2 >= r2);
    }

    printf("Case #%d:", ncase+1);
    REP(i, N) {
      printf(" %d %d", xs[i], ys[i]);
    }
    printf("\n");
  }
  
  return 0;
}


