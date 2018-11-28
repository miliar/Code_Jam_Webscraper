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



int Prod[3000];



VI compute(int N, int M, int A) {
  memset(Prod, -1, sizeof(Prod));
  REP(x, N+1) REP(y, M+1) Prod[x*y] = x;
  VI R;

  REP(x1, N+1) REP(y2, M+1) {
    int prod = x1*y2 - A;
    if(prod < 0 || prod > N*M) continue;
    if(Prod[prod] != -1) {
      R.resize(4);
      R[0] = x1;
      R[1] = prod / Prod[prod];
      R[2] = Prod[prod];
      R[3] = y2;
      return R;
    }
    return R;
  }
}


int main() {

  int C;
  cin >> C;
  for(int i = 1; i <= C; i++) {

    int N, M, A;
    cin >> N >> M >> A;


    VI Tri = compute(N, M, A);
    if(Tri.sz == 0)  cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    else {
      cout << "Case #" << i << ": 0 0 ";
      cout << Tri[0] << " " << Tri[1] << " " << Tri[2] << " " << Tri[3] << endl;
    }
  }
}
