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
const int MOD = 1000000007;

int main() {
	long long N, n, m, X, Y, Z;
	cin >> N;
	
	REP(iCase, N) {
		cin >> n >> m >> X >> Y >> Z;
		vector<long long> tmp(m);
		vector<int> A(n);
		REP(i, m) cin >> tmp[i];
		REP(i, n) {
			A[i] = tmp[i%m];
			tmp[i%m] = (X * tmp[i%m] + Y * (i+1)) % Z;
		}
		
		map<int, long long> M2; 
				
		REP(i, n) {
			map< int, long long> M1(all(M2));
			/*cout << endl;
			TR(it, M1) {
				REP(i, it->fi.sz) cout << it->fi[i] << " ";
				cout << "    ::= " << it->se << endl;
			}*/

			typeof(M1.begin()) it2 = M2.find(A[i]);
			if (it2 == M2.end()) {
				M2[ A[i] ] = 1;
				it2 = M2.find(A[i]);
			}else{
				it2->second++;
				it2->second %= MOD;
			}	
			
			TR(it, M1) if (it->fi < A[i]) {
				it2->second += it->second;
				it2->second %= MOD;
			}
			
		
			
		}
		
		//REP(i, n) cout << A[i] << endl;
		int ret = 0;
		TR(it, M2) {ret+=it->second; ret %= MOD;   }
		cout << "Case #" << iCase + 1 << ": " << ret << endl;
	}
		
	
	return 0;
}
