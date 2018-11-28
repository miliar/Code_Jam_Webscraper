#include <iostream>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std ;

#define fv(i, s, n) for ( int i = s ; i < n ; i++ )
#define fb(i, n) fv (i, 0, n)
#define fe(i, n) fb (i, n.size())
#define pb push_back
#define all(n) n.begin(), n.end()
#define fi(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)

int main()
{
	ifstream in ("Welcome.in") ;
	ofstream out ("Welcome.out") ;
	
	string str = "welcome to code jam" ;
	
	int n ;
	in >> n ;
	
	string g ;
	getline (in, g) ;
	
	fb (i, n)
	{
		vector <int> k(str.size(), 0) ;
		string s ;
		
		getline(in, s) ;
		
		fe (u, s) for ( int j = k.size() - 1 ; j >= 0 ; j-- ) if ( str[j] == s[u] )
		{
			if ( j == 0 ) k[j]++ ;
			else k[j] += k[j - 1] ;
			
			k[j] %= 10000 ;
		}
		
		char r[100] ;
		sprintf (r, "Case #%d: %04d\n", i + 1, k[ k.size() - 1 ]) ;
		out << r ;
	}
	
	return 0 ;
}

