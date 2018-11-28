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




map<VI , int> MM;

int nnb(VI NN) { 
  if(MM.count(NN)) return MM[NN];
//  MM[NN] = 1000;
  int i = 0;
//  REP(k, NN.sz) cerr << NN[k] << " " ;
//  cerr << endl;

  for(; i < NN.sz && NN[i] <= i; i++);
  if(i == NN.sz) {
    MM[NN] = 0;
    return 0;
  }

  int best = 1000;
  REP(i, NN.sz - 1) {
    VI N2(NN);
    if(NN[i+1] >= NN[i]) continue;
    N2[i] = NN[i+1];
    N2[i+1] = NN[i];
    int b = nnb(N2);
    if(b < best) best = b;
  }
  MM[NN] = best+1;
  return best+1;
}




int nb(VS M) {
  VI NB(M.sz);
  REP(i, M.sz) NB[i] = 0;
  REP(i, M.sz) REP(j, M.sz) if(M[i][j] == '1') NB[i] = j;
  MM.clear();
  return nnb(NB);
  /*
  int C = 0;
  
  int i = 1;
  while(i >= 0) {
    for(int k = 0; k < M.sz; k++) cerr << NB[k] << " " ;
    cerr << endl;
  for(i = M.sz - 1; i >= 0; i--) {
    if(NB[i] > i) {
      while(NB[i+1] >= NB[i] || NB[i+1] > i) i++;
      int t = NB[i];
      NB[i] = NB[i+1];
      NB[i+1] = t;
      C++;
      break;
    }
  }

  }

  return C;*/
}


int main() {
  cout.precision(16);
  int T, N;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> N;
    string S;
    VS M;
    for(int n = 0; n < N; n++) {
      cin >> S;
      M.pb(S);
    }
    cout << "Case #" << i << ": " << nb(M) << endl;

  }
}
