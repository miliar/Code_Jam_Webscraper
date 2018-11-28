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
int main()
{
    int casos;
    ifstream ifs("B-large.in", ifstream::in );
    ofstream ofs("B-large.txt");
    ifs >> casos;
    for( int t = 0 ; t < casos; t ++ )
    {
        ll N, K, B, T;
        ifs >> N >> K >> B >> T;
        vector<ll> X, V;
        ll aux;
        for( int i = 0 ; i < N ; i ++ )
        {
            ifs >> aux; X.PB(aux);
        }for( int i = 0 ; i < N ; i ++ )
        {
            ifs >> aux; V.PB(aux);
        }
        int NOLLEGAN = 0 ;
        int res = 0 ;
        int cant = 0 ;
        for( int i = N-1; i >= 0 ; i -- )
        {
            if( cant >= K ) break;
            if( (V[i] * T) >= (B - X[i]) )
            {
                cant++;
                res += NOLLEGAN;
            }else
            {
                NOLLEGAN++;
            }
        }


        if( cant >= K )
        ofs << "Case #" << (t+1) << ": " << res << "\n";
        else ofs << "Case #" << (t+1) << ": " << "IMPOSSIBLE" << "\n";
    }
    return 0;
}


