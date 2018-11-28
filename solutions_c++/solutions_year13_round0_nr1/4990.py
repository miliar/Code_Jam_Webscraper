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

#define REP(i, n) for(int i = 0; i< n; ++i)
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

const int sto = 103;

char c, t[4][4];
int n, tn, dots, xwin, owin, xks, oks;

void compute(int ti) {
  dots = xwin = owin = 0;
  REP(i, 4) {
    SCC(c);
    REP(j, 4) {
      SCC(t[i][j]);
      if(t[i][j] == '.') ++dots;
    }
  }
  SCC(c);
  REP(i, 4) {
    oks = xks = 0;
    REP(j, 4) {
      if(t[i][j] == 'O' || t[i][j] == 'T') ++oks;
      if(t[i][j] == 'X' || t[i][j] == 'T') ++xks;
    }
    owin += (oks == 4);
    xwin += (xks == 4);
    
    oks = xks = 0;
    REP(j, 4) {
      if(t[j][i] == 'O' || t[j][i] == 'T') ++oks;
      if(t[j][i] == 'X' || t[j][i] == 'T') ++xks;
    }
    owin += (oks == 4);
    xwin += (xks == 4);
  }
    oks = xks = 0;
    REP(j, 4) {
      if(t[j][j] == 'O' || t[j][j] == 'T') ++oks;
      if(t[j][j] == 'X' || t[j][j] == 'T') ++xks;
    }
    owin += (oks == 4);
    xwin += (xks == 4);
    
    oks = xks = 0;
    REP(j, 4) {
      if(t[j][3-j] == 'O' || t[j][3-j] == 'T') ++oks;
      if(t[j][3-j] == 'X' || t[j][3-j] == 'T') ++xks;
    }
    owin += (oks == 4);
    xwin += (xks == 4);
  
  fprintf(stderr,"%d %d %d\n", xwin, owin, dots);
  
  
  printf("Case #%d: ", ti);
  if(xwin)
    printf("X won\n");
  else if (owin)
    printf("O won\n");
  else if (!dots)
    printf("Draw\n");
  else
    printf("Game has not completed\n");
}

int main() {
  SC(tn);
  FORE(1, tn, ti)
    compute(ti);
  return 0;
}

