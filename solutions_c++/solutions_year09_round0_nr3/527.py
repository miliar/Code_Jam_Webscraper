#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <set>
#include <map>

#define VI vector<int>
#define VS vector<string>
#define VVI vector< VI > 
#define pb push_back
#define mp make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORC(it,kont) for(__typeof((kont).begin()) it = (kont).begin(); it != (kont).end(); ++it )

using namespace std;

string A = "welcome to code jam";

int a[501][20];

int main()
    {
    int TC;
    cin >> TC; getchar();
    FOR( tc, 0 , TC )
       {
       char bla[600];
       gets( bla );
             
       string s;
       FOR( i, 0, strlen(bla)) s += bla[i];
       memset( a, 0, sizeof(a ));
       a[0][0] = 1;
       FOR( i , 0, ((int)s.size()) + 1 ) 
           FOR( j, 0, 19 )
              if ( a[i][j] )
                 {
                 FOR( k, i+1, ((int)s.size()) + 1 ) 
                    if ( s[k - 1] == A[j] ) 
                       {
                       a[k][j+1] += a[i][j]; 
                       a[k][j+1] %= 10000;
                       }
                 }
       
      // FOR( i , 0, 20 ) { FOR ( j, 0, 20 ) cout << a[i][j] << " "; cout << endl; } 
       
       int sol = 0;
       FOR( i , 0, 501 ) 
           sol = ( sol + a[i][19] ) % 10000;
       
       printf("Case #%d: %04d\n",tc+1,sol);
       
       }      
   // system("pause");
    return 0;
    }
