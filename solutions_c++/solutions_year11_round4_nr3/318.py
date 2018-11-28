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

const int duzo = 1003;

char c;
int n, tn;
int t[duzo];

int compute() {
  SC(n);
  if (n == 1)
    return 0;
    
  int out1 = 0, out2 = 0;
  
  FORE(2, n, i)
    if(t[i] == i) {
      ++out1;
      
      int pot = 1, j = i;
      while(j * i <= n) {
        j *= i;
        ++pot;
      }      
      out2 += pot;
    }
        
  
  return out2 - out1 + 1;
}

int main() {
  t[1] = 1;
  FORE(2, duzo - 1, i)
    if(!t[i]) {
      for(int j = i; j <=duzo - 1; j += i)
        t[j] = i;
    }
      
  SC(tn);
  FORE(1, tn, ti)
      printf("Case #%d: %d\n", ti, compute());
  return 0;
}

