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

bool vicinx(int a,int b,int turns) {
	if (a > b) return vicinx(b,a,turns);
	if (2*a <= b) return 1;
	if (turns == 0) return 0;
	return vicinx(b-a,a,turns-1);
	}

bool iswin(int a,int b) {
	if (a > b) return iswin(b,a);
	if (2*a <= b) return 1;
	if (a == b) return 0;
	return !iswin(b-a,a);
	}

int main() {
	
	int nc;
	scanf("%d",&nc);
	forn(z,nc) {
		printf("Case #%d: ",z+1);
		int a1,a2,b1,b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		ll ret = 0LL;
		rep(i,a1,a2+1) {
			rep(j,b1,b2+1) {
				if (iswin(i,j)) ret++;
				}
			}
		printf("%I64d\n",ret);
		}
	
	return 0;
	}


//Powered by [KawigiEdit] 2.0!









