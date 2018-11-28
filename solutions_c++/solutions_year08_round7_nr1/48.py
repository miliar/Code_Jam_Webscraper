#include <iostream>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <functional>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define FOR( i, s, n ) for (int i = s; i < n; ++i)
#define CLEAR( x, v ) memset( x, v, sizeof( x ) )

int N;
bool ing[1000];
vector<int> x[1000];
map<string,int> m;
int cnt;

int cache[1000];

int solve( int v )
{
    int& res = cache[v];
    if (res != -1) return res;

    vector<int> r( x[v].size() );
    FOR( i, 0, x[v].size() )
    {
        r[i] = solve( x[v][i] );
    }

    sort( r.begin(), r.end() );

    int p = x[v].size() + 1;
    FOR( i, 0, r.size() )
    {
        int j = r.size() - i - 1;
        int q = r[i];
        if (q+j > p) p = q+j;
    }

    res = p;
    return res;
}

int get( string s )
{
    if (m.count( s ) == 0)
    {
        m[s] = cnt++;
    }
    return m[s];
}

int main( void )
{
    int TC;
    cin >> TC;

    FOR( tc, 0, TC )
    {
        int M;
        string s, t;

        cnt = 0;
        cin >> N;

        CLEAR( ing, 0 );
        FOR( j, 0, N ) x[j].clear();
        m.clear();
        CLEAR( cache, -1 );

        FOR( i, 0, N )
        {
            cin >> s >> M;
            get(s);
            FOR( j, 0, M )
            {
                cin >> t;
                if (t[0] >= 'a' && t[0] <= 'z') ing[get(s)] = true;
                else
                {
                    x[get(s)].push_back( get(t) );
                }
            }
        }

        int res = solve( 0 );
        cout << "Case #" << (tc+1) << ": " << res << endl;
    }

    return 0;
}
