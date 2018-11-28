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
int 	noword ( string t )
{
	for ( int i = 0; i < ( int ) t . size (); i ++ )
	{
		if ( t[i] >= 'a' && t[i] <= 'z' )return false;
		if ( t[i] >= 'A' && t[i] <= 'Z' )return false;
	}
	return true;
}

string 	nc ( int next = 1 )
{
	static 	int 	number = 0;
	number += next;
	stringstream 	tmp;
	tmp << "Case #" << number << ":";
	string 	str;
	getline ( tmp, str );
	return 	str;
}

int 	a[2000000];
int 	low ( int t )
{
	return t & ( t ^ ( t - 1 ) );
}
int 	sum ( int end )
{
	end ++;
	int 	sum = 0;
	while ( end > 0 )
	{
		sum += a[end];
		end -= low(end);
	}
	return sum;
} 

void 	pluss( int pos , int num)
{
	pos ++;
	while(pos <= 1000000)
	{
		a[pos] += num;
		pos += low(pos);
	}
} 


int 	fr ( int t )
{
	return t - sum ( t ) ;
}
int 	ans[2000000];
int 	search ( int  t, int l, int r )
{
	int 	mid = ( l  + r ) / 2;
	if ( fr ( mid ) == t && fr ( mid - 1 ) < t ) 
		return 	mid;
	if ( fr ( mid ) >= t )
		return search ( t, l, mid - 1 );
	return search ( t, mid + 1, r );
}
int main ()
{
	freopen ( "1.in", "r", stdin );
	freopen ( "1.out", "w", stdout );
	int 	rr = 0;
	cin >> rr;
	while ( rr -- )
	{
		memset ( a, 0, sizeof ( a ) );
		memset ( ans, 0, sizeof ( ans ) );
		int 	n;
		cin >> n;
		int 	pr = 0;
		for ( int i = 1; i <= n; i ++ )
		{
			if ( i % 1000 == 0  )
				cerr << i << endl;
			int 	place = 0;
			if ( i > 1 )
				place = fr ( pr ) + i;
			if ( place >= n - i + 1 )
			{
				place %= ( n - i + 1 );
			}
			place = search ( place, 0, n - 1 );

			pluss ( place, 1 );
			ans[place] = i;
			pr = place;
		}
		cin >> n;
		cout << nc ();
		for ( int i = 0; i < n; i ++ )
		{
			int 	t;
			cin >> t;
			cout << " " << ans[t - 1];
		}
cout << endl;



















	}
//	cout << nc ( 100 ) << endl;
//	cout << nc () << endl;
}
