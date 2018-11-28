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

#define MOD 100003

pair<int,int> mod_inv( long long x, long long y ) 
{
if ( x % y == 0 ) return make_pair(0,1);
pair <int, int> p = mod_inv( y, x % y);
return make_pair( p.second, p.first - p.second*(x/y)); 
}

int N;

long long dp[600][600];

long long fakt[600][600];

void izracunaj_fakt()
     {
     fakt[0][0] = 1;
     for( int i = 1; i < 600; ++i )                
       for( int j = 0; j <= i; ++j ) 
            {
            if ( j == 0 || j == i ) fakt[i][j] = 1; 
            else fakt[i][j] = ( fakt[i-1][j] + fakt[i-1][j-1] ) % MOD;
                
            }
     return;
     }


long long go( int x, int p )
{
long long& sol = dp[x][p];
if ( sol!=-1 ) return sol;
if ( p == 1 ) { return sol = 1; } 
if ( x <= p ) return sol = 0; 

sol = 0;

for( int i = 1; i <= p-1; ++i  )
     {
     long long bla = go( p , i ) ;
     bla *= fakt[x-p-1][p-i-1];
     sol += bla;
     sol %= MOD;
     }

return sol;
}


int main()
    {
    izracunaj_fakt();
    cin >> test_cases;
    for( int test_nmbr = 0; test_nmbr < test_cases; ++test_nmbr ) 
         {
         cin >> N;
         //cout << N << endl;
         memset( dp , -1,sizeof( dp ));
         long long sol = 0;
         for( int i = 1; i <= N-1; ++i ) 
            {
            sol += go( N, i ) ;  
            sol %= MOD;
            }
         cout << "Case #" << test_nmbr + 1 << ": " << sol << endl;
         }
    //system("pause");
    return 0;
    }
