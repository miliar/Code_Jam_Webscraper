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
#include<iostream>

#define SC(a) scanf("%d", &a)
#define SCC(a) scanf("%c", &a)
#define SC2(a, b) scanf("%d%d", &a, &b)
#define SC3(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define PR(a) printf("%d\n", a)
#define FORE(a, b, c) for(int c=int(a); c<= int(b); ++c)
#define FORD(a, b, c) for(int c=int(a); c>= int(b); --c)
#define FORIT(cont_t, cont, it) for(cont_t::iterator it = cont.begin(); it != cont.end(); ++it) 
#define ALL(a) a.begin(), a.end()

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
typedef long double ld;
typedef unsigned int uint;

const int sto = 103;

char c;
int n, tn, s, p, a;

void compute(int ti) {
  SC3(n,s,p);
  int out = 0;
  FORE(1, n, i) {
    SC(a);
    int b = a / 3;
    if(b >= p || (b == p - 1 && (a % 3) ) )
      ++out;
    else if(s) if( (b == p - 2 && a % 3 == 2) || (b == p - 1 && b > 0) ) {
      --s;
      ++out;
    }
    prd("%d %d %d %d\n", a, b, out, s);
  }
  printf("Case #%d: %d\n", ti, out);
  fprintf(stderr, "Case #%d: %d\n", ti, out);
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

