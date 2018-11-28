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
#include <cstring>

using namespace std;

#define ll          long long
#define VI          vector<int>
#define ALL(a)      (a).begin(), (a).end()
#define SORT(a)     sort( ALL(a) )
#define PB          push_back
#define FOR(i,a,b)  for( int i = (a); i < (int)(b); i++ )
#define dump_(x)     cerr << #x << " = " << (x) << " ";
#define dump(x)     cerr << #x << " = " << (x) << endl
#define dump_vec(x) FOR(zZz,0,x.size()) cout << x[zZz] << " "; cout << endl


template< typename type > type readOne()
{
    type res;
    char inp[5000];
    char* dum = fgets( inp, sizeof( inp ), stdin );
    stringstream ss( dum );
    ss >> res;
    return res;
}

template< typename type > vector<type> readMulti()
{
    vector<type> res;
    char inp[5000];
    char* dum = fgets( inp, sizeof( inp ), stdin );
    stringstream ss( dum );
    for ( type t; ss >> t; )
        res.push_back( t );
    return res;
}

//
//
// LET'S START
//
//
vector<int> groups;
vector<int> arr;
vector<int> done;

void dfs( int pos, int depth )
{
    if ( done[pos] ) {
        groups.push_back( depth );
        FOR( i, 0, arr.size() )
            if ( !done[i] ) {
                dfs( i, 0 );
                break;
            }
        return;
    }
    done[pos] = 1;
    dfs( arr[pos], depth + 1 );
}

double doit( int n )
{
    return n == 1 ? 0 : n;
}

double doCase()
{
    arr.clear();
    int n;
    cin >> n;
    FOR( i, 0, n ) { int t; cin >> t; arr.push_back(t - 1); }
    done = vector<int>( n, 0 );
    groups.clear();
    dfs(0, 0);

    double res = 0;
    FOR( i, 0, groups.size() ) res += doit( groups[i] );
    return res;
}

int main()
{
    int cases = readOne<int>();
    for (int caseno = 1; caseno <= cases; caseno++) {
        printf( "Case #%d: %.10f\n", caseno, doCase() );
    }
    return 0;
}

