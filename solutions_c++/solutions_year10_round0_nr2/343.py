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

#define forn(X,Y) for (int X = 0;X < Y;X++)
#define debug(x) cout << '>' << #x << ':' << x << '\n';

#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define reset(Z,Y) memset(Z,Y,sizeof(Z))

#define sz(Z) ((int)Z.size())
#define all(W) W.begin(), W.end()
#define pb push_back

#define mp make_pair
#define A first
#define B second

#define inf 1023123123
#define eps 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

ll gcd(ll abc, ll def) {
	if (abc < def) return gcd(def,abc);
	if (!def) return abc;
	return gcd(def,abc % def);
	}

int main() {
	
	int y,n,m;
	ll event[2050];
	scanf("%d",&y);
	forn(z,y) {
		printf("Case #%d: ",z+1);
		scanf("%d",&n);
		forn(i,n) scanf("%I64d",&(event[i]));
		ll tryans = 0LL;
		forn(i,n) forn(j,n) tryans = max(tryans,abs(event[i]-event[j]));
		//debug(tryans);
		forn(i,n) forn(j,n) tryans = gcd(tryans,abs(event[i]-event[j]));
		//debug(tryans);
		ll ret = event[0] % tryans;
		printf("%I64d\n",(tryans - ret) % tryans);
		}
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









