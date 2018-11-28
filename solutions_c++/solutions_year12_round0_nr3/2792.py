#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cfloat>
#include <climits>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>

#define INF 1000000007
#define EPS (1e-8)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
typedef long long LL;

using namespace std;

inline int getDigits( int num )
{
  return ceil( log10(num + 1) );
}

inline int countValidPairs( int num , int left , int right )
{
  int num_digits = getDigits( num );
  int valid_pairs = 0;
  int t = 10;
  int recyclednum;
  int tp;
  int multiple = pow( 10 ,  num_digits  );

  int num1, num2;
  
  set<int> all_recycles;
  while( t < multiple )
    {
      tp = multiple/t;
      num1 = num/t;
      num2 = (num % t);
      
      recyclednum = num1 + ( num2 ) * tp;

      if( ( num < recyclednum ) && 
	  ( recyclednum >= left ) && 
	  ( recyclednum <= right ) && 
	  ( getDigits( recyclednum ) == num_digits ) )
  	{
	  if( all_recycles.count( recyclednum) == 0 )
	    {
	      valid_pairs++;
	    }
	  all_recycles.insert(recyclednum);
	}
      
      t = t*10;
    }
  
  return valid_pairs;
}


main()
{
  int tests;
  scanf("%d",&tests);
  
  int left,right;
  int num_recycled_pairs;
  for( int tc = 1 ; tc <= tests ; tc++ )
    {
      num_recycled_pairs = 0;
      scanf("%d%d", &left , &right );

      for( int t = left ; t <= right ; t++ )
	{
	  num_recycled_pairs = num_recycled_pairs + countValidPairs( t , left , right );
	}
      printf("Case #%d: %d\n",tc,num_recycled_pairs);
    }
}



