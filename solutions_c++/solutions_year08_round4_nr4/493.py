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
  for( int TEST = 0 ; TEST < NBTEST ; TEST ++ )
    {
      int result = 1000000 ;
      int K ;
      string s ;
      cin >> K ;
      cin >> s ;
      int pk = 1 ;
      for( int k = 0 ; k < K ; k ++ )
        pk *= K ;
      
      for( int perm = 0 ; perm < pk ; perm ++ )
        {
          int permu[K] ;
          set<int> unique ;
          int vperm = perm ;
          for( int k = 0 ; k < K ; k ++ )
            {
            permu[k] = vperm % K ;
            vperm /= K ;
            unique.insert( permu[k] );
            }

          if( unique.size() == K )
            {
              //for( int k = 0 ; k <K ; k ++ )
              //  cout << permu[k] << " " ;
              //cout << endl ;
              // }

              int l = s.size() ;
              char previous = 0 ;
              int compressed = 0 ;
              
              for( int pl = 0 ; pl < l/K ; pl ++ )
                {
                  for( int k = 0 ; k < K ; k ++ )
                    {
                      char now = s[ permu[k] + pl*K ] ;
                      if( previous != now )
                        {
                          compressed ++ ;
                          previous = now ;
                        }
                    }
                }
              
              result = min( result , compressed );
            }
        }

      cout << "Case #" << (TEST+1) << ": " << result << endl ;
    }
}
