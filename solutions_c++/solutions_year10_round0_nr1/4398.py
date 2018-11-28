#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// MACROS
#define PRINT(X, K) cout << "Case #" << X << ": " << K << endl;
#define FOR(i, a, b) for(int i=(a); i<(b);++i)
#define FOREACH(T, I, J) for (T::iterator I = J.begin(); I != J.end(); ++I)
#define FOREACH_B(T, I, S, E) for (I = S; I != E; ++I)
#define FOREACH_CONST(T, I, J) for (T::const_iterator I = J.begin(); I != J.end(); ++I)
#define PRINT_COLLECTION(T, C) for(T::iterator it=C.begin(); it!=C.end(); ++it) cout << " " << *it;

int main() {
	
	int T, N, K, i; cin >> T;
	FOR(i, 0, T) {
		cin >> N >> K;
		int *s = new int[N];
		bool *p = new bool[N];
		int j,k;
		fill(p, p+N, false);
		fill(s, s+N, 0);
		bool on;
		FOR(j, 0, K) {
			p[0] = on = true;
			FOR(k, 1, N) {
				p[k] = p[k-1] && (s[k-1] == 1);
			}
			FOR(k, 0, N) {
				if (p[k]) {
					s[k] = (s[k] == 0 ? 1 : 0);
				}
			}
		}
		
		on = true;
		FOR(j, 0, N) {
			on = on && (s[j] == 1);
		}
		cout << "Case #" << (i+1) << ": " << (on ? "ON" : "OFF") << endl;
	}
	
	return 0;
	
}

