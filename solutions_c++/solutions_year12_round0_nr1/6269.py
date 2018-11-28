#include <iostream>
#include <string>
#include <map>
#include <fstream>

using namespace std ;

map <char,char> mp ;

int main() {

	int t ;
	cin >> t ;
	mp.clear() ;
	mp['a'] = 'y' ;
	mp['b'] = 'h' ;
	mp['c'] = 'e' ;
	mp['d'] = 's' ;
	mp['e'] = 'o' ;
	mp['f'] = 'c' ;
	mp['g'] = 'v' ;
	mp['h'] = 'x' ;
	mp['i'] = 'd' ;
	mp['j'] = 'u' ;
	mp['k'] = 'i' ;
	mp['l'] = 'g' ;
	mp['m'] = 'l' ;
	mp['n'] = 'b' ;
	mp['o'] = 'k' ;
	mp['p'] = 'r' ;
	mp['q'] = 'z' ;
	mp['r'] = 't' ;
	mp['s'] = 'n' ;
	mp['t'] = 'w' ;
	mp['u'] = 'j' ;
	mp['v'] = 'p' ;
	mp['w'] = 'f' ;
	mp['x'] = 'm' ;
	mp['y'] = 'a' ;
	mp['z'] = 'q' ;
	
	ofstream out ( "out.txt" ) ;
	cin.ignore() ;
	for ( int tc = 1 ; tc <= t ; tc ++ ) {
			string line ;
			getline ( cin , line ) ;
			for ( int i = 0 ; i < line.size() ; i ++ )
				if ( line[i] >= 'a' && line[i] <= 'z' )
					line[i] = mp[line[i]] ;
			out << "Case #" << tc << ": " << line << endl ;
	}

	return 0 ;
}