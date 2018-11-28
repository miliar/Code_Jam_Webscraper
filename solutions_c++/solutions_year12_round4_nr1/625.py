#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

int t, n;
tint d[10004], l[10004], D, best[10004];
map<tint, int> dp[10004];

int calc(int pos, tint v){
	if(d[pos]+v >= D) return 1;
	if(v < best[pos]) return 0;
	best[pos] = v;
	
	if(dp[pos].count(v)) return dp[pos][v];
	int &ret = dp[pos][v];
	ret = 0;
	
	forsn(i, pos+1, n){
		if(d[i] <= d[pos]+v){
			if(calc(i, min(min(v, l[i]), d[i]-d[pos])) == 1){
				ret = 1;
				break;
			}
		}else
			break;
	}
	
	return ret;
}

int main()
{
#ifdef __YO__
	freopen("A-small.in", "r", stdin);
	freopen("A-small2.out", "w", stdout);
#endif
	
	cin >> t;
	forn(T, t){
		cin >> n;
		forn(i,n) cin >> d[i] >> l[i];
		cin >> D;
		
		cerr << T << " " << n << endl;
		
		forn(i, n) dp[i].clear();
		memset(best, 0, sizeof(best));
		int ret = calc(0, d[0]);
		
		cout << "Case #" << T+1 << ": " << (ret == 0 ? "NO" : "YES") << endl;
	}

	return 0;
}
