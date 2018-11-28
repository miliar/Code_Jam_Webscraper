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

int T, R;
int bo[120][120];

bool ck(int i, int j) {
	if (!i || !j) return false;
	
	if (bo[i-1][j] && bo[i][j-1]) return true;

	return false;
}

bool ckalive(int i, int j) {
	if ((i && bo[i-1][j]) || (j && bo[i][j-1])) return true;
	return false;
}

int main() {
	cin >> T;
	rep(t,T) {
		cin >> R;
		
		memset(bo, 0, sizeof(bo));
		
		rep(i,R) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			x1--; x2--; y1--; y2--;
			
			for (int j = x1; j <= x2; j++) {
				for (int k = y1; k <= y2; k++) {
					bo[k][j] = 1;
				}
			}
		}
		
//		rep(i,100) {
//			rep(j,100) {
//				cout << bo[i][j] << " ";
//			}
//			cout << endl;
//		}

		int res = 0;
		
		while (true) {
			res++;
			bool keep = false;
			
			for (int i = 115; i >= 0; i--) {
				for (int j = 115; j >= 0; j--){
					if (bo[i][j]) {
						if (ckalive(i,j)) keep = true;
						else bo[i][j] = 0;
					}
					else {
						if (ck(i,j)) {
							bo[i][j] = 1;
							keep = true;
						}
					}
				}
			}

			if (!keep) break;
		}
		
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	
	return 0;
}

