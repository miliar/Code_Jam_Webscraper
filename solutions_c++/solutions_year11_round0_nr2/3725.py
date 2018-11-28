#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

string main2() {
	int t;
	string s, sf, news;
	map<string,char> mc;
	map<char,string> mo;
	bool flag;

	cin >> t;
	for( int i = 0; i < t; i++ ) {
		cin >> s;
		sf = s.substr( 0, 2 );
		mc[sf] = s[2];
		reverse(sf.begin(), sf.end());
		mc[sf] = s[2];
	}

	cin >> t;
	for( int i = 0; i < t; i++ ) {
		cin >> s;
		if ( mo.find( s[0] ) == mo.end() )
			mo[s[0]] = s[1];
		else
			mo[s[0]] = mo[s[0]] + s[1];
		if ( mo.find( s[1] ) == mo.end() )
			mo[s[1]] = s[0];
		else
			mo[s[1]] = mo[s[1]] + s[0];
	}
	cin >> t;
	cin >> s;
	for( int i = 1; i < s.size(); i++ ) {	
		if( mc.find(s.substr( i - 1, 2 ) ) != mc.end() ) {
			s = s.substr( 0, i - 1 ) + mc[s.substr( i - 1, 2 )] + s.substr( i + 1, s.length());
			continue;

		}
		if( mo.find( s[i] ) != mo.end() ) {
			flag = 0;
			for( int j = 0; j < i; j++ ) {
				news = mo[s[i]]; 
				for( int k = 0; k < news.length(); k++ ) {
					if( s[j] == news[k] ) {
						flag = 1;
					}
				}
			}
			if( flag ) {
				s = s.substr( i + 1 );
				i = 0;
			}
		}
	}
	return s;
}
int main()
{
	int T;
	cin >> T;
	string s, sf;
	for( int i = 0; i < T; i++ ) {
		s = main2();
		sf = "";
		for( int j = 0; j < s.size(); j++ ) {
			sf = sf + s[j] + ", ";
		}
		sf = sf.substr( 0, sf.length() - 2 );
		cout << "Case #" << i+1 << ": [" << sf << "]" << endl;
	}
}
	
