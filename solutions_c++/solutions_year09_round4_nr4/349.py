//AlexFetisov
//Accepted
//I'm Feeling Lucky!

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:128000000")

#include <iostream>

void initf()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string>
#include <cmath>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i)
#define fi(a) for ( int i = 0; i < ( a ); ++i)
#define fj(a) for ( int j = 0; j < ( a ); ++j)
#define fk(a) for ( int k = 0; k < ( a ); ++k)
#define CLR(a, b) memset( ( a ), ( b ), sizeof( ( a ) ) )
#define clr(a) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(),( v ).end()

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef vector < int > vi;
typedef pair < int, int > pii;

const int inf = 1 << 30;
const int MOD = 10000;

struct tpnt 
{
	double x, y;
};

struct circle
{
    tpnt p;
	double r;
};

double dst( tpnt p1, tpnt p2 )
{
	return ( hypot( p1.x - p2.x, p1.y - p2.y ) );
}


circle c[50];
int n;

void doit()
{
	cin >> n;
	fi( n )
	{
    	cin >> c[i].p.x >> c[i].p.y >> c[i].r;	
    }
    if ( n == 1 )
    {
    	printf("%.7lf\n", c[0].r);
    	return;
    }
    if ( n == 2 )
    {
    	printf("%.7lf\n", max( c[0].r, c[1].r ) );
    	return;
    }
    if ( n == 3 )
    {
    	
    	double best = 1e15;

    	best = min( best, max( c[0].r, (dst( c[1].p, c[2].p ) + c[1].r + c[2].r) / 2. ) );
    	best = min( best, max( c[1].r, (dst( c[0].p, c[2].p ) + c[0].r + c[2].r) / 2. ) );
    	best = min( best, max( c[2].r, (dst( c[1].p, c[0].p ) + c[1].r + c[0].r) / 2. ) );    
    	printf("%.7lf\n", best );
    	return;
    }
}

void solve()
{
	int test;
	scanf("%d", &test);
	fr(tst,1,test)
	{
		printf("Case #%d: ", tst );
		/////////////////////////////////////

		doit();

	}
}

int main()
{
	initf();
	solve();
	return (0);
}