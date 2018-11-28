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


//int* MAP[2];

int compute(VI &T, int pos, VI &C, int V, int M) {

 // cout << pos << " " << T[pos] << endl;
  if(pos >= (M - 1)/2) {
    if(V == T[pos]) return 0;
    else return 100000;
  }
//  if(MAP[V][pos] != -2) return MAP[V][pos];

  int nb1 = compute(T, 2*pos+1, C, V, M);
  int nb2 = compute(T, 2*pos+2, C, V, M);

  int best_AND = 100000;
  int best_OR = 100000;

  if(V == 1) {
    best_AND = nb1 + nb2;
    if(nb1 < nb2) best_OR = nb1; else best_OR = nb2;
  }
  else {
    best_OR = nb1 + nb2;
    if(nb1 < nb2) best_AND = nb1; else best_AND = nb2;
  }

//  cout << pos << " " << best_OR << " " << best_AND << " " << nb1 << " " << nb2 << endl;

  int best = 100000;

  if(T[pos] == 0) best = best_OR;
  else best = best_AND;
  if(C[pos] == 1) {
    if(T[pos] == 0 && best_AND + 1 < best) best = best_AND + 1;
    else if(T[pos] == 1 && best_OR + 1 < best) best = best_OR + 1;
  }

  if(best >= 100000) return 100000;
  else return best;






}

int main() {
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    int M, V;
    cin >> M >>  V;
    VI T(M), C(M);
    REP(k, (M - 1)/2) cin >> T[k] >> C[k];
    REP(k, (M + 1)/2) cin >> T[((M - 1)/2) + k];

    int nb = compute(T, 0, C, V, M) ;
    if(nb >= 100000) cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    else cout << "Case #" << i << ": " << nb << endl;
  }
}
