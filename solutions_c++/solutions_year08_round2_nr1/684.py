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

#define com(a, b, c, d) ( ( a + b ) % 3 == 0 && ( c + d ) % 3 == 0 )

int cas ( vector <pair <int, int> > cor )
{
	vector <int> co(9, 0) ;
	int r = 0 ;
	
	fe (i, cor) co[ 3 * cor[i].first + cor[i].second ]++ ;
	
	//fb (a, 9) fb (b, 9) fb (c, 9)
	
	/*fe (i, co) cout << co[i] << ' ' ;
	cout << endl ;*/
	
	fb (a, 9) for ( int b = a ; b < 9 ; b++ ) for ( int c = b ; c < 9 ; c++ )
	{
		if ( (a / 3 + b / 3 + c / 3) % 3 == 0 && (a % 3 + b % 3 + c % 3) % 3 == 0)
		{
			int u = 0 ;
			
			//if (a == 5 && b == 5 && c == 5 ) u = a * (a - 1) * (a - 2) / 6 ;
			
			if ( a == b && a == c && b == c ) u = co[a] * (co[a] - 1) * (co[a] - 2) / 6 ;
			
			else if ( a == b ) u = ( co[a] * (co[a] - 1) / 2 ) * co[c] ;
			else if ( a == c ) u = ( co[a] * (co[a] - 1) / 2 ) * co[b] ;
			else if ( b == c ) u = co[a] * ( co[b] * (co[b] - 1) / 2 ) ;
			
			else u = co[a] * co[b] * co[c] ;
			
			r += u ;
			
			//if (u) cout << a << ' ' << b << ' ' << c << endl ;*/
		}
	}
	
	return r ;
}


int main()
{
	ifstream in ("Crop.in") ;
	ofstream out ("Crop.out") ;
	
	int N ;
	in >> N ;
	
	fb (i, N)
	{
		long long n, A, B, C, D ;
		int x, y, m ;
		in >> n >> A >> B >> C >> D >> x >> y >> m ;
		
		vector <pair <int, int> > cor(n) ;

		fb (u, n)
		{
			cor[u] = make_pair (x % 3, y % 3) ;
			x = ((A * x + B) % m) ;
			y = ((C * y + D) % m) ;
		}
		
		out << "Case #" << i + 1 << ": " << cas (cor) << endl ;
	}
	
	return 0 ;
}

