#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen( "x.in", "r" , stdin );
	freopen( "y", "w", stdout );
	
	string conv = "yhesocvxduiglbkrztnwjpfmaq";
	
	string s;
	int i = 0;
	
	int test;
	cin >> test;
	
	getline( cin,s );
	
	for ( int i =1 ; i <= test; i++ ) {
		getline ( cin, s );
		cout << "Case #" << i << ": ";
		for ( int j = 0 ; j < s.length(); j++ ) {
			if ( s[j] == ' ' ) {
				cout << ' ';
			} else {
				cout << conv[s[j]-'a'];
			}
		}
		cout << endl;
	}
	
	return 0;
}
