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

const int sto = 103;

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mi;
typedef pair<int, int> pi;
typedef vector<pi> vii;
typedef long long ll;
typedef double ld;
typedef unsigned int uint;

char c, score[sto][sto];
int n, tn;
vi op[sto];
int wins[sto];
ld wp[sto], owp[sto], oowp[sto];

int compute(int ti) {
  SC(n);
  FORE(1, n, i) {
    op[i].clear();
    wins[i] = 0;
    SCC(c);
    
    FORE(1, n, j) {
      SCC(score[i][j]);
      if (score[i][j] != '.')
        op[i].pb(j);
      if (score[i][j] == '1')
        ++wins[i];
      prd("%d vs %d: %c\n", i, j, score[i][j]);
    }
  }
  
  FORE(1, n, i) {
    wp[i] = (ld) wins[i] / op[i].size();
    owp[i] = 0;
    FORIT(vi, op[i], it)
      owp[i] += (ld) (wins[*it] - (score[*it][i] == '1')) / (op[*it].size() - 1);
    owp[i] /= op[i].size();
  }
  
  FORE(1, n, i) {
    oowp[i] = 0;
    FORIT(vi, op[i], it)
      oowp[i] += owp[*it];
    oowp[i] /= op[i].size();
    
    prd("%d: %d %d %f %f %f\n", i, wins[i], op[i].size(), wp[i], owp[i], oowp[i]);
  }
    
  printf("Case #%d:\n", ti);
  FORE(1, n, i)
    printf("%f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
  return 0;
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
      compute(ti);
  return 0;
}

