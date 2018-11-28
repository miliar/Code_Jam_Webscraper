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
#define dforn(a, n) for(int (a) = (n); (a) >= 0; --(a))

#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define dforsn(a, s, n) for(int (a) = (s); (a) >= (n); --(a))

#define forall(a, b) for(typeof(b.begin()) a = b.begin(); a != b.end(); ++a)
#define dforall(a, b) for(typeof(b.rbegin()) a = b.rbegin(); a != b.rend(); ++a)
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

int main()
{
#ifdef TAVO92
	freopen("A-small.in" , "r" , stdin);
//	freopen("A-small.out", "w" , stdout);
#endif
	
	int t;
	tint n, k;
	scanf("%i", &t);
	
	forn(p, t)
	{
		scanf("%lld%lld", &n, &k);
		tint turn = (1LL<<(n));
		
		printf("Case #%i: %s\n", p+1,  (k+1LL)%turn==0LL ? "ON" : "OFF");
	}

	return 0;
}
