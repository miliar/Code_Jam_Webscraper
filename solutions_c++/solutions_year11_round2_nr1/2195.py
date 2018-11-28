// CodeJam 2011 : Round 1B : RPI
// Author: Rodrigo González del Cueto

#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  

int main ()
{
  cout.precision(10);
 
  int cases;
  float wp, owp, oowp;

  float ggames [ 100 ];
  float gwp [ 100 ];
  float gowp [ 100 ];
  float goowp [ 100 ];
  
  char t [ 100 * 100 ];

  // Read Cases
  cin >> cases;

  for ( int i = 1; i <= cases; i++ )
    {
      int n;
      cin >> n;

      for ( int j = 0; j < n; j++ )
	{
	  for ( int k = 0; k < n; k++ )
	    {
	      cin >> t [ j * n + k ];
	    }
	}

      for ( int j = 0; j < n; j++ )
	{
	  int games = 0;
	  int won = 0;
	  int lost = 0;
	  for ( int k = 0; k < n; k++ )
	    {
	      if ( t [ j * n + k ] == '0' )
		lost++;
	      if ( t [ j * n + k ] == '1' )
		won++;
	      if ( t [ j * n + k ] != '.' )
		games++;
	    }

	  ggames [ j ] = games;
	  gwp [ j ] = won;
	}

      for ( int j = 0; j < n; j++ )
	{
	  owp = 0;
	  int opponents = 0;
	  for ( int k = 0; k < n; k++ )
	    {
	      if ( t [ j * n + k ] != '.' )
		{
		  opponents++;
		  if ( t [ j * n + k ] == '0' )
		    owp += ( gwp [ k ] - 1 ) / ( ggames [ k ] - 1 );
		  else
		    owp += gwp [ k ] / ( ggames [ k ] - 1 );
		}
	    }
	  gowp [ j ] = owp / opponents;
	}

      for ( int j = 0; j < n; j++ )
	{
	  oowp = 0;
	  for ( int k = 0; k < n; k++ )
	    {
	      if ( t [ j * n + k ] != '.' )
		oowp += gowp [ k ];
	    }
	  goowp [ j ] = oowp / ggames [ j ];
	}

      cout << "Case #" << i << ": " << endl;
      
      for ( int j = 0; j < n; j++ )
	{
	  cout << ( 0.25 * ( gwp [ j ] / ggames [ j ] ) + 0.5 * gowp [ j ] + 0.25 * goowp [ j ] ) << endl;
	}

    }
  return 0;
}
