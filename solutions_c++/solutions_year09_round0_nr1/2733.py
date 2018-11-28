#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string>
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

bool check( string s, vs &dict )
{
   int i;
   for( i = 0; i < dict.size(); ++i )
   {
      if( dict[i].find( s ) == 0 )
         return true;
   }
   
   return false;
}

int main()
{
   bool open = false;
   int nCases, l, d;
   string str;
   char c;

   cin >> l; cin >> d; cin >> nCases;

   vs dict, words;
   vc mult;

   FORI( i, 0, d )
   {
      cin >> str;
      dict.push_back( str );
   }

   FORLE( i, 1, nCases )
   {
      int j = 0, cnt = 0;
      mult.clear();
      words.clear();

      while( j < l )
      {
         cin >> c;

         if( c == '(' )
            open = true;
         else if( c == ')' )
         {
            open = false;
            vs temp( words );

            words.clear();

            FORI( k, 0, mult.size() )
            {
               if( j == 0 )
               {
                  string tstr;
                  tstr.insert( 0, 1, mult[k] );

                  words.push_back( tstr );
               }
               else
               {
                  FORI( x, 0, temp.size() )
                  {
                     string tmpstr( temp[x] );
                     tmpstr.insert( j, 1, mult[k] );

                     if( check( tmpstr, dict ) )
                        words.push_back( tmpstr );
                  }
               }
            }

            ++j;
            mult.clear();
         }
         else
         {
            if( open )
               mult.push_back( c );
            else
            {
               if( j == 0 )
               {
                  string tstr;
                  tstr.insert( 0, 1, c );
                  words.push_back( tstr );
               }
               else
               {
                  FORI( k, 0, words.size() )
                     words[k].insert( j, 1, c );
               }

               ++j;
            }
         }
      }

      FORI( j, 0, words.size() )
      {
//         cout << words[j] << " ";

         FORI( k, 0, dict.size() )
         {
            if( words[j].compare( dict[k] ) == 0 )
            {
               ++cnt;
               break;
            }
         }
      }
//      cout << endl;

      cout << "Case #" << i << ": " << cnt;
      cout << endl;
   }

   return 0;
}  
