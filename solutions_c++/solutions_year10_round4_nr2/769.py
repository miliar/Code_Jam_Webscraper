#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 
#define INT_INF 0x3F3F3F3F
#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)

string itos(int x) { stringstream ss; ss << x; return ss.str(); }
vector<string> split(string s) { vector<string> r; string t; stringstream ss(s); while(ss >> t) r.push_back(t); return r; }

int T, P;
int M[1050];
int pr[1050][1050];
int res;

void calc(int init, int quant) {
	bool last = false;

	for (int i = init; i < init+quant; i++) if (M[i] > 0) {
		last = true;
		break;
	}

	if (last) {
		for (int i = init; i < init+quant; i++) {
			if (M[i] > 0) M[i]--;
		}
		res++;
	}
}

int main() {
	cin >> T;
	rep(t,T) {
		cin >> P;
		
		rep(i, 1<<P) {
			cin >> M[i];
			M[i] = P - M[i];
		}
		rep(i,(1<<P)-1) cin >> pr[0][0];
		
		res = 0;
		
		int iter = P;
		while (iter > 0) {
			int quant = 1<<iter;

			for (int i = 0; i < (1<<P); i += quant) {
				calc(i, quant);
			}
			
			iter--;
		}

		cout << "Case #" << t+1 << ": " << res << endl;
	}
	
	return 0;
}

