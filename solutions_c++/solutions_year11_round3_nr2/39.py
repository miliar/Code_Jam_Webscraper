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
		LL L, t, N, C;
		cin >> L >> t >> N >> C;
		vector<LL> D(N), A(C);
		FOR(i, 0, C) cin >> A[i];
		FOR(i, 0, C)
			FOR(k, 0, N){
				LL x = k*C + i, y = k*C + i + 1;
				if (x >= N) break;
				D[x] = A[i];
			}
		//FOR(i, 0, N) cout << D[i] << " "; puts("");
		LL res = 0;
		FOR(i, 0, N) res += D[i];
		LL tmp = 0, remain = L;
		vector<LL> R;
		FOR(i, 0, N){ 
			tmp += D[i]*2;
			if (tmp == t){
				FOR(j, i+1, N) R.pb(2*D[j]);
				break;
			}else if (tmp > t){
				tmp -= D[i] * 2;
				LL del = t - tmp;
				tmp = t;
				R.pb(D[i]*2-del);
				FOR(j, i+1, N) R.pb(2*D[j]);
				break;
			}
		}
		sort(ALL(R));
		reverse(ALL(R));
		FOR(i, 0, R.size()){
			if (remain){
				remain--;
				tmp += R[i]/2;
			}else tmp += R[i];
		}
		cout << tmp << endl;
	}
	return 0;
}
