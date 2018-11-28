#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>


#define debug(x) cout << '>' << #x << ':' << x << '\n';
#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define forn(X,Y) for (int X = 0;X < Y;X++)
#define sz(Z) Z.size()
#define all(W) W.begin(), W.end()
#define inf 2123123123LL
#define eps 0.0000001
#define vint vector<int>
#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)
#define mp make_pair
#define I(M) (typeof((M).begin()))
#define pb push_back

#define pipii pair< int, pair<int, pair<int, pair<int,int> > > >

typedef long long ll;
typedef long double ld;

using namespace std;

int x[1000];
int y[1000];
int r[1000];

int main() {
	
	int zz;
	
	scanf("%d",&zz);
	
	forn(z,zz) {
		printf("Case #%d: ",z + 1);
		
		int n;
		scanf("%d",&n);
		forn(i,n) scanf("%d%d%d",&x[i],&y[i],&r[i]);
		int maxr = 0;
		forn(i,n) maxr = max(maxr,r[i]);
		
		if (n <= 2) {
			printf("%d\n",maxr);
			continue;
			}
		double best = inf;
		forn(i,3) forn(j,3) forn(k,3) {
			if (i == j || j == k || k == i) continue;
			best = fmin(best,fmax( (double)r[k], (double) ((sqrt ( (double) (x[i] - x[j]) * (double) (x[i] - x[j]) + 
			(double) (y[i] - y[j]) * (double) (y[i] - y[j])) + (double) r[i] + (double) r[j]) / 2.0)));
			}
		printf("%lf\n",best);
		}
		

	}

