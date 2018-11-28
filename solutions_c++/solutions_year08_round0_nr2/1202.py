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






pair< int, int > 	get ()
{
	int 	a, b, c, d;
	scanf ( "%d:%d %d:%d", & a, & b, & c, & d );
	return make_pair ( a * 60 + b , c * 60 + d );
}



int main ()
{
	freopen ( "1.in", "r", stdin );
		freopen ( "1.out", "w", stdout );
	int 	rr;
	int 	nrr=0;
	cin >> rr;
	while ( rr -- )
	{
		nrr ++;
		int 	sep = 0;
		cin >> sep;
		vector < pair < int, int > > 	a, b;
		int 	n, m;
		cin >> n >> m;
		while ( n -- )
			a . push_back ( get () );
		while ( m -- )
			b . push_back ( get () );
		sort ( a . begin (), a . end () );
		sort ( b . begin (), b . end () );
		int 	na = 0, nb = 0;
		while ( ! a . empty () || ! b . empty () )
		{
			if ( ! a . empty () && (b . empty () || a[0] . first < b[0] . first ) )
			{
				na ++;
				int 	t = a[0] . second;
				a . erase ( a . begin () );
				t += sep;
				while ( 1 )
				{
					for ( int i = 0; i < ( int ) b . size (); i ++ )
					{
						if ( b[i] . first >= t )
						{
							t = b[i] . second + sep;
							b . erase ( b . begin () + i );
							goto xxxx;
						}
					}
					break;
					xxxx:
					for ( int i = 0; i < ( int ) a . size (); i ++ )
					{
						if ( a[i] . first >= t )
						{
							t = a[i] . second + sep;
							a . erase ( a . begin () + i );
							goto oooo;
						}
					}
					break;
					oooo:;
				}
			}
			else
			{
				nb ++;
				int 	t = b[0] . second;
				b . erase ( b . begin () );
				t += sep;
				while ( 1 )
				{
					for ( int i = 0; i < ( int ) a . size (); i ++ )
					{
						if ( a[i] . first >= t )
						{
							t = a[i] . second + sep;
							a . erase ( a . begin () + i );
							goto xxx;
						}
					}
					break;
					xxx:
					for ( int i = 0; i < ( int ) b . size (); i ++ )
					{
						if ( b[i] . first >= t )
						{
							t = b[i] . second + sep;
							b . erase ( b . begin () + i );
							goto ooo;
						}
					}
					break;
					ooo:;
				}
			}
		}
		cout << "Case #" << nrr << ": " << na << " " << nb << endl;
	}
//	cout << my_answer;
//	for ( int i = 0; i < ( int ) my_answer . size (); i++ )	cout << my_answer[i] << endl;
}
