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
int a, b, tn;

int next(int x, int ten) {
  int last = x % 10;
  int out = x / 10 + last * ten;
  prd("next %d %d -> %d\n", x, ten, out);
  return out;
}

void compute(int ti) {
  SC2(a, b);
  int out = 0;
  int ten = 1;
  FORE(a, b, i) {
    while(ten <= i / 10)
      ten *= 10;
      
    int c = next(i, ten);
    while(c != i) {
      if(i < c && c <= b && c >= ten)
        ++out;
      c = next(c, ten);
    }
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

