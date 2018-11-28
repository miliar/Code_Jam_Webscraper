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
long long 	fa[2000000];
long long 	getfa ( long long t )
{
	if ( fa[t] == t )
		return t;
	fa[t] = getfa ( fa[t] );
	return getfa ( fa[t] );
}
void 	combine ( long long a, long long b )
{
	fa[getfa ( a)] = getfa ( b );
}

void 	process ( long long p, long long a, long long b )
{
	for ( long long i = a / p * p; i <= b; i += p )
	{
		if ( i >= a && i + p <= b )
			combine ( i - a, i - a + p );
	}
}

long long 	prime ( long long t )
{
	for ( long long i = 2; i * i <= t; i ++ )
		if ( t % i == 0 )
			return false;
	return true;
}

int main ()
{
	freopen ( "1.in", "r", stdin );
	freopen ( "1.out", "w", stdout );
	long long 	rr = 0;
	cin >> rr;
	vector < long long > 	pr;
	for ( long long i = 2; i <= 1000000; i ++ )
		if ( prime ( i ) )
			pr . push_back ( i );
	while ( rr -- )
	{
		memset ( fa, 0, sizeof ( fa ) );
		for ( long long i = 0; i < 2000000; i ++ )
			fa[i] = i;
		long long 	a, b, p;
		cin >> a >> b >> p;
		for ( long long i = 0; i < ( long long ) pr . size (); i ++ )
		{
			if ( pr[i] >= p )
			{
				process ( pr[i], a, b );
			}
		}
		long long 	ans  =  0;
		for ( long long i = 0; i < b - a + 1; i ++ )
			if ( getfa(i) == i )
				ans ++;
			cout << nc () << ans << endl;





















	}
//	cout << nc ( 100 ) << endl;
//	cout << nc () << endl;
}
