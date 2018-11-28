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
#include <climits>
#include <string>
#include <cstring>
using namespace std;

#define forn(a, n) for(int (a) = 0; (a) < (n); ++(a))
#define dforn(a, n) for(int (a) = (n-1); (a) >= 0; --(a))

#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define dforsn(a, s, n) for(int (a) = (s-1); (a) >= (n); --(a))

#define forall(a, b) for(typeof(b.begin()) a = b.begin(); a != b.end(); ++a)
#define dforall(a, b) for(typeof(b.rbegin()) a = b.rbegin(); a != b.rend(); ++a)
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

int t, d, ii, m, n, arr[105], dp[105][260];

int calc(int pos, int last)
{
	if(pos == n) return 0;
	int& ret = dp[pos][last+1];
	if(ret != -1) return ret;
	
	ret = calc(pos+1, last)+d;
	
	if(last != -1 && abs(arr[pos]-last) <= m)
		ret <?= calc(pos+1, arr[pos]);
	
	forn(nv, 256) 
	{
		if(last == -1 || abs(last-nv) <= m)
			ret <?= calc(pos+1, nv)+abs(arr[pos]-nv);
		if(last != -1 && abs(last-nv) <= m && nv != last)
			ret <?= calc(pos, nv)+ii;
	}
	
	return ret;
}

int main()
{
#ifdef TAVO92
	freopen("B-large.in" , "r" , stdin);
	freopen("B-large.out", "w" , stdout);
#endif

	scanf("%i", &t);
	
	forn(p, t)
	{
		scanf("%i%i%i%i", &d, &ii, &m, &n);
		forn(i, n) scanf("%i", &arr[i]);
		
		memset(dp, -1, sizeof(dp));
		printf("Case #%i: %i\n", p+1, calc(0, -1));
	}
	
	return 0;
}
