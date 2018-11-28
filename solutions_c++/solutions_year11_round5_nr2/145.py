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
typedef long double ld;
typedef unsigned int uint;

const int duzo = 1000;

char c;
int n, tn, a;
int dn[duzo][duzo];

bool check(int k, mi t) {
  if(k == 1)
    return 1;
  int suma = n;
    
  while(suma) {
    mi::itr mit = t.begin();
    if(mit->yy == 0) {
      t.erase(mit);
      continue;
    }
    int i = mit->xx;
    if(t[i + 1] == 0)
      return 0;
    
    while(t[i + 1] >= t[i])
      ++i;
      
    if(i - mit->xx + 1 < k)
      return 0;
    prd("usuwam %d %d\n", mit->xx, i);
    FORE(mit->xx, i, j)
      t[j]--;
    suma -= i - mit->xx + 1;
  }
    
  prd("sukces %d\n", k);
  return 1;
}

void compute(int ti) {
  SC(n);
  if(!n) {
    printf("Case #%d: %d\n", ti, 0);
    fprintf(stderr, "Case #%d: %d\n", ti, 0);
    return;
  }
  mi t;
  FORE(0, n-1, i) {
    SC(a);
    t[a]++;
  }
  if(n == 1) {
    printf("Case #%d: %d\n", ti, 1);
    fprintf(stderr, "Case #%d: %d\n", ti, 1);
    return;
  }
  //sort(t, t+n);
  
  int start = 1, stop = n;
  while(start < stop) {
    int mid = (start + stop + 1) / 2;
    if(check(mid, t))
      start = mid;
    else
      stop = mid - 1;
  }
  
  printf("Case #%d: %d\n", ti, start);
  fprintf(stderr, "Case #%d: %d\n", ti, start);
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

