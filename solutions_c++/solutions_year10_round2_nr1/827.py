#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

string pop_dir( string &d );
void split_insert( vector< string > &M, string &d );
bool parents( vector< string > &M, string &d );

int main()
{
    int t, n, m, k = 0;
    scanf( "%d", &t );
    while( k++ < t )
    {
        printf( "Case #%d: ", k );
        scanf( "%d%d", &n, &m );
        vector< string > R( n, "" );
        string next, tmp;
        for( int i = 0; i < n; ++i )
            cin >> R[ i ];
        int count = 0;
        for( int i = 0; i < m; ++i )
        {
            cin >> next;
            tmp = next;
            while( !parents( R, tmp ) )
            {
                tmp = pop_dir( tmp );
                ++count;
                if( tmp.size() < 2 )
                    break;
            }
            split_insert( R, next );
        }
        printf( "%d\n", count );
    }
    return 0;
}

void split_insert( vector< string > &M, string &d )
{
    string dir = "/";
    for( int i = 1, s = d.size(); i < s; ++i )
    {
        if( d[i] == '/' )
            M.push_back( dir );
        dir += d[i];
    }
    M.push_back( d );
}

/*
    returns true if the d exists in M
*/
bool parents( vector< string > &M, string &d )
{
    for( int i = 0, s = M.size(); i < s; ++i )
        if( M[i] == d )
            return true;
    return false;
}

string pop_dir( string &d )
{
    int s = d.size();
    for( int i = s - 1; i >= 0; --i )
        if( d[ i ] == '/' )
            return d.substr( 0, i );
    return "/";
}
