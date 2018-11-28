#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long ll ;

int NBTEST ;


int main()
{
  cin >> NBTEST ;
  for( int TEST = 1 ; TEST <= NBTEST ; TEST ++ )
    {
      ll result = 0 ;
      ll P,K,L ;

      cin >> P >> K >> L ;

      ll freq[L] ;
      for( int l = 0 ; l < L ; l ++ )
        {
          cin >> freq[l] ;
        }
      sort( &freq[0] , &freq[L] ) ;
      
      for( int l = 0 ; l < L ; l ++ )
        {
          //cout << freq[L-l-1] << endl ;
          //cout << (l / K) + 1 << endl ;
          result += freq[L-l-1] * ( (l / K) + 1 ) ;
        }

      cout << "Case #" << TEST << ": " << result << endl ;
    }
} 
