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










int main ()
{
	freopen ( "1.in", "r", stdin );
	freopen ( "1.out", "w", stdout );
	int 	rr;
	cin >> rr;
	int 	nrr = 0;
	while ( rr -- )
	{
		nrr ++;
		set < string > 	a;
		int 	n;
		cin >> n;
		string 	tmp;
		getline ( cin, tmp );
		for ( int i = 0; i < n; i ++ )
		{
			string 	tmp;
			getline ( cin, tmp ); 
			a . insert ( tmp );
		}
		set < string > b;
		cin >> n;
		b = a;
		getline ( cin, tmp );
		int 	ans = 0;
		while ( n -- )
		{
			string 	tmp;
			getline ( cin, tmp );
			//cerr << tmp << endl;
			if ( a . find ( tmp ) != a . end () )
				a . erase ( a . find ( tmp ) );
			//cerr << a . size () << endl;
			if ( a . empty () )
			{ 
				a = b;
				ans ++;
				if ( a . find ( tmp ) != a . end () )
					a . erase ( a . find ( tmp ) );
			}
		}
		cout << "Case #" << nrr << ": " << ans << endl;
	}
//	cout << my_answer;
//	for ( int i = 0; i < ( int ) my_answer . size (); i++ )	cout << my_answer[i] << endl;
}
