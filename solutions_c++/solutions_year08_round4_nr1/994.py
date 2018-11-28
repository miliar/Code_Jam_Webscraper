#include <cstdio>
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

#define VI vector<int>
#define VS vector<string>
#define VVI vector< VI >
#define PB push_back
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort( ALL(a) )
#define IPAIR pair<int,int>
#define VIPAIR vector< IPAIR >
#define FOR(i,b,n) for ( int i = (b); i < (n); i++ )
#define REP(i,n) FOR(i,0,n)
#define ll long long

int solve( VI& v, VI& gates, VI& change, int V )
{
    int m = v.size();
    int m0 = change.size();
    int ret = 10000000;
#if 0
    cout << "V = " << m0 << endl;
    cout << change[0] << change[1] << change[2] << change[3];
#endif
    for ( int mask = 0; mask < ( 1 << m0 ); mask++ ) {
        VI ngates = gates;
        int c = 0;
        for ( int j = 0; j < m0; j++ ) {
            if ( ( mask & ( 1 << j ) ) && change[j] ) {
                ngates[j] = 1 - ngates[j];
                c ++;
            }
        }
        VI nv = v;
        for ( int j = m0-1; j >= 0; j-- ) {
            if ( ngates[j] ) {
                nv[j] = nv[2*(j+1)-1] & nv[2*(j+1)+1-1];
            }
            else {
                nv[j] = nv[2*(j+1)-1] | nv[2*(j+1)+1-1];
            }
        }
#if 0
        for ( int i = 0; i < m0; i++ ) {
            cout << nv[i];
        }
        cout << "(";
        for ( int i = 0; i < m0; i++ ) {
            cout << ngates[i];
        }
        cout << ")";
        cout << endl;
#endif
        if ( nv[0] == V ) {
            ret <?= c;
        }
    }
    return ret;
}

int main()
{
    int numCases;
    cin >> numCases;
    
    for ( int prob = 1; prob <= numCases; prob++ ) {
        int result = 0;
        int M;
        int V;
        cin >> M >> V;
        VI v( M, 0 );
        VI gates( (M-1)/2, 0 );
        VI change( (M-1)/2, 0 );
        int i;
        for ( i = 0; i < (M-1)/2; i++ ) {
            cin >> gates[i] >> change[i];
        }
        for ( ; i < M; i++ ) {
            cin >> v[i];
        }
        result = solve( v, gates, change, V );
        if ( result == 10000000 )
            cout << "Case #" << prob << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << prob << ": " << result << endl;
    }
    
    return 0;
}
