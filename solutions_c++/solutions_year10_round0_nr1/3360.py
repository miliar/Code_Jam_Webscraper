#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

#define MAPITR(a,b)	map<a,b>::iterator
#define LISTITR(a)	list<a>::iterator

#define ITER(itr,a)	for( itr = (a).begin(); itr != (a).end(); ++itr )
#define ITERNI(itr,a)	for( itr = (a).begin(); itr != (a).end();  )
#define FORI(i,a,b)	for( int i(a), _b(b); i < _b; ++i )
#define FORD(i,a,b)	for( int i(a), _b(b); i > _b; --i )
#define FORLE(i,a,b)	for( int i(a), _b(b); i <= _b; ++i )
#define FORGE(i,a,b)	for( int i(a), _b(b); i >= _b; --i )

typedef list<char> lc;
typedef list<int> li;
typedef list<double> ld;
typedef list<string> ls;

typedef vector<char> vc;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;

vector< pair<bool, bool> > snappers;

void power( int index, bool val, int max )
{
	if( index == max )
		return;
	
	snappers[index].first = val;

	power( index + 1, val && snappers[index].second, max );
}

int main()
{
   int nCases;
   int nSnappers, nSnaps;

   cin >> nCases;

   FORLE( i, 1, nCases )
   {
	   snappers.clear();

		cout << "Case #" << i << ": ";
		
		cin >> nSnappers;
		cin >> nSnaps;

		FORI( j, 0, nSnappers )
		{
			snappers.push_back( pair<bool,bool>(0,0) );
		}

		snappers[0].first = 1;

		FORI( j, 0, nSnaps )
		{
			FORGE( k, nSnappers-1, 0 )
			{
				if( snappers[k].first )
					snappers[k].second ^= true;
			}

			power( 0, 1, nSnappers );
		}

		cout << (snappers[nSnappers-1].first &&
				 snappers[nSnappers-1].second ? "ON" : "OFF") << endl;
   }

   return 0;
}  
