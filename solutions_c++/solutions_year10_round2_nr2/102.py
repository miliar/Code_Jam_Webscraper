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




int main() {
  cout.precision(16);
  long long C, N, K, B, T;
  cin >> C;
  for(int i = 1; i <= C; i++) {
    cin >> N >> K >> B >> T;
    vector<long long> X(N), V(N);
    for(int j = 0; j < N; j++) cin >> X[j];
    for(int j = 0; j < N; j++) cin >> V[j];

    int nb_slow = 0, nb_swap = 0, nb_fast = 0;
    for(int j = N-1; j>=0 && nb_fast < K; j--) {
      if(X[j] + V[j] * T < B) {nb_slow++; continue;}
      nb_swap += nb_slow;
      nb_fast++;
    }

    if(nb_fast < K) cout << "Case #" << i << ": IMPOSSIBLE" << endl; 
    else  cout << "Case #" << i << ": " << nb_swap << endl; 
  }
}
