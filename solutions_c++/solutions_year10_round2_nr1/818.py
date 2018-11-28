#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

int n, m;
string pa[100024];
bool vis[100024];
bool us[10024];

vector<int> g[100024];

map<string,int> mp;

int md;

string sp( string str )
{
    int found;
    string par;

    found = str.find_last_of( "/\\" );
    par = str.substr( 0, found );
    return par;
}

void dfs( int v )
{
    int i, u;
    for ( i = 0; i < g[v].size(); i++ )
    {
        u = g[v][i];
        if ( vis[u] == 0 )
        {
            vis[u] = 1;
            dfs( u );
            if ( u > n )
                md++;
        }
    }
}

int main()
{
    int i, j, k;
    int be, kbe;
    int T;

    string s;

    scanf( "%d", &T );
    for ( int tt = 1; tt <= T; tt++ )
    {
        md = 0;
        scanf( "%d %d", &n, &m );
        pa[0] = "";
        mp.clear();
        mp[pa[0]] = 0;
        memset( us, 0, sizeof( us ) );
        for ( i = 1; i <= n; i++ )
        {
            cin >> pa[i];
            mp[pa[i]] = i;
        }

        for ( i = n+1; i <= n+m; i++ )
        {
            cin >> pa[i];
            if ( mp.find( pa[i] ) == mp.end() )
                mp[pa[i]] = i;
            else
                us[i] = 1;
        }

        k = n+m;
        for ( i = n+1; i <= n+m; i++ )
        {
            s = sp( pa[i] );
            while ( mp.find( s ) == mp.end() )
            {
                k++;
                mp[s] = k;
                pa[k] = s;
                s = sp( s );
            }
        }

        for ( i = 0; i <= k; i++ )
        {
            g[i].clear();
        }

        for ( i = 1; i <= k; i++ )
        {
            s = sp( pa[i] );
            if ( us[i] == 0 )
            {
                s = sp( pa[i] );
                g[mp[s]].push_back(mp[pa[i]]);
                g[mp[pa[i]]].push_back(mp[s]);
            }
        }

        memset( vis, 0, sizeof( vis ) );
        vis[0] = 1;
        dfs( 0 );

        printf( "Case #%d: %d\n", tt, md );
    }
}
