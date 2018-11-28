////////////////////////////////////////////////////////////////////////////////
//
// Google Codejam 2010
// Round ? - Problem A.
//
// Author : Kang, Jin-Kook, 2010.05.22
//
// * 
//

#include <stdio.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
//
/*
Input 
3
0 2
/home/gcj/finals
/home/gcj/quals
2 1
/chicken
/chicken/egg
/chicken
1 3
/a
/a/b
/a/c
/b/b

Output 
Case #1: 4
Case #2: 0
Case #3: 4
 
*/

//ifstream fin("input.txt");
//#define cin fin

struct Info;
typedef vector< string >		PathVec;
typedef map< string, Info* >	InfoVec;

struct Info
{
	InfoVec	sub_;
};

void parse( const string& path, PathVec& pathVec )
{
	string token;
	int len = path.size();
	for ( int i = 0; i < len; ) {
		int j = path.find( '/', i + 1 );
		if ( j < 0 ) j = len;
		pathVec.push_back( path.substr( i + 1, j - i - 1 ) );
		//cout << pathVec[ pathVec.size() - 1 ] << endl;
		i = j;
	}
}

int loadPath( Info* root, const string& path )
{
	PathVec pathVec;
	parse( path, pathVec );

	int nNeed = 0;
	Info* cur = root;

	for ( int i = 0, size = pathVec.size(); i < size; ++i ) {
		string& node = pathVec[ i ];

		InfoVec::iterator iter = cur->sub_.find( node );
		if ( iter != cur->sub_.end() ) {
			cur = iter->second;
		}
		else {
			cur->sub_[ node ] = new Info;
			cur = cur->sub_[ node ];
			++nNeed;
		}
	}

	return nNeed;
}

void cleanup( Info* root )
{
	// no need for gcj
}

int main( int argc, char *argv[] )
{
	int count;
	cin >> count;

	for ( int i = 1; i <= count; ++i ) {
		int n, m;
		cin >> n >> m;

		Info* root = new Info;
		string path;
		for ( int j = 0; j < n; ++j ) {
			cin >> path;
			loadPath( root, path );
		}

		int nNeed = 0;
		for ( int j = 0; j < m; ++j ) {
			cin >> path;
			nNeed += loadPath( root, path );
		}

		cleanup( root );

		cout << "Case #" << i << ": " << nNeed << endl;
	}

	return 0;
}
