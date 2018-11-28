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
// BEGIN CUT HERE
#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)

string itos(int x) { stringstream ss; ss << x; return ss.str(); }
vector<string> split(string s) { vector<string> r; string t; stringstream ss(s); while(ss >> t) r.push_back(t); return r; }
// END CUT HERE

vi digits;
int numdigs;
int countzero;

int main() {
	int T;
	scanf("%d", &T);

	rep(t,T) {
		char buf[50];
		scanf("%s", buf);
		
		digits.clear();
		countzero = 0;
		
		char chardig[2];
		chardig[1] = '\0';
		rep(i, strlen(buf)) {
			chardig[0] = buf[i];
			int aux = atoi(chardig);

			if (!aux) countzero++;
			digits.pb(aux);
			numdigs++;
		}

//		numdigs = 0;
//		while (N) {
//			int aux = N%10;
//			if (!aux) {
//				countzero++;
//			}
//			
//			digits.pb(aux);
//
//			numdigs++;
//			N /= 10;
//		}
		
		printf("Case #%d: ", t+1);
		
		bool succeed = next_permutation(all(digits));
		if (succeed) {
			rep(i, sz(digits)) {
				printf("%d", digits[i]);
			}
		}
		else {
			sort(all(digits));
			int first = true;
			rep(i, sz(digits)) {
				if (digits[i]) {
					printf("%d", digits[i]);
					if (first) {
						first = false;
						rep(j, countzero+1) printf("0");
					}
				}
			}
		}

		printf("\n");
	}
}

