#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

int x[55];
int v[55];

int race(int N, int K, int B, int T) {
	int res = 0;
	int cand = 0;
	int i,j;

	//cout << N << ' ' << K << ' ' << B << ' ' << T << endl;

	for (i = N - 1; i >= 0; --i) {
		if (cand == K)
			break;
		if (x[i] + v[i] * T >= B) {
			++cand;
			//cout << "p ";
		} else {
			res += i;
			//cout << "n ";
		}

		if (cand == K)
			break;
	}
	//cout << endl << i << endl;

	if (i < 0)
		return -1;

	if (cand == 0)
		return 0;

	int non_cand = N - i - K;

	FOR(j,i,i+non_cand-1) {
		res -= j;
	}

	return res;
}

void main() {
	int C;
	int N,K,B,T;
	int i,j;

	scanf("%d", &C);

	REP(i,C) {
		scanf("%d %d %d %d", &N, &K, &B, &T);

		REP(j, N)
			scanf("%d", &x[j]);
		REP(j,N)
			scanf("%d", &v[j]);

		int res = race(N,K,B,T);
		//cout << "ha" << res << endl;

		if (res == -1)
			cout << "Case #" << (i+1) << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << (i+1) << ": " << res << endl;
	}
}