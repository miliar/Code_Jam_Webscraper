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

int seen[1000000];
int bases[15];

int ishappy(int n, int base) {
	memset(seen, 0, sizeof(seen));

	int curr = n;
	while (!seen[curr]) {
		seen[curr] = 1;
		
		int locres = 0;
		
		while (curr) {
			int digit = curr % base;
			locres += digit*digit;
			curr /= base;
		}
		
		curr = locres;
		if (locres == 1) break;
	}

	return (curr == 1);
}

int main() {
	int T;
	scanf("%d", &T);
	rep(t,T) {
		char line[1000];
		char *pos = line;
		int anda = 0;
		scanf(" %[^\n]", line);
		
		int ind = 0;
		while (sscanf(pos, "%d %n", &bases[ind++], &anda) > 0) pos += anda;
		
		ind--;

		int curr = 2;
		while(1) {
			bool good = true;
			rep(i, ind) {
				if (!ishappy(curr, bases[i])) {
					good = false;
					break;
				}
			}

			if (good) break;
			curr++;
		}

		printf("Case #%d: %d\n", t+1, curr);
	}
}
