#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <numeric>
// #include <gmpxx.h>       // GNU MP Bignum library 
using namespace std;

#define FOR(i, a, b) for(int i = (int)a; i < (int)b; ++i)
#define REP(i, n) for(int i = 0; i < (int)n; ++i)
#define TR(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

#define all(c) (c).begin(), (c).end()
#define rAll(c) (c).rbegin(), (c).rend()

#define sz size()
#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

int main() {
	int N, P, K, L;
	cin >> N;
	
	REP(iCase, N) {
		cin >> P >> K >> L;
		vi freq(L);
		REP(i, L)  cin >> freq[i];
		sort(rAll(freq));
		
		priority_queue<long long> q;
		REP(i, K) q.push(-1);
		
		long long ret = 0;
		bool poss = true;
		REP(i, L) {
			if (q.empty()) {poss = false; break;}
			long long tmp = q.top(); q.pop();
			ret -= tmp * freq[i];
			if (tmp > -P) q.push(tmp-1);
		}
		
		cout << "Case #" << iCase + 1 << ": ";
		if (poss) cout << ret << endl; 
		else cout << "Impossible" << endl;
	}
		
	
	return 0;
}
