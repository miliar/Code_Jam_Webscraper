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

#define max 2000

struct tre
{
	int p ;
	int w ; // 0->en A, 1->en B, 2->llendose a A, 3->llendose a B
} ;

pair <int, int> rep (vector <pair <int, int> > ab, vector <pair <int, int> > ba, int T)
{
	vector <tre> tr ;
	
	int ra = 0, rb = 0 ;
	
	fe (i, ab) ab[i].second += T ;
	fe (i, ba) ba[i].second += T ;
	
	fb (tim, max)
	{
		fe (i, tr) if (tr[i].p == tim)
		{
			if (tr[i].w == 2) tr[i].w = 0 ;
			if (tr[i].w == 3) tr[i].w = 1 ;
			tr[i].p = -1 ;
		}
	
		fe (i, ab) if (ab[i].first == tim)
		{
			bool y = false ;
		
			fe (u, tr) if (tr[u].w == 0)
			{
				tr[u].w = 3 ;
				tr[u].p = ab[i].second ;
				y = true ;
				break ;
			}
			
			if (!y)
			{
				tr.pb ((tre){ab[i].second, 3}) ;
				ra++ ;
			}
		}
		fe (i, ba) if (ba[i].first == tim)
		{
			bool y = false ;
		
			fe (u, tr) if (tr[u].w == 1)
			{
				tr[u].w = 2 ;
				tr[u].p = ba[i].second ;
				y = true ;
				break ;
			}
			
			if (!y)
			{
				tr.pb ((tre){ba[i].second, 2}) ;
				rb++ ;
			}
		}
	}
	
	return make_pair (ra, rb) ;
}
	
int main()
{
	ifstream in ("Timetablenm.in") ;
	ofstream out ("Timetablenm.out") ;
		
	int N ;
	in >> N ;
	
	fb (i, N)
	{	
		int T ;
		int na, nb ;
		vector < pair <int, int> > ab ;
		vector < pair <int, int> > ba ;
		
		in >> T >> na >> nb ;
		
		fb (i, na)
		{
			int a, b, c, d ;
			char j ;
			
			in >> a >> j >> b >> c >> j >> d ;
			ab.pb (make_pair (a * 60 + b, c * 60 + d)) ;
		}
		
		fb (i, nb)
		{
			int a, b, c, d ;
			char j ;
			
			in >> a >> j >> b >> c >> j >> d ;
			ba.pb (make_pair (a * 60 + b, c * 60 + d)) ;
		}
		
		pair <int, int> r = rep(ab, ba, T) ;
		
		out << "Case #" << i + 1 << ": " << r.first << ' ' << r.second << endl ;
	}
	
	return 0 ;
}

