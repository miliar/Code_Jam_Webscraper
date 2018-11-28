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
	tmp << "Case #" << number << ": ";
	string 	str;
	getline ( tmp, str );
	return 	str;
}

inline  int 	cha ( int a, int b, int c, int d )
{
	return a * d - b * c ;
}
inline int 	calcarea ( int a, int b, int c, int d, int e, int f )
{	return abs ( cha ( c - a , d - b, e - a, f  - b ) );
}




int main ()
{
	freopen ( "1.in", "r", stdin );
	freopen ( "1.out", "w", stdout );
	int 	rr = 0;
	cin >> rr;
	while ( rr -- )
	{
		cerr << rr << endl;
		int 	n, m, a;
		cin >> n >> m >> a;
		for ( int i1 = 0; i1 <= n; i1 ++ )
		for ( int i2 = 0; i2 <= m; i2 ++ )
		for ( int i3 = 0; i3 <= n; i3 ++ )
		for ( int i4 = 0; i4 <= m; i4 ++ )
		{
			if ( calcarea ( i1,0, 0, i2, i3, i4 ) == a )
			{
				cout << nc ();
				printf ( "%d %d %d %d %d %d\n", i1,0, 0,i2 , i3, i4 );
				goto end;
			}
		}
		cout << nc ();
		cout << "IMPOSSIBLE" << endl;
		
		end:;





















	}
//	cout << nc ( 100 ) << endl;
//	cout << nc () << endl;
}
