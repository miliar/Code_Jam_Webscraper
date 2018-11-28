// includes + defines {{{
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#define REP(i, n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define FORD(i, a, b) for(int i = (int)(a); i >= (int)(b); --i)
#define FORE(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SIZE(x) ((int)((x).size()))
#define DEBUG(x) { cout << #x << ": " << (x) << endl; }
#define SQR(x) ((x) * (x))
#define INF 1023456789
using namespace std;
// }}}

int main(){
	int C;
	cin >> C;
	FOR(qi, 1, C){
		int N, K, B, T;
		cin >> N >> K >> B >> T;
		vector<int> X(N), V(N);
		REP(i, N)
			cin >> X[i];
		REP(i, N)
			cin >> V[i];

		int res = 0, zle = 0, dobre = 0;
		for(int i = N - 1; i >= 0 && dobre < K; --i)
			if(B - X[i] > V[i] * T)
				++zle;
			else{
				++dobre;
				res += zle;
			}

		if(dobre == K)
			cout << "Case #" << qi << ": " << res << endl;
		else
			cout << "Case #" << qi << ": IMPOSSIBLE" << endl;
	}
}
