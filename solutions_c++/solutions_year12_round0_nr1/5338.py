#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

char f[256] = {0};
char c[26] = {
	'y','h','e','s','o','c','v','x','d','u','i','g','l',
	'b','k','r','z','t','n','w','j','p','f','m','a','q'
};

int main(){
	for(int i=0 ; i < 26 ; i++ ){
		f[i+'a'] = c[i];
	}
	
	int T;
	cin >> T;
	cin.ignore();
	for(int t=1 ; t <= T ; t++ ){
		string s;
		getline(cin, s);
		for(int i=0 ; i < s.size() ; i++ ){
			if( s[i] != ' ' ){
				s[i] = f[ s[i] ];
			}
		}
		cout << "Case #" << t << ": " << s << endl;
	}
}
