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

struct seg{
	int st, ed, w;
	seg(){}
	seg(int st, int ed, int w):st(st),ed(ed),w(w){}
	bool operator<(const seg &S)const{
		return w < S.w;
	}
};

int main(int argc, char **argv){
	int T;
	cin >> T;
	FOR(Ca, 1, T+1){
		printf("Case #%d: ", Ca);
		int L, S, R, tt, N;
		cin >> L >> S >> R >> tt >> N;
		double t = tt;
		vector<seg> SS(N);
		FOR(i, 0, N) cin >> SS[i].st >> SS[i].ed >> SS[i].w, L -= SS[i].ed - SS[i].st;
		if (L) SS.push_back(seg(0, L, 0));
		sort(ALL(SS));
		double res = 0;
		FOR(i, 0, SS.size()){
			int L1 = SS[i].ed - SS[i].st, ww = SS[i].w;
			if (t - 1. * L1 / (ww + R) > -eps){
				t -= 1. * L1 / (ww + R);
				res += 1. * L1 / (ww+R);
			}else{
				double L2 = (ww + R) * t;
				res += t;
				t = 0;
				double L3 = L1 - L2;
				res += L3 / (ww + S);
			}
		}
		printf("%.12f\n", res);
	}
	return 0;
}
