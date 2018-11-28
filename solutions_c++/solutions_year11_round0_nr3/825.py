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

const int duzo = 10000001;

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef pair<int, int> pi;
typedef long long ll;
typedef long double ld;

ll n, t, x, com, all_min, all_sum, all_xor;

ll compute() {
  SC(n);
  all_min = duzo, all_sum = all_xor = 0;
  
  FORE(1, n, j) {
    SC(x);
    all_sum += x;
    all_xor ^= x;
    all_min = min(all_min, x);
  }
  
  if (all_xor)
    return 0;
  else
    return all_sum - all_min;
}

int main() {
  SC(t);
  FORE(1, t, i) {
    com = compute();
    if (com)
      printf("Case #%d: %ld\n", i, com);
    else
      printf("Case #%d: NO\n", i);
  }
  dbg SC(t);
  return 0;
}

