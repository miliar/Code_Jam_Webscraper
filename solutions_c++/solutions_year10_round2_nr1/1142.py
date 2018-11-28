#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <set>
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

int main()
{
   int nCases, cnt, numDirs, numNewDirs, dirIndex;
   string dir, tmp;
   set<string> dirs;

   cin >> nCases;

   FORLE( i, 1, nCases )
   {
	   dirs.clear();

	   cin >> numDirs;
	   cin >> numNewDirs;


	   FORI( j, 0, numDirs )
	   {
		   cin >> dir;
		   dirs.insert( dir );
	   }

	   cnt = dirs.size();

	   FORI( j, 0, numNewDirs )
	   {
		   cin >> dir;
		   dirIndex = 0;

		   do
		   {
			   dirIndex = dir.find( '/', dirIndex+1 );

			   if( dirIndex == string::npos )
				   tmp = dir;
			   else
				   tmp = dir.substr( 0, dirIndex );
			   
			  /* for( set<string>::iterator itr = dirs.begin();
					itr != dirs.end(); ++itr )
			   {
				   cout << "\n" << *itr;
			   }
			   */
			   if( dirs.find( tmp ) == dirs.end() )
			   {
				   dirs.insert( tmp );
			   }
		   }
		   while( dirIndex != string::npos );
	   }

	   cnt = dirs.size() - cnt;

      cout << "Case #" << i << ": " << cnt;
      cout << endl;
   }

   return 0;
}  
