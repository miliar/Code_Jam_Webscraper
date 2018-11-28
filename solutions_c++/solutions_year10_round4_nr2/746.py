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

int N;
int P;
VI mec;
VI cijena;
const int oo = ( 1 << 25 ) ;

int dp[1100][20];

int go( int pos, int dosad) 
    {
    int& sol = dp[pos][dosad];
    if ( sol != -1 ) return sol;
    if ( pos >= N/2 ) 
       {
       int y = min( mec[(pos - N/2)*2], mec[(pos - N/2)*2 + 1] );
       //cout <<"blabla" <<  pos << " " << dosad << " " << y << endl;
       if ( y < dosad  ) { sol = oo; }
       else if ( y >= dosad + 1 ) { sol = 0; } 
       else { sol = cijena[pos];  } 
   //    cout << pos << " " << y << " " << dosad << " " << sol << endl;
       return sol;   
       }
    
    sol = 0;
    int sol1 = cijena[pos] + go( pos * 2, dosad ) + go( pos*2 + 1, dosad ) ;
    int sol2 = go( pos * 2, dosad + 1) + go( pos*2 + 1, dosad + 1 ) ;
    
    sol = min ( sol1, sol2 ) ;
    if ( sol > oo ) sol = oo; 
 //   cout << pos << " " << dosad << " " << sol << endl;
    return sol;
    
    }

int main()
    {
    cin >> test_cases;
    for( int test_nmbr = 0; test_nmbr < test_cases; ++test_nmbr ) 
         {
         mec.clear();
         cijena.clear();
         memset(dp,-1,sizeof(dp));
         cin >> P;
         N = ( 1 << P );
         mec.resize( N ) ;
         FOR( i, 0, N ) cin >> mec[i];
        // FOR( i,0, N) mec[i] = P - mec[i];
       //  FOR( i , 0, N ) cout << mec[i] << endl;
         cijena.resize( N - 1 ) ;
         FOR ( i,0 , N- 1) cin >> cijena[i];
         cijena.pb( 0 ) ;
         
         reverse( cijena.begin(), cijena.end() ) ;
         reverse( mec.begin(), mec.end());
        // FOR( i, 0, N) cout << cijena[i] << endl;
        // cout << "tu" << endl;
         int sol = go( 1, 0);
         
         
         
         cout << "Case #" << test_nmbr + 1 << ": " << sol << endl;
         }
          
    return 0;
    }
