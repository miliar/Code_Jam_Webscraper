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

vector<pair<pair<string, long double>,pair<int,int> > > tree;

int build( string s ) {
    //write( s );
    int begin, end;
    for( begin = 0; begin < s.size(); ++begin )
	if( s[ begin ] == '(' ) break;
    ++begin;
    for( end = s.size() - 1; end >= 0; --end )
	if( s[ end ] == ')' ) break;
    --end;
    string str = "";
    int i;
    for( i = begin; i < (int)s.size() && ( s[ i ] != '(' && s[ i ] != ')' ); ++i )
	str += s[ i ];
    istringstream ss( str );
    long double a;
    ss >> a;
    string qwe;
    ss >> qwe;
    tree.pb( mp( mp( qwe, a ), mp( -1, -1 ) ) );
    int ans = tree.size() - 1;
    int st = 0, j;
    int flag = 0;
    for( j = begin; j < s.size(); ++j )
	if( s[ j ] == '(' ) {
	    st++;
	    flag = 1;
	}
	else if( s[ j ] == ')' ) {
	    --st;
	    if( !st ) break;
	}
    if( flag && !st ) {
	int val = build( s.substr( i, j - i + 1 ) );
	//write( val );
	tree[ ans ].y.x = val;//build( s.substr( i, j - i + 1 ) );
    }
    st = 0, flag = 0;
    int k;
    for( k = j + 1; k < s.size(); ++k )
	if( s[ k ] == '(' ) {
	    st++;
	    flag = 1;
	}
	else if( s[ k ] == ')' ) {
	    --st;
	    if( !st ) break;
	}
    if( flag && !st ) {
	int val = build( s.substr( j + 1, k - j ) );
	//write( val );
	tree[ ans ].y.y = val;//build( s.substr( j + 1, k - j ) );
    }
    //write( ans );
    return ans;
}
set<string> Set;
long double dfs( int v ) {
    if( tree[ v ].y.x == -1 && tree[ v ].y.y == -1 ) return tree[ v ].x.y;
    if( Set.find( tree[ v ].x.x ) != Set.end() ) {
	return tree[ v ].x.y * dfs( tree[ v ].y.x );
    }
    else return tree[ v ].x.y * dfs( tree[ v ].y.y );
}
int main() {
    freopen( "in", "r", stdin );
    freopen( "out", "w", stdout );
    int t;
    cin >> t;
    for( int test = 1; test <= t; ++test ) {
	int n;
	cin >> n;
	tree.clear();
	string s = "";
	getchar();
	for( int i = 0; i < n; ++i ) {
	    string str;
	    getline( cin, str );
	    s += str;
	}
//	write( s );
	build( s );
	/*for( int i = 0; i < tree.size(); ++i ) {
	    write( tree[ i ].x.x );
	    write( tree[ i ].x.y );
	    write( tree[ i ].y.x );
	    write( tree[ i ].y.y );
	    write( "------------------" );
	}*/
	cin >> n;
	cout << "Case #" << test << ":\n";
	for( int i = 0; i < n; ++i ) {
	    cin >> s;
	    int m;
	    cin >> m;
	    Set.clear();
	    for( int j = 0; j < m; ++j ) {
		cin >> s;
		Set.insert( s );
	    }
	    long double ans = dfs( 0 );
	    cout.precision( 7 );
	    cout << fixed << ans << endl;
	}
    }
    return 0;
}
