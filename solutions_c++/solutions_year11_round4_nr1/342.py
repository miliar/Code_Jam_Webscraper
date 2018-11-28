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
  int T, X, S, R, t, N;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> X >> S >> R >> t >> N;
		int E, B;
		vector<pair<int, int> > W(N+1);
		for(int j = 0; j < N; j++) {
			cin >> B >> E >> W[j].first;
			W[j].second = E - B;
		}
		int sl = X;
		for(int j = 0; j < N; j++) sl -= W[j].second;
		W[N].first = 0;
		W[N].second = sl;

		sort(W.begin(), W.end());

		double tt = 0;
		for(int j = 0; j < N+1; j++) {

			if(tt < t) {
				if((t - tt)*(R + W[j].first) >= W[j].second) 
					tt +=W[j].second / double(R + W[j].first);
				else
					tt = t + (W[j].second - (t - tt)*(R + W[j].first))/ double(S + W[j].first);
			}
			else {
				tt += W[j].second / double(S + W[j].first);
			}
		//	cerr << W[j].first << " " << W[j].second << " " << tt << endl;
		}

		cout << "Case #" << i << ": " << tt << endl;

	}
}
