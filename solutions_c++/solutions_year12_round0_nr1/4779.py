#include <iostream>
#include <string>

using namespace std;

int main()
{
	int i, j, l, t;
	string s, ss;
	char c;
	
	cin >> t;
	getline(cin, s);
	for ( i = 0; i < t; i++ ) {
		getline(cin, s);
		l = s.length();
		ss = "";
		cout << "Case #"<< i+1 <<": ";
		for ( j = 0; j < l; j++ ) {
			c = s[j];
			if ( c == ' ' )
				ss +=  ' ';
			else if ( c == 'a' )
				ss += 'y';
			else if ( c == 'b' )
				ss += 'h';
			else if ( c == 'c' )
				ss += 'e';
			else if ( c == 'd' )
				ss += 's';
			else if ( c == 'e' )
				ss += 'o';
			else if ( c == 'f' )
				ss += 'c';
			else if ( c == 'g' )
				ss += 'v';
			else if ( c == 'h' )
				ss += 'x';
			else if ( c == 'i' )
				ss += 'd';
			else if ( c == 'j' )
				ss += 'u';
			else if ( c == 'k' )
				ss += 'i';
			else if ( c == 'l' )
				ss += 'g';
			else if ( c == 'm' )
				ss += 'l';
			else if ( c == 'n' )
				ss += 'b';
			else if ( c == 'o' )
				ss += 'k';
			else if ( c == 'p' )
				ss += 'r';
			else if ( c == 'q' )
				ss += 'z';    
			else if ( c == 'r' )
				ss += 't';
			else if ( c == 's' )
				ss += 'n';
			else if ( c == 't' )
				ss += 'w';
			else if ( c == 'u' )
				ss += 'j';
			else if ( c == 'v' )
				ss += 'p';
			else if ( c == 'w' )
				ss += 'f';
			else if ( c == 'x' )
				ss += 'm';
			else if ( c == 'y' )
				ss += 'a';
			else if ( c == 'z' )
				ss += 'q';
		}
		cout << ss << endl;
	}
	return 0;
}	
