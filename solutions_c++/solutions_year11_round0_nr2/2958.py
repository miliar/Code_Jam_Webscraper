#include <iostream>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

int comb[26][26];
bool opos[26][26];

string Combine( const string& S ) {
	int size = (int)S.size();
	if( size < 2 ) return S;
	if( comb[ S[0]-'A' ][ S[1]-'A' ] != -1 )
		return (char)( comb[ S[0]-'A' ][ S[1]-'A' ] + 'A' ) + S.substr( 2 );
	if( comb[ S[size-2]-'A' ][ S[size-1]-'A' ] != -1 )
		return S.substr( 0, size-2 ) + (char)( comb[ S[size-2]-'A' ][ S[size-1]-'A' ] + 'A' );
	return S;
}

string Oppose( const string& S ) {
	int size = (int)S.size();
	if( size < 2 ) return S;
	for( int i=0; i<size-1; i++ )
		if( opos[ S[i]-'A' ][ S[size-1]-'A' ] ) return "";
	return S;
}

int main() {
	freopen( "B_Large.in", "r", stdin );
	freopen( "B_Large.out", "w", stdout );

	int TC;
	cin >> TC;

	for( int TCC=1; TCC<=TC; TCC++ ) {
		int C, D, N;
		memset( comb, -1, sizeof comb );
		memset( opos, false, sizeof opos );
		string str;
		cin >> C;
		for( int i=0; i<C; i++ ) {
			string S;
			cin >> S;
			comb[ S[0]-'A' ][ S[1]-'A' ] = S[2]-'A';
			comb[ S[1]-'A' ][ S[0]-'A' ] = S[2]-'A';
		}
		cin >> D;
		for( int i=0; i<D; i++ ) {
			string S;
			cin >> S;
			opos[ S[0]-'A' ][ S[1]-'A' ] = true;
			opos[ S[1]-'A' ][ S[0]-'A' ] = true;
		}
		cin >> N;
		cin >> str;

		string ret;
		for( int i=0; i<(int)str.size(); i++ ) {
			ret += str[i];
			//cout << ret << ' ';
			ret = Combine( ret );
			ret = Oppose( ret );
			//cout << ret << endl;
		}

		cout << "Case #" << TCC << ": [";
		for( int i=0; i<(int)ret.size(); i++ ) {
			if( i != 0 ) cout << ", ";
			cout << ret[i];
		}
		cout << "]" << endl;
	}
}