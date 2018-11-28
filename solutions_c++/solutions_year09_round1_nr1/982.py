#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <sstream>
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

map< int, vi > memo;

bool is_happy( int num, int base )
{
   if( num == 1 ) return true;

   vi vec = memo[base];

   FORI( i, 0, vec.size() )
   {
      if( vec[i] == num ) return false;
   }

   memo[base].push_back( num );

   int newnum = 0, tempnum = num;

   while( tempnum )
   {
      int temp = tempnum % base;

      newnum += temp*temp;

      tempnum /= base;
   }

   return is_happy( newnum, base );
}

int main()
{
   bool done = false;
   char tmpline[256];
   int nCases, cnt, tmpbase;
   vi bases;

   cin >> nCases;
   cin.ignore();


   FORLE( i, 1, nCases )
   {
      cnt = 0;
      bases.clear();
      done = false;
      memo.clear();

      cin.getline( tmpline, 256 );
      string line( tmpline ), token;
      istringstream iss( line );

      while( getline( iss, token, ' ' ) )
      {
         bases.push_back( atoi( token.c_str() ) );
         vi v;
         memo[ atoi( token.c_str() ) ] = v;
      }

      for( cnt = 2; !done; ++cnt )
      {
         done = true;
         FORI( k, 0, bases.size() )
         {
            memo[bases[k]].clear();
            done &= is_happy( cnt, bases[k] );
            if( !done ) break;
         }
      }

      --cnt;

      cout << "Case #" << i << ": " << cnt;
      cout << endl;
   }

   return 0;
}  
