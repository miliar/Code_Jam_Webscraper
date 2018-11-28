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


int* SOL;

void init(int K) {
	K++;
	memset(SOL, -1, K*sizeof(int));
	int pos = 0;
	
	for(int n = 0; n < K; n++) {
		
		int move = n;// % (K - n);
		while(SOL[pos] != -1 || move > 0) {
			pos++;
			if(pos == K) pos = 0;
			if(SOL[pos] == -1) move--;
		}		
		SOL[pos] = n;
	}
}

int main() {
	SOL = new int[6000];
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    int K, n;
    cin >> K >> n;
    VI D;
    REP(k, n) {
	    int d;
	    cin >> d;
	    D.pb(d);
    }
    init(K);
    cout << "Case #" << i << ":";

    REP(k, D.sz) cout << " " << SOL[D[k]];
    cout << endl;



  }
}
