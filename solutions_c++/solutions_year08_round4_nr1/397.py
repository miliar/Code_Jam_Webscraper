#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <cmath>
#include <sstream>
using namespace std;
typedef long long LL;
typedef vector < int > VI;
#define SZ(X) ((int)X.size())
int m;
const int inf = 1 << 29;
bool isleaf ( int pos ) {
	return pos >= (m + 1 )/2 ;
}

const int mn = 10010;
int cache [mn][2] , isand[mn] , val[mn] , cha[mn];
int go ( int pos , int req ) {
//	cout << " Inside  " << pos <<"::" <<req <<endl;
	int & res = cache[pos][req];
	if ( res != -1 ) return res;
	res = inf;
	if ( isleaf ( pos ) ) {
//		cout << pos <<"L::" << val[pos] << << endl;
		if ( req == val [pos] ) {
			res = 0;
			return 0;
		}
		else {
			res = inf;
			return inf;
			}
	}
	if ( isand [ pos ] ) {
		for ( int i=0;i<=1;i++ )
		for ( int j=0;j<=1;j++ ) if (( i & j ) == req )
		res = min ( res , go ( pos * 2  , i ) + go ( pos * 2 + 1 , j ) );
	}
	else {
		for ( int i=0;i<=1;i++ )
		for ( int j=0;j<=1;j++ ) if (( i | j ) == req )
		res = min ( res , go ( pos * 2  , i ) + go ( pos * 2 + 1 , j ) );
	}
	if ( cha[pos] ) {
		if ( isand [pos] ) {
		for ( int i=0;i<=1;i++ )
		for ( int j=0;j<=1;j++ ) if (( i | j ) == req ){
//			cout << "CH " << pos << endl;
//			if ( pos == 3 ) cout << 1 +  go ( pos * 2  , i ) + go ( pos * 2 + 1 , j ) << endl;
		res = min ( res ,1 +  go ( pos * 2  , i ) + go ( pos * 2 + 1 , j ) );
		}
		}
		else {
		for ( int i=0;i<=1;i++ )
		for ( int j=0;j<=1;j++ ) if (( i & j ) == req )
		res = min ( res ,1 +  go ( pos * 2  , i ) + go ( pos * 2 + 1 , j ) );
		}
	}
//	cout << "Out " << pos <<"::" << req <<"::" << res << endl;
	return res;
}
int main() {
	string imp = "IMPOSSIBLE";
	int t;
	cin >> t;
	for ( int n__ = 1 ; n__ <= t; n__ ++ ) {
		cout << "Case #" << n__ <<": " ;
		int req;
		cin >> m >> req;
		memset ( cache , -1 , sizeof ( cache ) );
		for ( int i=1;i<=(m-1)/2;i++ ) {
			isand[i] = 0;
			cin >> isand[i] >> cha[i];
		}
		for ( int cnt = (m-1)/2 + 1 ; cnt <= m ; cnt ++ ) {
			cin >> val[cnt] ;			
		}
		int res = go ( 1 , req );
		if ( res < inf ) cout << res << endl;
		else cout << imp << endl;
	}
	return 0;
}
