#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define forn(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
typedef long long ll;
// NUNCA DEFINIR int max....

#define MOD 100003LL
long long dp[550][550];
long long comb[550][550];

long long go(int place, int quedan)
{
 //   cout << place << " "  << quedan << endl;
    if( quedan == 1 && place > 1 ) return 1;
    if( quedan == 1 && place <= 1 ) return 0;
    if( place <= 1 ) return 0;

    ll & res = dp[place][quedan];
    if( res >= 0 ) return res;
    res = 0 ;
    for( int i = 1; i < quedan; i ++ )
    {
        if( quedan - i <= place - quedan && place != quedan)
        res = ( res +  comb[place-quedan-1][quedan-i-1] * go(quedan, i) ) % MOD;
    }
    return res;
}

int main()
{
    int casos;
    ifstream ifs("C-large.in", ifstream::in );
    ofstream ofs("C-large.txt");
    ifs >> casos;
    for( int i = 0 ; i < 550; i ++ ) for( int j = 0 ; j < 550; j ++ ) dp[i][j] = -1;
    for( int i = 0 ; i < 550 ; i ++ ) comb[i][i] = comb[i][0] = 1;
    for( int i = 1 ; i < 550 ; i ++ )
        for( int j = 1 ; j < i ; j ++ )
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j] ) % MOD;
    for( int t = 0 ; t < casos; t ++ )
    {
        int N;
        ifs >> N;


        ll res = 0 ;
        for( int i = 1; i < N ; i ++ )
        {
            res += go(N,i);
            res = res % MOD;
        }


        ofs << "Case #" << (t+1) << ": " << res << "\n";
    }
    return 0;
}


