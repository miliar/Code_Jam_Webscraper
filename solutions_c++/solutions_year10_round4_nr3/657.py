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

int a[120][120];

bool prazna()
     {
     FOR ( i, 0, 120 ) 
         FOR( j, 0 , 120 ) 
            if ( a[i][j] == 1 ) return false;
     return true;        
     }

void transform()
     {
     for( int i = 119; i >= 0; -- i ) 
          for( int j = 119 ;j>= 0; --j ) 
               {
               if ( a[i-1][j] == 1 && a[i][j-1] == 1 ) 
                  a[i][j] = 1;    
               else if ( a[i-1][j] == 0 && a[i][j-1] == 0 ) 
                    a[i][j] = 0;
               }
     return;
     }

int main()
    {
    cin >> test_cases;
    for( int test_nmbr = 0; test_nmbr < test_cases; ++test_nmbr ) 
         {
         memset(a,0,sizeof(a));
         int R; cin >> R;
         
         FOR(i,0,R)
            {
            int p,q,r,s;
            cin >> p >> q >> r >> s;
            FOR( i, p, r + 1 ) 
              FOR ( j, q, s + 1 ) 
                  a[i][j] = 1;       
            }
         int sol = 0;
         while(!prazna() ) 
           {
           ++sol;
           transform();          
           }
         
         cout << "Case #" << test_nmbr + 1 << ": " << sol << endl;
         }
          
    return 0;
    }
