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

const 	int BIG = 100000000;



int 	a[1000000];
int 	cg[1000000];
int 	best[1000000][2];

int main ()
{ 
	freopen ( "1.in", "r", stdin );
	freopen ( "1.out", "w", stdout );
	int 	rr = 0;
	cin >> rr;
	while ( rr -- )
	{
		memset ( a, 0, sizeof ( a ) );
		memset ( cg, 0, sizeof ( cg ) );
		memset ( best, 0, sizeof ( best ) );
		int 	n, v;
		cin >> n >> v;
		for ( int i = 0; i < n / 2; i ++ )
		{
			cin >> a[i] >> cg[i];
		}
		for ( int i = n / 2; i < n; i ++ )
		{
			cin >> a[i];
			best[i][a[i]] = 0;
			best[i][1 - a[i]] = BIG;
		}
		for ( int i = n / 2 - 1; i >= 0; i -- )
		{
			int 	l, r ;
			l = i * 2 + 1;
			r = l + 1;
			best[i][0] = best[i][1] = BIG;
			if ( a[i] == 0 )
			{
				for ( int t1 = 0; t1 <= 1; t1 ++ )
				for ( int t2 = 0; t2 <= 1; t2 ++ )
				for ( int t3 = 0; t3 <= 1; t3 ++ )
				if ( t1 == (t2 ||t3 ))
				{
					best[i][t1] = min ( best[i][t1], best[l][t2] + best[r][t3] );
				}
			}
			else
			{
				for ( int t1 = 0; t1 <= 1; t1 ++ )
				for ( int t2 = 0; t2 <= 1; t2 ++ )
				for ( int t3 = 0; t3 <= 1; t3 ++ )
				if ( t1 == (t2 && t3) )
				{
					best[i][t1] = min ( best[i][t1], best[l][t2] + best[r][t3] );
				}
			}
			if ( cg[i] )
			{
				if ( a[i] == 0 )
				{
					for ( int t1 = 0; t1 <= 1; t1 ++ )
					for ( int t2 = 0; t2 <= 1; t2 ++ )
					for ( int t3 = 0; t3 <= 1; t3 ++ )
					if ( t1 == (t2 && t3) )
					{
						best[i][t1] = min ( best[i][t1], best[l][t2] + best[r][t3] + 1 );
					}
				}
				else
				{
					for ( int t1 = 0; t1 <= 1; t1 ++ )
					for ( int t2 = 0; t2 <= 1; t2 ++ )
					for ( int t3 = 0; t3 <= 1; t3 ++ )
					if ( t1 == (t2 || t3) )
					{
						best[i][t1] = min ( best[i][t1], best[l][t2] + best[r][t3] + 1 );
					}
				}
			}
		}
		if ( best[0][v] < BIG )
			cout << nc() << best[0][v] << endl;
		else
			cout << nc () << "IMPOSSIBLE" <<endl;





















	}
//	cout << nc ( 100 ) << endl;
//	cout << nc () << endl;
}
