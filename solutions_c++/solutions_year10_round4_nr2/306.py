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

#define inf 523123123
#define eps 1e-11

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;

int dp[1050][1050][30]; //tim dari a sampe b, tiket uda c yang diskip
int price[1050][1050];

int skip[1050];

int recurse(int a, int b, int c) {
	
	if (dp[a][b][c] != -1) return dp[a][b][c];
	//debug(a);
	//debug(b);
	rep(i,a,b+1) if (c > skip[i]) {
		dp[a][b][c] = inf;
		return inf;
		}
	
	if (a == b) return 0;
	//coba diskip
	int dx = (b-a+1)/2;
//	debug(a);
//	debug(b);
//	debug(dx);
	dp[a][b][c] = min(recurse(a,a+dx-1,c+1) + recurse(a+dx,b,c+1),
					  recurse(a,a+dx-1,c) + recurse(a+dx,b,c) + price[a][b]);
	return dp[a][b][c];
	}

int main() {
	
	
	
	int nc;
	scanf("%d",&nc);
	forn(z,nc) {
		printf("Case #%d: ",z+1);
		reset(dp,-1);
		
		int p;
		cin >> p;
		//debug(p);
		forn(i,1 << p) cin >> skip[i];
		int mult = 2;
		int n = 1 << p;
		while (mult <= n) {
			int angka = 0;
			while (angka < n) {
				cin >> price[angka][angka + mult-1];
			//	debug(angka);
			//	debug(angka+mult-1);
				angka += mult;
				}
			mult *= 2;
			}
		printf("%d\n",recurse(0,n-1,0));
		}
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









