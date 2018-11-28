#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <queue>
#include <set>
using namespace std;

typedef long long ll ;

int N ;

const int MAXP = 1000010 ;
bool prime[MAXP] ;
int parent[MAXP] ;

int getParent( int p )
{
  if( parent[p] == p )
    return p ;
  else
    {
      int pp = getParent( parent[p] ) ;
      parent[p] == pp ;
      
      return pp ;
    }
}

int main()
{
  cin >> N ;
  for( int p = 0 ; p < MAXP ; p ++ )
    prime[p] = true ;
  prime[0] = false ;
  prime[1] = false ;

  for( int p = 2 ; p < MAXP ; p ++ )
    if( prime[p] )
      for( int q = 2 ; q * p < MAXP ; q ++ )
        prime[p*q] = false ;
  
  for( int n = 0 ; n < N ; n ++ )
    {
      for( int p = 0 ; p < MAXP ; p ++ )
        parent[p] = p ;
      
      ll A, B, P ;
      cin >> A >> B >> P ;
      
      for( int p = 2 ; p < MAXP ; p ++ )
        if( prime[p] && p >= P )
          {
            int firstel  ;
            if( A % p == 0 )
              firstel = 0 ;
            else
              firstel = p - (A % p)  ;

            for( int el = firstel ; el <= B - A ; el += p )
              {
                parent[ getParent( el ) ] = getParent( firstel ) ;
              }
          }
      
      set<int> s ;
      for( int el = 0 ; el <= B-A ; el ++ )
        {
          s.insert( getParent(el) ) ;
          //cout << el + A << " "<< getParent(el ) << endl ;
        }
      cout << "Case #" << (n+1 ) << ": " << s.size() << endl ;
    }
}
