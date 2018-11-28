#include <fstream>
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
#include <cstring>

using namespace std;

typedef long long			ll;
typedef vector<int>			vi;
typedef pair<int, int>		ii;
typedef vector<ii>			vii;
typedef set<int>			si;
typedef map<string, int>	msi;

#define REP(i, a, b) for (int i = int(a); i < int(b); i++)
#define TRvi(c, it)  for (vi::iterator it = (c).begin(); it != (c).end(); it++)

#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traverse containers
#define pb push_back
#define mp make_pair

#define dbg(x) cout << #x << " = " << x << "\n";
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << "\n";
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "\n";
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w << "\n";

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a, b, sizeof a)

int main() {
	int t;
	ll n, pd, pg;
	scanf("%d", &t);
	REP(i, 0, t) {
		scanf("%lld %lld %lld", &n, &pd, &pg);
		
		if ((pg == 0 and pd != 0) || (pg == 100 and pd != 100)) {
			printf("Case #%d: Broken\n", i + 1);
			continue;
		}
		
		if (pd == 100) {
			printf("Case #%d: Possible\n", i + 1);
			continue;
		}
		
		ll g = __gcd( 100LL , pd );
		pd/=g;
		ll c2 = 100LL/g; 
	
		if (c2 <= n and c2 > pd )
			printf("Case #%d: Possible\n", i + 1);
		else
			printf("Case #%d: Broken\n", i + 1);
	}
	
	return 0;
}