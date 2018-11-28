#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream fin( "A.in" );
ofstream fout( "A.out" );
int mpRev[26], mp[26], test, cnt = 1;
string s, t;



int main(){
	memset( mp, -1, sizeof mp );
	memset( mpRev, -1, sizeof mpRev );
	for( int T = 0; T < 3; T++ ){
		getline( cin, s );
		getline( cin, t );
		int len = s.length();
		for( int i = 0; i < len; i++ ){
			if( s[i] == ' ')
				continue;
			mp[s[i] - 'a'] = t[i] - 'a', mpRev[t[i] - 'a'] = s[i] - 'a';
		}
	}
	mp[25] = 'q' - 'a';
	mpRev['q' - 'a'] = 25;
	mp['q' - 'a'] = 25;
	mpRev[25] = 'q' - 'a';
	/*for( int  i = 0; i < 26; i++ )
		if( mp[i] == -1 )
			cout << i << ' ' << (char)( i + 'a' ) << endl;
	for( int  i = 0; i < 26; i++ )
		if( mpRev[i] == -1 )
			cout << i << ' ' << (char)( i + 'a' ) << endl;
	*/
	#define cin fin
	#define cout fout
	cin >> test;
	//cout << "HERE " << endl;
	getline( cin, s );
	for( ; test--; ){
		getline( cin, s );
		cout << "Case #" << cnt++ << ": ";
		for( int i = 0; i < s.length(); i++ ){
			if( s[i] != ' ' )
				s[i] = mp[s[i] - 'a'] + 'a';
			cout << s[i];
		}
		cout << endl;
	}
	return 0;
}