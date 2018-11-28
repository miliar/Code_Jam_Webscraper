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

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi;
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 

#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)
#define watcharr(i, x) TRACE(cout << #x" = "); rep(i, sz(x)) cout << x[i] << " "; cout << endl

int main() {
	
	int T, R, k, N, g[1000];

	cin >> T;

	bool usd[1000];
	int gp[1000];
	int fs[1000];

	rep(cs, T) {
		
		cin >> R >> k >> N;
		rep(i, N) cin >> g[i], gp[i] = 0, fs[i] = 0, usd[i] = false;

		long long ret;

		int gpi = 0, si = 0;
		while(!usd[si]) {
			int i = si, tot = 0;
			bool tmp_usd[1000] = {};
			while(true) {
				if(tot + g[i] > k || tmp_usd[i]) {
					gp[gpi] = tot;
					usd[si] = true;
					fs[si] = gpi;
					gpi++;
					si = i;
					break;
				}
				tot += g[i];
				tmp_usd[i] = true;
				i = (i + 1) % N;
			}
		}
		int fst = fs[si];
	
		int tSum1 = 0, tSum2 = 0;
		rep(i, fst) tSum1 += gp[i];
		for(int i = fst; i < gpi; i++) tSum2 += gp[i];

		if(R <= fst) rep(i, R) ret += (long long) gp[i];
		else {
			int lt = R - fst, n = gpi - fst;
			ret = (long long) tSum1 + (long long) (lt / n) * (long long) tSum2;
			for(int i = fst; i < fst + (lt % n); i++) ret += gp[i];
		}

		cout << "Case #" << (cs + 1) << ": " << ret << endl;
	}
	
	return 0;
	
}

