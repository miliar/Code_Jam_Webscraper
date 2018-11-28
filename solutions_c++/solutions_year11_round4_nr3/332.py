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
  int T;
  cin >> T;
  for(int a = 1; a <= T; a++) {
		int N;
		cin >> N;


		vector<int> T(N+1);

int nb = 1;
		for(int i = 2; i <= N; i++) {
			
			if(T[i] == 0) {
				for(int j = 1; i*j <= N; j++) T[i*j] = 1;
				int g = i;
				for(int j = 1; g*i <= N; g*=i) nb++;
			}
		}

		if(N <= 1) nb = 0;

    cout << "Case #" << a << ": " << nb << endl;

  }
}
