#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

char replace ( char t ) {
	if (t == 'a')
		return 'y' ;
	if (t == 'b')
		return 'h' ;
	if (t == 'c')
		return 'e' ;
	if (t == 'd')
		return 's' ;
	if (t == 'e')
		return 'o' ;
	if (t == 'f')
		return 'c' ;
	if (t == 'g')
		return 'v' ;
	if (t == 'h')
		return 'x' ;
	if (t == 'i')
		return 'd' ;
	if (t == 'j')
		return 'u' ;
	if (t == 'k')
		return 'i' ;
	if (t == 'l')
		return 'g' ;
	if (t == 'm')
		return 'l' ;
	if (t == 'n')
		return 'b' ;
	if (t == 'o')
		return 'k' ;
	if (t == 'p')
		return 'r' ;
	if (t == 'q')
		return 'z' ;
	if (t == 'r')
		return 't' ;
	if (t == 's')
		return 'n' ;
	if (t == 't')
		return 'w' ;
	if (t == 'u')
		return 'j' ;
	if (t == 'v')
		return 'p' ;
	if (t == 'w')
		return 'f' ;
	if (t == 'x')
		return 'm' ;
	if (t == 'y')
		return 'a' ;
	if (t == 'z')
		return 'q' ;
	return ' ' ;
}

int main() {

	string s ;
	int n ;
	
	cin >> n ;
	getline (cin,s);
	for (int _i = 1 ; _i <= n ; _i++ ) {
		getline (cin,s);
		cout << "Case #" << _i << ": " ;
		for (int i = 0 ; i < s.size() ; i++) {
			cout << replace(s[i]) ;
		}
		cout << endl ;
	}
	
	return 0 ;
}
