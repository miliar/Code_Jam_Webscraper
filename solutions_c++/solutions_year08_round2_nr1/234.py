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


int count(vector<pair<int, int> > V) {
	SORT(V);
	int NB = 0;
	REP(i, V.sz) REP(j, i) REP(k, j) {
		int X3 = V[i].first + V[j].first + V[k].first;
		if(X3 % 3 != 0) continue;
		int Y3 = V[i].second + V[j].second + V[k].second;
		if(Y3 % 3 != 0) continue;
		NB++;
	}
	return NB;
}

int main() {
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    LL n, A, B, C, D, x0, y0, M;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

    vector<pair<int, int> > V;

    LL X = x0;
    LL Y = y0;
    for(int k = 0; k < n; k++) {
	    V.push_back(pair<int, int>(X, Y));
	    X = (A * X + B) % M;
	    Y = (C * Y + D) % M;
    }

    cout << "Case #" << i << ": " << count(V) << endl;

  }
}
