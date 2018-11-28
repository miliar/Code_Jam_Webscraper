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
	
	int nc;
	scanf("%d",&nc);
	
	int bakteri[500][500];
	int bakteri2[500][500];
	
	forn(z,nc) {
		printf("Case #%d: ",z+1);
		int n;
		cin >> n;
		vint x1,y1,x2,y2;
		forn(i,n) {
			int a,b,c,d;
			cin >> a >> b >> c >> d;
			x1.pb(a);
			y1.pb(b);
			x2.pb(c);
			y2.pb(d);
			}
		reset(bakteri,0);
		forn(i,n) {
			rep(j,x1[i],x2[i]+1) rep(k,y1[i],y2[i]+1) {
			//	debug(j);
			//	debug(k);
				bakteri[j][k] = 1;
				/*debug(j);
				debug(k);
				debug(bakteri[j][k]);*/
				}
			}
		int seconds = 0;
		while (1) {
			//ada kehidupan?
			int ishidup = 0;
			reset(bakteri2,0);
			forn(i,500) forn(j,500) if (bakteri[i][j]) {
				ishidup = 1;
				}
			
		
			
			if (!ishidup) break;
			seconds++;
			//debug("v\n");
			forn(i,500) forn(j,500) {
				
				if (bakteri[i][j]) 
					if ((i && bakteri[i-1][j]) || (j && bakteri[i][j-1])) bakteri2[i][j] = 1;
				if (i&&j&&bakteri[i-1][j]&&bakteri[i][j-1]) bakteri2[i][j] = 1;
				}
			forn(i,500) forn(j,500) bakteri[i][j] = bakteri2[i][j];
			
			//forn(i,500) bakteri[0][i] = bakteri[i][0] = 0;
			}
		printf("%d\n",seconds);
		}
		
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









