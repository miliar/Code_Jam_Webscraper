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
#define eps 1e-9
#define FOR(x, s, e) for(int x = (s); x < (e); ++x)
#define FORc(x, s, e, c) for(int x = (s); x < (e) && (c); ++x)
#define STEP(x, s, e, d) for(int x = (s); x < (e); x+=(d))
#define ROF(x, s, e) for(int x = (s); x >= (e); --x)
#define ROFc(x, s, e, c) for(int x = (s); x >= (e) && (c); --x)
#define vb vector<bool>
#define vi vector<int>
#define vii vector<pair<int, int> >
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define LL long long
#define pii pair<int, int>
#define x first
#define y second
#define gcd(x, y) __gcd((x), (y))
#define countbit(x) __builtin_popcount(x)

using namespace std;

int main(int argc, char **argv){
	int T;
	cin >> T;
	FOR(Ca, 1, T+1){
		printf("Case #%d: ", Ca);
		int C, D;
		cin >> C >> D;
		vi seq;
		FOR(i, 0, C){
			int P, V;
			cin >> P >> V;
			FOR(j, 0, V) seq.pb(P);
		}
		if (seq.size() == 1){ puts("0"); continue;}
		double lo = 0, hi = 1e20, res = 1e60;
		int M = seq.size();
		FOR(tt, 0, 100){
			double mi = (hi+lo)/2.;
			double pos[M];
			pos[0] = seq[0] - mi;
			bool ok = 1;
			FORc(i, 1, M, ok){
				pos[i] = pos[i-1] + D;
				double time = fabs(pos[i] - seq[i]);
				if (mi - time >= eps){
				}else{
					if (pos[i] - seq[i] > eps) ok = 0;
					else pos[i] = seq[i] - mi;
				}
			}
			if (ok){
				hi = mi;
				if (res - mi > eps) res = mi;
			}else lo = mi;
		}
		printf("%.10f\n", res);
	}
	return 0;
}
