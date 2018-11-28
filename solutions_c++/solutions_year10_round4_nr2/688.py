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



int P;
int solve(vector<int> &M, VVI &Price, int h, int pos) {

//  cerr << "# " << h << " " << pos << endl;
  
  if(h == P - 1) {
    if(M[2*pos] > 0 && M[2*pos+1] > 0) return 0;
    else return Price[h][pos];
  }


  int price1 = Price[h][pos] + solve(M, Price, h + 1, 2*pos) + solve(M, Price, h + 1, 2*pos+1);

  vector<int> M2(M);

  for(int t = pos * (1 << (P-h)); t < (pos+1) * (1 << (P-h)); t++) {
    if(M[t] == 0) return price1;
    M2[t]--;
  }

  int price2 = solve(M2, Price, h + 1, 2*pos) + solve(M2, Price, h + 1, 2*pos+1);

  return min(price1, price2);
}

int main() {
  cout.precision(16);
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> P;
    VI M(1 << P);    
    for(int j = 0; j < M.sz; j++) cin >> M[j];
    VVI Price(P);
    for(int j = 1; j <= P; j++) {
      Price[P - j].resize(1 << (P - j));
      for(int k = 0; k < Price[P-j].sz; k++) cin >> Price[P-j][k];
    }

//REP(a, Price.sz) {REP(b, Price[a].sz) cerr << Price[a][b] << " "; cerr << endl;}


    cout << "Case #" << i << ": " << solve(M, Price, 0, 0) << endl;

  }
}
