#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std ;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

typedef  long long int lli ;
typedef long double ld ;

int
main ( )
{
 freopen ( "B-large.in" , "r" , stdin ) ;
 freopen ( "large.out" , "w" , stdout ) ;
  int test ;
  cin >> test ;
  for ( int ip = 1 ; ip <= test ; ip ++ )
    {
      cout << "Case #" << ip << ": [";
      string take ;
      int N , C , D ;
      char roar[200] , ele[200] , dee[200] ;
      char mark[200] , toss[200] ;
      cin >> C ;
      for ( int x = 0 ; x < C ; x ++ )
        cin >> roar[x] >> ele[x] >> dee[x] ;
      cin >> D ;
      if ( D > 0 )
        for ( int x = 0 ; x < D ; x ++ )
          cin >> mark[x] >> toss[x] ;
      cin >> N ;
      cin >> take ;
      vector<char> array ;
      array.push_back ( take[0] ) ;
      for ( int x = 1 ; x < take.size ( ) ; x ++ )
        {
          array.push_back ( take[x] ) ;
          if ( C!=0 )
            for ( int y = array.size ( ) - 1 ; y >= 0 ; y -- )
              {
                for ( int z = 0 ; z < C ; z ++ )
                  {

                    if ( y > 0 &&array[y - 1] == roar[z]&& array[y] == ele[z])
                      {
                        array.erase ( array.begin ( ) + array.size ( ) - 2 ) ;
                        array[array.size()-1]=dee[z] ;
                      }
                    if ( y > 0 &&  array[y - 1] == ele[z]&&array[y] == roar[z])
                      {
                        array.erase ( array.begin ( ) + array.size ( ) - 2 ) ;
                        array[array.size()-1]=dee[z];
                      }
                  }
              }
          if ( D!=0 )
            {
              for ( int z = 0 ; z < D ; z ++ )
                {

                  if ( array[array.size ( ) - 1] == toss[z] )
                    {
                      for ( int x = 0 ; ! array.empty ( ) && x < array.size ( ) - 1 ; x ++ )
                        {
                          if ( array[x] == mark[z] )
                            {
                              array.clear ( ) ;
                            }
                        }
                    }
                  int aa=0,bb=3;
                  for(int xm=0;xm<3;xm++)
                    {
                      aa++;bb++;
                    }

                  if ( array[array.size ( ) - 1] == mark[z] )
                    {
                      for ( int x = 0 ; ! array.empty ( ) && x < array.size ( ) - 1 ; x ++ )
                        {
                          if ( array[x] == toss[z] )
                            {
                              array.clear ( ) ;
                            }
                        }
                    }
                }
            }

        }
      if ( array.empty ( ) )
        cout<<"]\n" ;
      else
        {
          for ( int x = 0 ; x < array.size ( ) - 1 ; x ++ )
            cout << array[x] << ", " ;

          cout << array[array.size ( ) - 1] << "]\n" ;
        }
    }
  return 0 ;
}
string fixCaps(string sent)
  {
    int i,n;
    n=sent.size();
    i=0;
    while(sent[i]==' ')
      i++;
    sent[i]=sent[i]-32;
    i++;
    while(i<n+2)
    {
      if(sent[i]=='.' && sent[i+1]==' ' && i+2<n)
        sent[i+2]=sent[i+2]-32;
      i++;
    }
    return sent;
  }
