#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin( "A-small-attempt0.in" );
ofstream fout( "A-small-attempt0.out" );

#define cin fin
#define cout fout

string a, b;
char mp[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r',
	'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
	/*getline( cin, a );
	getline( cin, b );
	for( int i = 0; i < 26; i++ )	mp[i] = 'A';
	for( int i = 0; i < a.length(); i++ ) {
		if( a[i] == ' ' )	continue;
		mp[a[i] - 'a'] = b[i];
	}
	for( int i = 0; i < 26; i++ )
		cout << "'" << mp[i] << "', ";
	cout << endl;*/
	int t;
	cin >> t;
	getline( cin, a );
	for( int i = 0; i < t; i++ ) {
		getline( cin, a );
		for( int j = 0; j < a.length(); j++ ) {
			if( a[j] == ' ' )	continue;
			a[j] = mp[a[j] - 'a'];
		}
		cout << "Case #" << i + 1 << ": " << a << endl;
	}
	return 0;
}