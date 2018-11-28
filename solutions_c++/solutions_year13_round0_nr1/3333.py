#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <string>
#include <cstring>
#include <queue>
using namespace std;

#define FOR0(i,n) for( i = 0 ; i < n ; ++i )
#define FOR1(i,n) for( i = 1 ; i <= n ; ++i )
#define sor(x) sort(x.begin(),x.end())
#define rsor(x) sort(x.rbegin(),x.rend())
#define sys_p system( "pause" )
#define End return 0
#define pb push_back 
#define mp make_pair

typedef long long LL ;

ifstream Cin("input.txt");
ofstream Cout( "output.txt" );

char r[4][4], stuff ;

bool eq( char give, char c1, char c2 )
{
      return give == c1 || give == c2 ;
}

bool eqq( LL i1, LL j1, LL i2, LL j2, char c )
{
      return eq( r[i1][j1], c, 'T' ) && eq( r[i2][j2], c, 'T' ) ;
}

bool check( char c )
{
      LL i, j ; 
      
      FOR0( i, 4 )
      {
        FOR0( j, 3 ) 
          if( !eqq( i, j, i, j+1, c ) )
            break ;
        if( j == 3 )
          return true ;
      }
      
      FOR0( j, 4 )
      {
        FOR0( i, 3 ) 
          if( !eqq( i, j, i+1, j, c ) )
            break ;
        if( i == 3 )
          return true ;
      }
      
      FOR0( i, 3 )
        if( !eqq( i, i, i+1, i+1, c ) )
          break ;
      if( i == 3 )
        return true ;
        
      FOR0( i, 3 )
        if( !eqq( i, 3-i, i+1, 2-i, c ) )
          break ;
      if( i == 3 )
        return true ;
      
      return false ;
}

bool full()
{
      LL i, j ; 
      FOR0( i, 4 ) FOR0( j, 4 ) if( r[i][j] == '.' ) return false ;
      return true ;
}

main()
{ 
      LL T, t ;
      Cin >> T ;
      FOR1( t, T )
      {
        LL i, j ;
        FOR0( i, 4 ) FOR0( j, 4 ) Cin >> r[i][j] ;
        //FOR0( i, 4 ){ FOR0( j, 4 ) cout << r[i][j] ; cout << endl ; }
        Cout << "Case #" << t << ": " ;
        if( check('X') ) Cout << "X won" ;
        else if( check('O') ) Cout << "O won" ;
        else if( full() ) Cout << "Draw" ;
        else Cout << "Game has not completed" ;
        Cout << endl ;
      }
} 

