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

const int tys = 1002;
const ld eps = 0.0000001;

char c;
int n, tn, w, l, u, g;
int x[2][tys], y[2][tys];

double pole(int ch, ld to) {
  int m = (ch == 0) ? l : u;
  double ret = 0;
  
  FORE(1, m-1, i) {
    if (x[ch][i + 1] <= to) {
      ret += (x[ch][i + 1] - x[ch][i]) * min(y[ch][i + 1], y[ch][i]);
      ret += abs(y[ch][i + 1] - y[ch][i]) * ((ld) (x[ch][i + 1] - x[ch][i]) / 2);
    }
    else {
      ld toy = y[ch][i] + (y[ch][i + 1] - y[ch][i]) * (to - x[ch][i]) / (x[ch][i + 1] - x[ch][i]);
      ret += (to - x[ch][i]) * min(toy, ld(y[ch][i]));
      ret += abs(toy - y[ch][i]) * ((ld) (to - x[ch][i]) / 2);
      break;
    }
  }
  return ret;
}   

void compute(int ti) {
  SC3(w, l, u);
  SC(g);
  FORE(1, l, i) {
    SC2(x[0][i], y[0][i]);
    y[0][i] += tys;
  }
  FORE(1, u, i) {
    SC2(x[1][i], y[1][i]);
    y[1][i] += tys;
  }
  printf("Case #%d:\n", ti);
  fprintf(stderr, "Case #%d:\n", ti);
  
  double whole = pole(1, w) - pole(0, w), last = 0;
  prd("pole: %f\n", whole);
  
  FORE(0, g-2, i) {
    ld start = last, stop = w;
    while(stop - start > eps) {
      ld mid = (start + stop) / 2;
      ld result = pole(1, mid) - pole(0, mid) - whole * i / g;
      
      if(result * g > whole)
        stop = mid;
      else
        start = mid;
    }
    last = start;
    printf("%f\n", start);
    fprintf(stderr, "%f\n", start);
    prd("za: %f\n", pole(1, start) - pole(0, start));
  }
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

