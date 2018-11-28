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

int X1, X2, X3, Y1, Y2, Y3;
void solve( ll N, ll M, ll A )
{
    for ( int a1 = 0; a1 <= N; a1++ ) {
        for ( int b1 = 0; b1 <= M; b1++ ) {
            for ( int a2 = 0; a2 <= N; a2++ ) {
                for ( int b2 = 0; b2 <= M; b2++ ) {
                    if ( abs( a1 * b2 - a2 * b1 ) == A ) {
                        X1 = 0;
                        Y1 = 0;
                        X2 = X1 + a1;
                        Y2 = Y1 + b1;
                        X3 = X1 + a2;
                        Y3 = Y1 + b2;
                        return;
                    }
                }
            }
        }
    }
}

int main()
{
    int numCases;
    cin >> numCases;
    
    for ( int prob = 1; prob <= numCases; prob++ ) {
        ll result = 0;
        ll N, M, A;
        cin >> N >> M >> A;
        X1 = -1;
        solve( N, M, A );
        if ( X1 == -1 )
            cout << "Case #" << prob << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << prob << ": " << X1 << " " << Y1 << " " << X2 << " " << Y2 << " " << X3 << " " << Y3 << endl;
    }
    
    return 0;
}
