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
		LL N, D, G;
		cin >> N >> D >> G;
		bool ok = 1;
		LL n;
		if (D == 0) n = 1;
		else n = 100/gcd(D, 100LL);
		if (n > N) ok = 0;
		if ((D!=100 && G==100) || (D!=0&&G==0)) ok = 0;
		puts(ok?"Possible":"Broken");
		//printf(ok?"Possible":"Broken");
		//if (yes) puts(" yes"); else puts(" no");
	}
	return 0;
}
