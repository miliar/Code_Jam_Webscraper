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
#include <gmpxx.h>       // GNU MP Bignum library 
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

mpz_class sub[41][41];
string s;

string helper(const string &s) {
	string ret;
	int i = 0;
	while (i < s.sz && s[i] == '0') ++i;
	ret = s.substr(i, s.sz-i);
	if (ret == "") ret = "0";
	
	return ret;
}

map< pair<mpz_class, int> int> M;

int cnt(mpz_class x, int idx) {
	if (idx >= s.sz) {
		if (x < 0) x = -x;
		//if (x % 2 == 0 || x % 3 == 0 || x % 5 == 0 || x % 7 == 0) cout << "endX = " << x << " ugly!" << endl; else cout << "endX = " << x << " not ugly!" << endl;
		if (x % 2 == 0 || x % 3 == 0 || x % 5 == 0 || x % 7 == 0)  return 1; else return 0;
	
	}
	
	typeof(M.begin()) it = M.find(mp(x, idx));
	
	if (it != M.end()) return it->second;
	
	int ret = 0;
	
	FOR(i, idx+1, s.sz+1) {
		ret += cnt(x + sub[idx][i], i);
		ret += cnt(x - sub[idx][i], i);
	}
	
	M[mp(x, idx)] = ret;
	
	//cout << "x = " << x << "  idx = " << idx << "  ret = " << ret << endl;
	
	return ret;
}

int main() {
	int N;
	cin >> N;
	
	REP(iCase, N) {
		cin >> s;
		
		FOR(b, 1, 1+s.sz) REP(a, b) sub[a][b] = mpz_class( helper(s.substr(a, b-a)) );		
		// FOR(b, 1, 1+s.sz) REP(a, b) cout << "a = " << a << "  b = " << b << "  ret = " << sub[a][b] << endl;
		
		int ret = 0;
		REP(i, s.sz) {
			ret += cnt(sub[0][i+1], i+1);
			//cout << x << endl;
		}

			
		cout << "Case #" << iCase + 1 << ": " << ret << endl;
	}
		
	
	return 0;
}
