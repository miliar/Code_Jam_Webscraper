#include<cstdio>
#include<algorithm>
#include<utility>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<cmath>

#define SC(a) scanf("%d", &a)
#define SCC(a) scanf("%c", &a)
#define SC2(a, b) scanf("%d%d", &a, &b)
#define SC3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define PR(a) printf("%d\n", a)
#define FORE(a, b, c) for(int c=a; c<=b; ++c)
#define FORIT(cont_t, cont, it) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it) 

#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define itr iterator

#define dbg if(0) 
#define prd dbg printf
#define koniec dbg {SCC(c);SCC(c);} return 0;

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef long long ll;
typedef double ld;
typedef unsigned int uint;

const int sto = 203;
const ll kosmos = (ll) 1000000 * 1000000 * 1000000;

char c;
int n, tn, d, coun, x, y;
vii in;
ll start, stop, mid;
ld last;

int check(ld di) {
  prd("check %f\n", di);
  last = in.begin()->xx - di;
  FORIT(vii, in, pit) {
    coun = pit->yy;
    if (pit == in.begin())
      --coun;
    
    FORE(1, coun, ci) {
      if(last + d> pit->xx + di)
        return 0;
      last = max(last + d, pit->xx - di);
    }
  }
  prd("check ok\n");
  return 1;
}

ld compute() {
  SC2(n, d);
  in.clear();
  
  FORE(1, n, i) {
    SC2(x, y);
    in.pb(mp(x, y));
  }
  
  //sort(in.begin(), in.end());
  
  start = 0, stop = kosmos;
  while(start < stop) {
    mid = (start + stop) / 2;
    
    if (check((ld) mid / 2))
      stop = mid;
    else
      start = mid + 1;
  }
    
  return (ld) start / 2;
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
      printf("Case #%d: %f\n", ti, compute());
  return 0;
}

