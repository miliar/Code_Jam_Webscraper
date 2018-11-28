#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int N ,S, Q;
vector < string > queries ;
vector < string > engine ;
map < string , int > cache ;
int DP [ 1010][101];
int inf = 1<<24;
main () 
{
     cin >> N;
     int Case = 1;
     while ( N-- )
     {
           int i ,j ,k;
           engine.clear();cache.clear();queries.clear();
           cin >> S;
           string tmp;
           char in [ 100 ];
           gets ( in );
           for ( i = 0; i < S ;i++ )
           {
               gets ( in );
               tmp  = in ;
               engine.push_back ( tmp );
           }
           cin >> Q;
           gets ( in );
           for ( i = 0; i < Q ;i++)
           {
               gets ( in );
               tmp = in ;
               queries.push_back ( tmp );
               cache [ tmp ]++; 
           }
          // cin >> i;
           for ( i = 0; i < Q ;i++)      
           for ( j = 0; j < S ;j++ )DP[i][j] = 1<<24;//cin >>i ;
           if ( Q > 0 )
           for ( j = 0 ;j < S ;j++ ) if ( queries [0] != engine [j] ) DP [0][j]=  0;
              // cin>>i;
               for ( i =1 ; i < Q ;i++)
               {
                   for ( j = 0 ;j <S ;j++)
                   {
                       if ( queries [i] != engine [j] )
                       {
                            if ( DP [i-1][j] != inf )
                            DP [i][j] = DP [i-1][j];
                            else
                            for ( k = 0 ; k < S ;k++ )
                            DP [i][j] = min ( DP[i][j] ,DP[i-1][k]+1 );
                       }
                      // cout << DP [i][j] <<" ";
                   }
                   //cout <<"\n";
               }
               //cout << "yes" <<"\n";cin >>i;
               int ans = 2000 ;
               if ( Q ==0 ) ans = 0 ;
               else for ( i = 0; i < S ;i++ ) ans = min ( ans ,DP [Q-1][i] );
               cout << "Case #"<<Case++ <<": ";
           cout << ans <<"\n";
               
     }
} 
          
           
