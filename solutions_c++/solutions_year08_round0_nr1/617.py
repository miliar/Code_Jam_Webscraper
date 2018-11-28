#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std ;

#define fb(i, n) for (int i = 0 ; i < n ; i++)
#define fe(i, n) fb (i, n.size())
#define pb push_back
#define all(n) n.begin(), n.end()
#define fi(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)

int rep (vector <int> f, int t)
{
	vector <bool> sd (t, false) ;
	int r = 0 ;
	
	cout << f.size() << ' ' << t << endl ;
	
	//if (f.size() == 0) return 0 ;
	
	fe (i, f)
	{
		sd[ f[i] ] = true ;
		if ( *min_element(all(sd)) == 1 )
		{
			r++ ;
			sd = vector <bool> (t, false) ;
			sd[ f[i] ] = true ;
		}
	}
	
	return r ;
}

int main()
{
	ifstream in ("Universe.in") ;
	ofstream out ("Universe.out") ;
	
	int N ;
	in >> N ;
	
	fb (i, N)
	{
		vector <int> r ;
		map <string, int> p ;
		int q, s ;
		string n ;
		
		in >> q ;
		
		getline (in, n) ;
		fb (u, q)
		{
			string j ;
			getline (in, j) ;
			p[j] = u ;
		}
		
		in >> s ;
		getline (in, n) ;
		fb (u, s)
		{
			string k ;
			getline(in, k) ;
			r.pb ( p[k] ) ;
			
			//cout << k << ' ' << p[k] << endl ;
		}
		
		out << "Case #" << i + 1 << ": " << rep(r, q) << endl ;
	}
			
	return 0 ;
}
