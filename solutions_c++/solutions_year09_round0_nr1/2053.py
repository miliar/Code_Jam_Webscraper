#include <iostream>
#include <vector>
#include <set>
#include <cassert>

using namespace std;

vector<string> dict;
set<char> poss[50];

int count( string s, int l ) {
	for( int i = 0; i < l; ++i ) {
		poss[i].clear();
	}
	int pos = 0;
	for( int i = 0; i < l; ++i ) {
		assert( pos < (int)s.size() );
		if( s[pos] == '(' ) {
			for( ++pos; pos < (int)s.size() && s[pos] != ')'; ++pos ) {
				poss[i].insert( s[pos] );
			}
		} else {
			poss[i].insert( s[pos] );
		}
		++pos;
	}
	
	int cnt = 0;
	for( int i = 0; i < (int)dict.size(); ++i ) {
		for( int j = 0; j < l; ++j ) {
			if( poss[j].find( dict[i][j] ) == poss[j].end() ) goto nexti;
		}
		++cnt;
	nexti:;
	}
	return cnt;
}

int main() {
		int l, d, n;

		cin >> l >> d >> n;	
		dict.clear();
		for( int i = 0; i < d; ++i ) {
			string s;
			cin >> s;
			dict.push_back( s );
		}
		for( int i = 0; i < n; ++i ) {
			string s;
			cin >> s;
			cout << "Case #" << i+1 << ": " << count( s, l ) << endl;
		}
		return 0;
}

