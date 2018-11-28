#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>

using namespace std;

#define LL long long

LL a[100], A[100], b[100], B[100];

LL max( LL a , LL b )
{
	return a > b ? a : b;
}
LL min( LL a , LL b )
{
	return a < b ? a : b;
}

LL mem[110][110];
int n, m;

LL f( int x , int y )
{
	if( x >= n || y >= m )
		return 0;
	LL res = 0;
	if( A[x] == B[y] )
	{
		LL r = min( a[x] , b[y] );
		a[x] -= r;
		b[y] -= r;
		if( a[x] )
			res = r + f( x , y+1 );
		else
			res = r + f( x+1 , y );
		a[x] += r;
		b[y] += r;
	}
	else
		res = max( res , max( f( x+1 , y ) , f( x , y+1 ) ) );
	return res;
}

int main()
{
	freopen( "in.txt" , "r" , stdin );
	freopen( "outc.out" , "w" , stdout );
	int t;
	cin >> t;
	for( int tc = 1 ; tc <= t ; tc ++ )
	{
		LL res = 0;
		cin >> n >> m;
		for( int i = 0 ; i < 3 ; i ++ )
			a[i] = A[i] = 0;
		for( int i = 0 ; i < 100 ; i ++ )
			b[i] = B[i] = 0;
		for( int i = 0 ; i < n ; i ++ )
			cin >> a[i] >> A[i];
		for( int i = 0 ; i < m ; i ++ )
			cin >> b[i] >> B[i];
		res = f( 0 , 0 );
		cout << "Case #" << tc << ": " << res << endl;
	}
	return 0;
}