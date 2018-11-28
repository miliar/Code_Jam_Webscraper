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
#define write( x, y ) cerr << x << y << endl;

const int INF = 1 << 29;

vector<set<char> > v;

set<int> parse( string & s, int pos ) {
    set<int> res;
    if( isalpha( s[ pos ] ) ) res.insert( s[ pos ] );
    else {
	for( ++pos; s[ pos ] != ')'; ++pos )
	    res.insert( s[ pos ] );
	++pos;
    }
    return res;
}
int main() {
    freopen( "in", "r", stdin );
    freopen( "out", "w", stdout );
    int l, d, n;
    cin >> l >> d >> n;
    vector<string> dict( d );
    for( int i = 0; i < d; ++i )
	cin >> dict[ i ];
    for( int t = 1; t <= n; ++t ) {
	string s;
	cin >> s;
	int pos = 0;
	v.assign( l, set<char>() );
	for( int i = 0; pos < (int)s.size(); ++i ) {
	    if( isalpha( s[ pos ] ) ) v[ i ].insert( s[ pos++ ] );
	    else {
		for( ++pos; s[ pos ] != ')'; ++pos )
		    v[ i ].insert( s[ pos ] );
		++pos;
	    }
	}
	int ans = 0;
	for( int i = 0; i < d; ++i ) {
	    int flag = 1;
	    for( int j = 0; j < l; ++j )
		if( v[ j ].find( dict[ i ][ j ] ) == v[ j ].end() ) {
		    flag = 0;
		    break;
		}
	    if( flag ) ++ans;
	}
	cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
