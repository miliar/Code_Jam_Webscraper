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
#include <fstream>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

int ti[104], T, n, s, p;

int diff(int num, int di){
	int a = num/3, b = num/3, c = num/3;
	
	if(a+b+c == num){
		if(di == 1) return a;
		return a + (a>0);
	}else if(a+b+c+1 == num)
		return a+1;
	if(di == 1) return a+1;
	return c+2;
}

int dp[104][104];
int calc(int i, int k){
	if(i == n) return (k == 0 ? 0 : -INT_MAX);
	
	int &ret = dp[i][k];
	if(ret != -1) return ret;
	
	ret = calc(i+1, k) + (p <= diff(ti[i], 1));
	
	if(k > 0)
		ret = max(ret, calc(i+1, k-1) + (p <= diff(ti[i], 2))); 
	
	return ret;
}

int main()
{
#ifdef __YO__
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	
	scanf("%i", &T);
	
	forn(t, T){
		scanf("%i%i%i", &n, &s, &p);
		forn(i,n) scanf("%i", &ti[i]);
		memset(dp, -1, sizeof(dp));

		printf("Case #%i: %i\n", t+1, calc(0, s));
	}

	return 0;
}
