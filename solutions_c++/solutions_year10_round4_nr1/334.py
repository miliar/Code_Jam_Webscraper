#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <cmath>
#include <vector>

using namespace std;

#define VI vector<int>
#define VS vector<string>
#define pb push_back
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it=(kont).begin();it!=(kont).end();++it)
#define VVI vector< vector<int> >

int test_cases;

int size;
VVI dijamant;
         
int main()
    {
    cin >> test_cases;
    for( int test_nmbr = 0; test_nmbr < test_cases; ++test_nmbr ) 
         {
         cin >> size;
         int nsize = size;
         dijamant.clear();
         dijamant.resize( size ) ;
         FOR( i , 0, size )
            for( int j = 0; j <= i; ++j ) 
                 {
                 int x;
                 cin >> x;
                 dijamant[j].pb( x ) ;    
                 }
         FOR( i, 1, size ) 
              for( int j = i; j < size; ++j ) 
                   {
                   int x; cin >> x;
                   dijamant[j].pb( x ) ;    
                   }
         /*
         FOR( i , 0, size )  { 
              FOR( j, 0, size) 
               cout << dijamant[i][j] << " ";
               cout << endl;}
         */
         int oo = (1<<30) +32432;
       //  cout << "tu" << endl;
         for( nsize = size; ; ++nsize)
              {
            //  cout << nsize << endl;
              VVI ndijamant;
              ndijamant.resize( nsize);
              
              FOR( i, 0 , nsize ) ndijamant[i].resize( nsize, oo);
              
              bool nasao = false;
              for( int i = 0; i + size <= nsize; ++i ) 
                   for( int j = 0; j+ size <= nsize; ++j)
                        {
                        bool uspio = true;
                        VVI nndijamant = ndijamant;
                        FOR( k, 0 , size ) 
                             FOR ( l, 0, size ) 
                                 nndijamant[i + k][j + l] = dijamant[k][l];
                        /*
                         FOR( i , 0, size )  { 
                              FOR( j, 0, size)   
                             cout << nndijamant[i][j] << " ";
                             cout << endl;}
                         system("pause" ) ;
                        */
                        FOR( k,0,nsize )
                             FOR( l, 0 , nsize ) 
                                  if ( nndijamant[k][l] != oo ) 
                                     {
                                     if ( nndijamant[l][k] != nndijamant[k][l] && nndijamant[l][k] != oo ) 
                                        uspio = false;
                                     else nndijamant[l][k] = nndijamant[k][l];
                                     int x = ( nsize - 1 - k - l );
                                     if ( nndijamant[k+x][l+x] != nndijamant[k][l] && nndijamant[k+x][l+x] != oo ) 
                                        uspio = false;
                                     else nndijamant[k+x][l+x] = nndijamant[k][l];
                                     }
                        if ( uspio ) nasao = true;
                        }
              if ( nasao ) break;      
              }
         cout << "Case #" << test_nmbr + 1 << ": " << nsize*nsize - size*size << endl;
         }
          
    return 0;
    }
