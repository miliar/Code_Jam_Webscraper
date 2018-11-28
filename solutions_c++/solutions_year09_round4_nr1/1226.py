#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <numeric>

using namespace std;

#define ll          long long
#define VI          vector<int>
#define ALL(a)      (a).begin(), (a).end()
#define SORT(a)     sort( ALL(a) )
#define PB          push_back
#define FOR(i,a,b)  for( int i = (a); i < (int)(b); i++ )
#define dump(x)     cerr << #x << " = " << (x) << endl
#define dump_vec(x) FOR(i,0,x.size()) cout << x[i] << " "; cout << endl


template< typename type > type readOne()
{
    type res;
    char inp[5000];
    
    gets( inp );
    stringstream ss( inp );
    ss >> res;
    return res;
}

template< typename type > vector<type> readMulti()
{
    vector<type> res;
    char inp[5000];
    
    gets( inp );
    stringstream ss( inp );
    for ( type t; ss >> t; )
        res.push_back( t );
    return res;
}

//
//
// LET'S START
//
//

int doit( VI& must, int pos )
{
    if ( pos >= must.size() ) return 0;
    if ( must[pos] > pos )
    {
        FOR( i, must[pos], must.size() )
            if ( must[i] <= pos )
            {
                swap( must[pos], must[i] );
                return 1 + doit( must, pos + 1 );
            }
        
    }
}

map< VI, int > memo;
int doit_s( VI& must )
{
    queue< VI > q;
    q.push( must );
    memo[ must ] = 0;
    while ( !q.empty() )
    {
        VI node = q.front();
        int cur = memo[ node ];
//        dump_vec( node );
//        dump( cur );
        q.pop();
        bool ok = true;
        FOR( i, 0, node.size() )
            if ( node[i] > i )
            {
                ok = false;
                break;
            }
        if ( ok )
            return cur;
        FOR( i, 0, node.size() )
        {
            {
                FOR( j, 0, node.size() ) if ( abs( i - j ) == 1 )
                {
                    VI next = node;
                    swap( next[i], next[j] );
                    if ( !memo.count( next ) )
                    {
                        memo[next] = cur + 1;
                        q.push( next );
                    }
                }
            }
        }
    }
    return -1;
}

int doCase()
{
    //
    // READ INPUT
    //
    int N = readOne<int>();
    VI must( N );
    for ( int i = 0; i < N; i ++ )
    {
        string line = readOne<string>();
        int pos = 0;
        for ( int j = 0; j < N; j ++ )
        {
            if ( line[j] == '1' )
                pos = j;
        }
        must[i] = pos;
    }
    
    //
    // DOIT!
    //
    //return doit( must, 0 );
    
    memo.clear();
    return doit_s( must );
}

int main()
{
    int cases = readOne<int>();
	for (int caseno = 1; caseno <= cases; caseno++)
        cout << "Case #" << caseno << ": " << doCase() << endl;

	return 0;
}

