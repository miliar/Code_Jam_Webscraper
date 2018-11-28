#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751

int Tab[20];
int N, M;


int MAP[10][1024];

int solve(int col, int leftcol) {

 

  if(col == N) return 0;
  if(MAP[col][leftcol] != -1) return MAP[col][leftcol];
  int best = 0;


  for(int pos = 0; pos < (1 << M); pos++) if((pos & Tab[col]) == 0) {
    if( ((pos & leftcol) == 0) 
    &&  (((pos >> 1) & leftcol) == 0) 
    &&  (((leftcol >> 1) & pos) == 0)
    ) {
      int r = solve(col+1, pos);
      if(__builtin_popcount(pos) + r > best) best = __builtin_popcount(pos) + r;
  }
  }
  MAP[col][leftcol] = best;
  return best;
}


int solve(VS C) {
  memset(MAP, -1, sizeof(MAP));

  REP(x, C[0].len) {
    int pos = 0;
    REP(y, C.sz) {
      pos <<= 1;
      if(C[y][x] == 'x') pos |= 1;
    }
    Tab[x] = pos;
  }

  return solve(0, 0);
}

int main() {
  cout.precision(16);
  int C;
  cin >> C;
  for(int i = 1; i <= C; i++) {
    cin >> M >> N;
    VS Classe;
    REP(k, M) {
      string S;
      cin >> S;
      Classe.pb(S);
    }
    cout << "Case #" << i << ": " << solve(Classe) << endl;

  }
}
