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

const int duzo = 502;

char c;
int n, tn;
int r, u, d;
int t[duzo][duzo], sum1[duzo][duzo], sum2[duzo][duzo], sum3[duzo][duzo];

bool check(int dim, int i, int j) {
  int ss1 = sum1[i + dim][j + dim] - sum1[i - 1][j + dim] - sum1[i + dim][j - 1] + sum1[i - 1][j - 1];
  int ss2 = sum2[i + dim][j + dim] - sum2[i - 1][j + dim] - sum2[i + dim][j - 1] + sum2[i - 1][j - 1];
  int ss3 = sum3[i + dim][j + dim] - sum3[i - 1][j + dim] - sum3[i + dim][j - 1] + sum3[i - 1][j - 1];
  prd("%d %d %d %d %d %d\n", dim, i, j, ss1, ss2, ss3);
  
  ss1 -= i * t[i][j] + i * t[i][j + dim] + (i + dim) * t[i + dim][j] + (i + dim) * t[i + dim][j + dim];
  ss2 -= j * t[i][j] + (j + dim) * t[i][j + dim] + j * t[i + dim][j] + (j + dim) * t[i + dim][j + dim];
  ss3 -= t[i][j] + t[i][j + dim] +  t[i + dim][j] + t[i + dim][j + dim];
  
  prd("%d %d %d %d %d %d\n", dim, i, j, ss1, ss2, ss3);
  prd("%d %d\n\n", 2 * i * ss3 + dim * ss3, 2 * j * ss3 + dim * ss3);
  if ((2 * ss1 == ((2 * i * ss3) + (dim * ss3))) && (2 * ss2 == (2 * j * ss3) + (dim * ss3)))
    return 1;
  return 0;
}

void compute(int ti) {
  SC3(r, u, d);
  FORE(0, r, i)
    t[i][0] = sum1[i][0] = sum2[i][0] = sum3[i][0] = 0;
  FORE(0, u, i)
    t[0][i] = sum1[0][i] = sum2[0][i] = sum3[0][i] = 0;
  
  FORE(1, r, i) {
    SCC(c);
    FORE(1, u, j) {
      SCC(t[i][j]);
      t[i][j] -= '0';
      sum1[i][j] = sum1[i - 1][j] + sum1[i][j - 1] - sum1[i - 1][j - 1];
      sum2[i][j] = sum2[i - 1][j] + sum2[i][j - 1] - sum2[i - 1][j - 1];
      sum3[i][j] = sum3[i - 1][j] + sum3[i][j - 1] - sum3[i - 1][j - 1];
      
      sum1[i][j] += i * t[i][j];
      sum2[i][j] += j * t[i][j];
      sum3[i][j] += t[i][j];
      
      prd("%d %d %d %d %d %d\n", i, j, t[i][j], sum1[i][j], sum2[i][j], sum3[i][j]);
    }
  }
  
  int best = duzo;
  for(int dim = min(r, u); dim >= 2; --dim) {
    FORE(1, r - dim, i) {
      FORE(1, u - dim, j)
        if (check(dim, i, j)) {
          best = dim + 1;
          break;
        }
      if (best != duzo) break;
    }
    if (best != duzo) break;
  }
        
  if (best == duzo)
    printf("Case #%d: IMPOSSIBLE\n", ti);
  else 
    printf("Case #%d: %d\n", ti, best);
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
      compute(ti);
  return 0;
}

