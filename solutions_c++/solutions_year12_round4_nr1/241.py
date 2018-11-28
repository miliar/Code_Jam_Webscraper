#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <memory.h>
using namespace std;

#define fi first
#define sc second
#define mp make_pair
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define RESET(a,b) memset( (a), b, sizeof(a) )
#define ren(a,b,c) for (int a=b; a<c; ++a)
#define red(a,b,c) for (int a=b; a>=c; --a)
#define repi(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

const double eps = 1e-9;
typedef long long ll;
typedef pair <int,int> pii;

//lintaor1's template

/*
const bool operator< (const pii &a, const pii &b)
{
	if (a.fi != b.fi) return a.fi > b.fi;
	return a.sc > b.sc;
}
*/

void solve( const int& );

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.ou", "w", stdout );
	int T;
	cin >> T; ++T;
	ren (TT,1,T)
	{
		solve( TT );
	}
	return 0;
}

//-----
void solve( const int &T )
{
	int n, a, b;
	priority_queue < pii, vector<pii>, greater<pii> > pq;
	//priority_queue < pii > pq;
	pii cur;
	
	/*
	pq.push( mp( 5,8 ) );
	pq.push( mp( 6,7 ) );
	printf( "%d\n", mp( 5,8 ) < mp( 6,7 ) );
	while (!pq.empty())
	{
		cout << pq.top().fi << " " << pq.top().sc << endl;
		pq.pop();
	}
	*/
	
	cin >> n >> a >> b;
	//pq.push( mp( a, (a<<1) ) );
	cur = mp( a, (a<<1) );
	while (--n)
	{
		cin >> a >> b;
		//printf("-- %d %d\n", cur.fi, cur.sc);
		while (cur.sc < a && !pq.empty())
		{
			cur = pq.top();
			pq.pop();
			//printf("-- %d %d\n", cur.fi, cur.sc);
		}
		if (cur.sc >= a) pq.push( mp(a, a+min( a-cur.fi, b )) );
	}
	cin >> a;
	while (cur.sc < a && !pq.empty())
	{
		cur = pq.top();
		pq.pop();
		//printf("-- %d %d\n", cur.fi, cur.sc);
	}
	printf("Case #%d: ", T);
	if (cur.sc < a) printf("NO\n"); else printf("YES\n");
}
