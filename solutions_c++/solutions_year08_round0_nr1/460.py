#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>
using namespace std ;

const int MAXQ = 1200 ;
const int MAXL = 120 ;

int T ;

int S ;
int Q ;

map<string,int> names ;
int queries[MAXQ] ;
int dyna[MAXQ][MAXL] ;

int UNDEFINED = -1 ;

int min(int a, int b){ return (a<b)?a:b ; }

int smallestSwitch(int q, int c )
{
  if( q == Q )
    return 0 ;

  if( c == queries[q] )
    return MAXQ ;

  int & dyn = dyna[q][c] ; 
  if( dyn != UNDEFINED )
    return dyn ;

  int r = MAXQ ;
  for( int nextc = 0 ; nextc < S ; nextc ++ )
    r = min( r, smallestSwitch( q+1, nextc ) + (nextc != c) ) ;
  
  dyn = r ;

  return r ;
}

int main()
{
  scanf("%d", &T );

  for( int t = 0 ; t < T ; t ++ )
    {
      //cout << "--------" << t <<"------" << endl ;

      scanf("%d\n",&S);
      names.clear() ;
      
      //cout << S << "--------" << endl ;

      for( int s = 0 ; s < S ; s ++ )
        {
          char name[MAXL] ;
          cin.getline(name, MAXL);
          names[name] = s ;          
          //cout << strlen(name) << endl ;
        }
      
      scanf("%d\n",&Q);
      
      for( int q = 0 ; q < Q ; q ++ )
        {
          char query[MAXL] ;
          cin.getline(query, MAXL);
          queries[q] = names[query] ;
          //cout << queries[q] << endl ;
        }

      for( int q = 0 ; q < Q ; q ++ )
        for( int c = 0 ; c < S ; c ++ )
          dyna[q][c] = UNDEFINED ;


      int r = MAXQ ;
      
      for( int c = 0 ; c < S ; c ++ )
        {
        r = min( r, smallestSwitch(0,c) );
        //cout <<  smallestSwitch(0,c)   << " " << c << endl ;
        }
      cout << "Case #" << (t+1) << ": " << r << endl ;
    }
}
