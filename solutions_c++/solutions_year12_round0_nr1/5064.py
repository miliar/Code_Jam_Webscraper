#include <iostream>
#include <fstream>
#include <map>
#include <string>
using namespace std ; 

int main (){
	map <char,char > m ; 
	m[' '] = ' ' ;
	m['a'] = 'y' ;
	m['b'] = 'h' ;
	m['c'] = 'e' ;
	m['d'] = 's' ;
	m['e'] = 'o' ;
	m['f'] = 'c' ;
	m['g'] = 'v' ;
	m['h'] = 'x' ;
	m['i'] = 'd' ;
	m['j'] = 'u' ;
	m['k'] = 'i' ;
	m['l'] = 'g' ;
	m['m'] = 'l' ;
	m['n'] = 'b' ;
	m['o'] = 'k' ;
	m['p'] = 'r' ;
	m['r'] = 't' ;
	m['q'] = 'z' ;
	m['s'] = 'n' ;
	m['t'] = 'w' ;
	m['u'] = 'j' ;
	m['v'] = 'p' ;
	m['w'] = 'f' ;
	m['x'] = 'm' ;
	m['y'] = 'a' ;
	m['z'] = 'q' ;

	ifstream in ("t.in") ;
	ofstream out ("t.out") ;
	
	string str ;
	getline(in,str) ;
	int num =1 ;
	while (getline(in,str)  ) {
		for(int i =0 ;i<str.length();i++)
			str[i] = m[str[i]] ;
		out << "Case #" << num << ": "  << str << endl ;
		num++ ;

	}


	return 0 ;
}
