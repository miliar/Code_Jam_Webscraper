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

using namespace std;
long long 	noword ( string t )
{
	for ( long long i = 0; i < ( long long ) t . size (); i ++ )
	{
		if ( t[i] >= 'a' && t[i] <= 'z' )return false;
		if ( t[i] >= 'A' && t[i] <= 'Z' )return false;
	}
	return true;
}

string 	nc ( long long next = 1 )
{
	static 	long long 	number = 0;
	number += next;
	stringstream 	tmp;
	tmp << "Case #" << number << ": ";
	string 	str;
	getline ( tmp, str );
	return 	str;
}


long long 	cc ( long long a, long long b )
{
	if ( b == 2 )
	{
		return a * ( a - 1 ) / 2;
	}
	else
		return ( a * ( a - 1 ) * ( a - 2 ) / 6 );
}

long long 	t[3][3];
void 	add ( long long x, long long y )
{
	t[x % 3][y % 3] ++;
}

int main ()
{
	freopen ( "1.in", "r", stdin );
	freopen ( "1.out", "w", stdout );
	long long 	rr = 0;
	cin >> rr;
	
	while ( rr -- )
	{
		memset ( t, 0, sizeof ( t ) );
		long long 	n,a, b, c, d, x, y, m;
		cin >>n >>a >> b >> c >> d >> x >> y >> m;
		add ( x, y );
		
		for ( long long i = 1; i < n; i ++ )
		{
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			add ( x, y );
		}
		long long 	ans= 0 ;
		ans += cc ( t[0][0], 3 );
		ans += cc ( t[0][1], 3 );
		ans += cc ( t[0][2], 3 );
		ans += cc ( t[1][0], 3 );
		ans += cc ( t[1][1], 3 );
		ans += cc ( t[1][2], 3 );
		ans += cc ( t[2][0], 3 );
		ans += cc ( t[2][1], 3 );
		ans += cc ( t[2][2], 3 );
		ans += t[0][0] * t[0][1] * t[0][2];
		ans += t[0][0] * t[1][0] * t[2][0];
		
		
		ans += t[1][0] * t[1][1] * t[1][2];
		ans += t[0][1] * t[1][1] * t[2][1];
		
		
		ans += t[2][0] * t[2][1] * t[2][2];
		ans += t[0][2] * t[1][2] * t[2][2];
		
		ans += t[0][0] * t[1][1] * t[2][2];
		ans += t[0][0] * t[1][2] * t[2][1];
		ans += t[0][1] * t[1][0] * t[2][2];
		ans += t[0][1] * t[1][2] * t[2][0];
		ans += t[0][2] * t[1][0] * t[2][1];
		ans += t[0][2] * t[1][1] * t[2][0];
		
		
		
		
		

		
		cout << nc () << ans << endl;
















	}
//	cout << nc ( 100 ) << endl;
//	cout << nc () << endl;
}
