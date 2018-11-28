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
	forn(z,nc) {
		printf("Case #%d: ",z+1);
		int del,ins,smooth,n;
		scanf("%d%d%d%d",&del,&ins,&smooth,&n);
		vint val;
		forn(i,n) {
			int x;
			scanf("%d",&x);
			val.pb(x);
			}
		int dp[115][300]; //last post, last digit, isempty
		forn(i,105) forn(j,300) dp[i][j] = inf;
		forn(i,256) dp[0][i] = 0;
		rep(i,1,n+1) {
			int cun = val[i-1];
			//ambil dari belakang
			forn(k,256) if (abs(k-cun) <= smooth) MN(dp[i][cun],dp[i-1][k]);	
			//coba didelete yg ini
			forn(j,256) MN(dp[i][j],dp[i-1][j] + del);
			//coba dirubah angkanya
			forn(j,256) forn(k,256) if (abs(j-k) <= smooth) MN(dp[i][j],dp[i-1][k] + abs(j-cun));
			//coba diinsert angka baru
			forn(l,256 / ((smooth==0)?1:smooth) + 2) forn(j,256) forn(k,256) if (abs(k-j) <= smooth) MN(dp[i][j],dp[i][k] + ins);
			}
		int cheapest = inf;
		forn(i,256) MN(cheapest,dp[n][i]);
		printf("%d\n",cheapest);
		}
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









