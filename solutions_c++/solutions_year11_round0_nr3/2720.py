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

map<pair<int, int>, int> dp[1004][2][2];
int arr[1004],n;

int calc(int p, bool za, bool zb, int a, int b){
	if(p == n)
		return (a == b && za && zb ? 0 : -INT_MAX);
	
	pair<int, int> pi = make_pair(a,b);
	if(dp[p][za][zb].count(pi))
		return dp[p][za][zb][pi];
	
	int &ret = dp[p][za][zb][pi];
	ret = -INT_MAX;
	
	ret = max(calc(p+1, true, zb, a^arr[p], b)+arr[p], calc(p+1, za, true, a, b^arr[p]));
	return ret;
}

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	
	int T;
	scanf("%i", &T);
	
	forn(p, T){
		scanf("%i", &n);
		forn(i, n){
			scanf("%i", &arr[i]);
			forn(j, 2) forn(k, 2)
				dp[i][j][k].clear();
		}
		
		int ret = calc(0,false,false,0,0);
		printf("Case #%i: ", p+1);
		
		if(ret <= 0)
			printf("NO\n");
		else
			printf("%i\n", ret);
	}

	return 0;
}
