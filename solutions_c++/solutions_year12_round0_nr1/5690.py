#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>

using namespace std ; 

map<char,char> m ; 

string solve( string & in ) {
	string res = "" ; 
	
	for ( int i = 0 ; i < in.size() ; i ++ ) {
		res += m[ in[ i ] ] ;
	}	
	
	return res ;
}

int getNum( string & in ) {
	istringstream iss ( in ) ;
	
	int N ; 
	
	iss >> N ; 
	
	return N ;
}

int main() {

	m['a']='y' ;
	m['b']='h' ;
	m['c']='e' ;
	m['d']='s' ;
	m['e']='o' ;
	m['f']='c' ; 
	m['g']='v' ;
	m['h']='x' ; 
	m['i']='d' ;
	m['j']='u' ;
	m['k']='i' ;
	m['l']='g' ;
	m['m']='l' ;
	m['n']='b' ;
	m['o']='k' ;
	m['p']='r' ;
	m['q']='z' ; 
	m['r']='t' ;
	m['s']='n' ;
	m['t']='w' ;
	m['u']='j' ;
	m['v']='p' ;
	m['w']='f' ;
	m['x']='m' ;
	m['y']='a' ;
	m['z']='q' ;
	m[' '] = ' ' ;
	
	string test = "" ; 
	
	getline( cin , test ) ;
	
	int T = getNum( test ) ;
	
	string in = "" ;
	
	for ( int i = 0 ; i < T ; i ++ ) {
		getline( cin , in ) ;
		
		string res = solve( in ) ;
		
		cout << "Case #" << i + 1 <<": " << res << endl ;	
	}
	
	return 0 ;
	
}
