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

struct kokos
   {
   int x;
   int v;  
   };

vector<kokos> kokosi;

int main()
    {
    cin >> test_cases;
    for( int test_nmbr = 0; test_nmbr < test_cases; ++test_nmbr ) 
         {
         kokosi.clear();
         int N, K , B, T;
         cin >> N >> K >> B >> T;
         kokosi.resize( N );
         FOR( i, 0, N ) 
            cin >> kokosi[i].x;
         FOR( i, 0, N ) 
            cin >> kokosi[i].v;
         FOR( i, 0 , N ) 
              FOR( j, i + 1, N ) 
                   if ( kokosi[i].x > kokosi[j].x ) 
                        swap ( kokosi[i], kokosi[j] );
         
         //FOR( i, 0, N ) 
         //   cerr << kokosi[i].x << " " << kokosi[i].v << endl;
         
         int cnt = 0;
         int pos = N - 1;
         int sol = 0;
         
         while ( cnt < K )
               {
               if ( pos < 0 ) { sol = -1; break; }       
               
               long long mp = kokosi[pos].x;
               mp += (long long)( T ) * (long long)( kokosi[pos].v);
               
               if ( mp < B ) { sol += K - cnt; } 
               else { ++cnt; } 
               --pos;
               }
         
         if ( sol == -1 ) { cout << "Case #" << test_nmbr + 1 << ": " << "IMPOSSIBLE" << endl;  }
         else { cout << "Case #" << test_nmbr + 1 << ": " << sol << endl; } 
         }
    //system("pause");
    return 0;
    }
