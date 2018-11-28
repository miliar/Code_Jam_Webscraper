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







int main ()
{
	freopen ( "1.in", "r", stdin );
	freopen ( "1.out", "w", stdout );
	int 	rr = 0;
	cin >> rr;
	while ( rr -- )
	{
		int 	n;
		cin >> n;
		cerr << rr <<endl;
		string	s;
		cin >> s;
		vector < int > 	a;
		int 	jc = 1;
		for ( int i = 0; i < n; i ++ )
		{
			a . push_back ( i );
			jc *= i + 1;
		}
		int 	ans = s . size ();
		while ( jc -- )
		{
			next_permutation ( a . begin (), a .end () );
			//for ( int i = 0; i < ( int ) a . size (); i ++ )
				//cerr << a[i] << " ";
			//cerr << endl;
			string 	tmp;
			for ( int j = 0; j < ( int ) s . size (); j += n )
			for ( int i = 0; i < n; i ++ )
			{
				tmp += s[j + a[i] ];
			}
			int 	t = 0;
			for ( int i = 0; i < ( int ) tmp . size (); i ++ )
			{
				if ( i == 0 || tmp[i] != tmp[i - 1]  )
					t ++;
			}
			//cerr << tmp << endl;
			//cerr << t << endl;
			ans = min ( ans, t );
		}
		cout << nc () << ans << endl;






















	}
//	cout << nc ( 100 ) << endl;
//	cout << nc () << endl;
}
