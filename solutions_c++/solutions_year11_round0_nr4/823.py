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

#define dbg if(1) 
#define prd dbg printf

const int duzo = 1001;

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef long long ll;
typedef double ld;

ld p[duzo], c[duzo];
int n, t;
int v;

void get_prob(int n) {
  p[1] = c[1] = 0;
  p[2] = 1;
  c[2] = 2;
  
  FORE(3, n, m) {
    ld suma = m;
    FORE(1, m - 1, k)
      suma += c[k] + p[m - k];
    
    c[m] = suma / (m - 1);
    p[m] = c[m] - 1;
    
    prd("%d: %f %f\n", m, p[m], c[m]);
  }
}
  
ld compute() {
  SC(n);
  ld out = n;
  
  FORE(1, n, j) {
    SC(v);
    if (v == j)
      --out;
  }

  return out;
}

int main() {
  //get_prob(100);
  SC(t);
  FORE(1, t, i)
      printf("Case #%d: %f\n", i, compute());
  return 0;
}

