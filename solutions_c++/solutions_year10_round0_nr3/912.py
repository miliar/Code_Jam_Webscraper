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

int main() {
	
	int z,n,passenger,loops;
	ll nump[1050];
	ll dp[1050];
	ll found[1050];
	scanf("%d",&z);
	forn(y,z) {
		printf("Case #%d: ",y+1);
		scanf("%d%d%d",&loops,&passenger,&n);
		forn(i,n) scanf("%I64d",&(nump[i]));
		reset(dp,-1);
		reset(found,-1);
		ll curprofit = 0LL;
		int pos = 0;
		ll counter = 0;
		while (dp[pos] == -1LL && loops) {
			found[pos] = counter;
			counter++;
			dp[pos] = curprofit;
			//try riding
			int hepos = (pos+1)%n;
			ll numpeople = nump[pos];
			if (numpeople > passenger) {
				loops = 0;
				break;
				}
			loops--;
			while (hepos != pos) {
				if (numpeople + nump[hepos] > (ll)passenger) break;
				numpeople += nump[hepos];
				hepos++;
				hepos %= n;
				}
			//debug(numpeople);
			curprofit += (ll)numpeople;
			pos = hepos;
			}
		if (loops == 0) {
			//debug(loops);
			printf("%I64d\n",curprofit);
			continue;
			}
		int iteration = counter - found[pos];
		ll iterprofit = curprofit - dp[pos];
		curprofit += ((ll)loops / (ll)iteration) * (ll)iterprofit;
		loops %= (ll)iteration;
		while (loops) {
			int hepos = (pos+1)%n;
			ll numpeople = nump[pos];
			if (numpeople > passenger) {
				loops = 0;
				break;
				}
			loops--;
			while (hepos != pos) {
				if (numpeople + nump[hepos] > (ll)passenger) break;
				numpeople += nump[hepos];
				hepos++;
				hepos %= n;
				}
			curprofit += (ll)numpeople;
			pos = hepos;
			}
		printf("%I64d\n",curprofit);
		}
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









