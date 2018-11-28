#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef long long lint;

#define mp make_pair
#define pb push_back
#define two(x) (1<<(x))
#define sq(a) (a)*(a)
#define all(c) (c).begin(),(c).end()
#define For(i,b,e) for(int i = b;i < e;i ++)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
const double PI = acos(-1.0);
#define INF 1000000000

int k;	
char st[1024];
char buf[1024];
int f[5];
bool used[5];
int nowmin, len, n;

void read_it()
{
	scanf( "%d %s", &k, st );
	nowmin = INF;
	memset( used, 0, sizeof( used ) );
	len = strlen( st );
	n = len / k;
}

void test_it()
{
	int i, j;
	for( i = 0; i < len; i += k )
	{
		for( j = 0; j < k; ++j )
			buf[i+j] = st[i + f[j]];
	}
	j = 0;
	for( i = 1; i < len; ++i )
		if( buf[i] != buf[i-1] )
			++j;
	++j;
	if( j < nowmin )
		nowmin = j;
}

void try_it( int p )
{
	if( p == k )
	{
		test_it();
		return;
	}
	for( int i = 0; i < k; ++i )
		if( !used[i] )
		{
			used[i] = true;
			f[p] = i;
			try_it( p + 1 );
			used[i] = false;
		}
}

void make_it()
{
	try_it( 0 );
	printf( "%d\n", nowmin );
}

int main()
{
	freopen( "data5.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	int c;
	scanf( "%d", &c );
	for( int i = 0; i < c; ++i )
	{
		printf( "Case #%d: ", i + 1 );
		read_it();
		make_it();
	}
	return 0;
}