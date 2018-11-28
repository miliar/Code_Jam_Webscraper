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
typedef vector<pair<pi, int> > viii;
typedef long long ll;
typedef double ld;
typedef unsigned int uint;

const int duzo = 1000009;

char c;
int n, tn;
int x, s, r, tim, x1, x2, w;
int tab[duzo];

bool comp(pair<pi, int> p1, pair<pi, int> p2) {
  return (p1.yy < p2.yy) || (p1.xx > p2.xx && p1.yy == p2.yy);
}

double compute() {
  SC3(x, s, r);
  SC2(tim, n);
  ld tim2 = tim;
  
  viii walks, walks2;
  
  FORE(1, n, i) {
    SC3(x1, x2, w);
    FORE(x1, x2 - 1, j)
      tab[j] += w;
    walks.pb(mp(mp(x1, x2), s + w));
  }
  sort(walks.begin(), walks.end());
  //reverse(walks.begin(), walks.end());
  
  int last = 0;
  FORIT(viii, walks, wit) {
    walks2.pb(mp(mp(last, wit->xx.xx), s));
    last = wit->xx.yy;
  }
  walks2.pb(mp(mp(last, x), s));
  
  FORIT(viii, walks2, wit)
    walks.pb(*wit);
  sort(walks.begin(), walks.end(), comp);
  
  dbg FORIT(viii, walks, wit)
    printf("%d %d %d\n", wit->xx.xx, wit->xx.yy, wit->yy);
   
  ld out = 0; 
  FORIT(viii, walks, wit) {
    if (tim2 > 0) {
      ld timw = ld (wit->xx.yy - wit->xx.xx) / (wit->yy + r - s);
      
      if (timw <= tim2) {
        out += timw;
        tim2 -= timw;
      }
      else {
        ld kon = tim2 * (wit->yy + r - s);
        out += tim2;
        out += ld ( (ld) wit->xx.yy - wit->xx.xx - kon) / (wit->yy);
        tim2 = 0;
      }
    }
    else
      out += ld (wit->xx.yy - wit->xx.xx) / (wit->yy);
    //prd("%f\n", out);
  }   
  
  return out;
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
      printf("Case #%d: %f\n", ti, compute());
  return 0;
}

