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

const int sto = 103;

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef long long ll;
typedef long double ld;

char c;
int n, t, x;
int last_ord_0, last_ord_1 = 1, last_time_0, last_time_1;
//int t[sto][sto][sto][2];

int compute() {
  SC(n);
  //vii orders;
  //orders.pb(mp(0, 1));
  last_ord_0 = last_ord_1 = 1;
  last_time_0 = last_time_1 = 0;
  
  /*FORE(1, sto, j)
    FORE(1, sto, h)
      FORE(1, sto, l)
        t[j-1][h-1][l-1][0] = t[j-1][h-1][l-1][0] = 0;*/
  
  FORE(1, n, j) {
    SCC(c);
    SCC(c);
    SC(x);
    
    prd("%d: %c\n", j, c);
    if (c == 'O') {
      //orders.pb(mp(0, x));
      last_time_0 = 1 + max(last_time_1, last_time_0 + abs(last_ord_0 - x));
      last_ord_0 = x;
    }
    else {
      //orders.pb(mp(1, x));
      last_time_1 = 1 + max(last_time_0, last_time_1 + abs(last_ord_1 - x));
      last_ord_1 = x;
    }
  }
  
  return max(last_time_0, last_time_1);
}    

int main() {
  SC(t);
  FORE(1, t, i)
      printf("Case #%d: %d\n", i, compute());
  return 0;
}

