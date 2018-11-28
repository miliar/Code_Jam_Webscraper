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
#define LL long long
#define pii pair<int, int>
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define countbit(X) __builtin_popcount(X)
#define gcd(x, y) __gcd(x, y)
#define x first
#define y second

using namespace std;

int main(int argc, char **argv){
	int T;
	cin >> T;
	FOR(Ca, 1, T+1){
		printf("Case #%d: ", Ca);
		int N, V=0, U=0;
		LL s = 0, res=0;
		cin >> N;
		vi S(N);
		FOR(i, 0, N) cin >> S[i], V ^= S[i], s += S[i];
		if (V){ puts("NO"); continue;}
		sort(ALL(S));
		LL ss = s;
		FOR(i, 0, N-1){
			V ^= S[i], U ^= S[i], ss -= S[i];
			if (V == U) res = max(res, max(ss, s-ss));
		}
		cout << res << endl;
	}
	return 0;
}
