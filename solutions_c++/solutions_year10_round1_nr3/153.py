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

typedef struct caso
{
	int a, b, turno;
	
	caso(int w, int e, int r) {a = w; b = e; turno = r;}
};

bool operator<(const caso& c0, const caso& c1)
{
	if(c0.a != c1.a)
		return c0.a < c1.a;
	if(c0.b != c1.b)
		return c0.b < c1.b;
	return c0.turno < c1.turno;
}

int t, a1, a2, b1, b2;
map<caso, bool> dp;

bool works(int a, int b, int tur)
{
	caso cc = caso(a, b, tur);
	if(dp.count(cc))
		return dp[cc];
	
	bool &ret = dp[cc];
	ret = false;
	
	if(a == 1 && b == 1)
		return (ret = false);
	else if(a == 1 || b == 1)
		return (ret = true);
	
	forsn(k, 1, INT_MAX)
	{
		bool ca = (a > k*b ? works(a-k*b, b, tur^1)^1 : false);
		bool cb = (b > k*a ? works(a, b-k*a, tur^1)^1 : false);
		
		ret = max(ret, max(ca, cb));
		
		if(k*b > a && k*a > b) break;
	}
	
	return ret;
}

int main()
{
#ifdef TAVO92
	freopen("C-small.in" , "r" , stdin);
	freopen("C-small.out", "w" , stdout);
#endif

	scanf("%i", &t);
	dp.clear();
	forn(p, t)
	{
		scanf("%i%i%i%i", &a1, &a2, &b1, &b2);
		
		int ret = 0;
		forsn(a, a1, a2+1) forsn(b, b1, b2+1)
		{
			ret += works(a, b, 0);
		}
		
		
		printf("Case #%i: %i\n", p+1, ret);
		cerr << p+1 << endl;
	}
	
	return 0;
}
