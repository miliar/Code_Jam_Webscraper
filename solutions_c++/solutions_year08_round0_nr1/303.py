#include <vector>
#include <set>
#include <string>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <iostream>
#include <cassert>
#include <cctype>
#include <cmath>
#include <map>
#include <deque>
#include <algorithm>

using namespace std;

vector<int> list;
int s, q;
int dp[1001][101];
const int INF = 1000000000;

int rec( int k, int eng ) {
	if( k == q ) return 0;
	int& res = dp[k][eng];
	if( res != -1 ) return res;
	res = INF;
	
	// no swap
	if( list[k] != eng && eng != s ) {
		res = min( res, rec( k+1, eng ) );
	}
	// swap
	for( int i = 0; i < s; ++i ) {
		if( i == eng ) continue;
		if( list[k] == i ) continue;
		res = min( res, rec( k+1, i ) + (k==0?0:1) );
	}
	
	return res;
}

int main() {
	int cases;
	map<string,int> engines;
	
	cin >> cases;
	for( int caseid = 1; caseid <= cases; ++caseid ) {
		engines.clear();
		list.clear();
	
		cin >> s;
		while( getchar() != '\n') {}
		
		for( int i = 0; i < s; ++i ) {
			string engine_name;
			getline( cin, engine_name );
			engines[engine_name] = i;
		}
		
		cin >> q;
		while( getchar() != '\n' ) {}
		
		for( int i = 0; i < q; ++i ) {
			string engine_name;
			getline( cin, engine_name );
			
			map<string,int>::const_iterator iter = engines.find( engine_name );
			assert( iter != engines.end() );
			
			list.push_back( iter->second );
		}
		
		memset( dp, -1, sizeof(dp) );
		cout << "Case #" << caseid << ": " << rec( 0, s ) << endl;
	}
	return 0;
}

