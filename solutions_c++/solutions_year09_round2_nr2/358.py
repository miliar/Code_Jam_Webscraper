#include<iostream>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<algorithm>
#include<string>
#include<cstring>
#include<memory.h>
#include<cmath>
#include<cassert>
#include<sstream>
#include<cstdlib>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<pii> vpii;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define write( x ) { cerr << #x << " = " << x << endl; }

const int INF = 1 << 29;


int main() {
    freopen( "in", "r", stdin );
    freopen( "out", "w", stdout );
    int t;
    cin >> t;
    for( int test = 1; test <= t; ++test ) {
	string s;
	cin >> s;
	cout << "Case #" << test << ": ";
	int i;
	for( i = s.size() - 2; i >= 0; --i )
	    if( s[ i ] < s[ i + 1 ] ) break;
//	write( i );
	if( i == -1 ) {
	    int pos = 0;
	    for( int j = 0; j < (int)s.size(); ++j )
		if( s[ j ] > '0' && s[ j ] < s[ pos ] ) pos = j;
	    swap( s[ 0 ], s[ pos ] );
	    sort( s.begin() + 1, s.end() );
	    s.insert( 1, "0" );
	    cout << s << endl;
	}
	else {
	    int pos = i + 1;
	    for( int j = i + 1; j < s.size(); ++j )
		if( s[ j ] > s[ i ] && s[ j ] < s[ pos ] )
		    pos = j;
	    swap( s[ i ], s[ pos ] );
	    sort( s.begin() + i + 1, s.end() );
	    cout << s << endl;
	}
    }
    return 0;
}
