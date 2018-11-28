
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std ;

char Change (const char &string)
{
	switch (string) {
	case 'a':
		return 'y' ;
	case 'b' :
		return 'h' ;
	case 'c' :
		return 'e' ;
	case 'd' :
		return 's' ;
	case 'e' :
		return 'o' ;
	case 'f' :
		return 'c' ;
	case 'g' :
		return 'v' ;
	case 'h' :
		return 'x' ;
	case 'i' :
		return 'd' ;
	case 'j' :
		return 'u' ;
	case 'k' :
		return 'i' ;
	case 'l' :
		return 'g' ;
	case 'm' :
		return 'l' ;
	case 'n' :
		return 'b' ;
	case 'o' :
		return 'k' ;
	case 'p' :
		return 'r' ;
	case 'q' :
		return 'z' ;
	case 'r' :
		return 't' ;
	case 's' :
		return 'n' ;
	case 't' :
		return 'w' ;
	case 'u' :
		return 'j' ;
	case 'v' :
		return 'p' ;
	case 'w' :
		return 'f' ;
	case 'x' :
		return 'm' ;
	case 'y' :
		return 'a' ;
	case 'z' :
		return 'q' ;
	default :
		return ' ' ;
	}
}
int main ()
{
	ifstream inSt ("A-small-attempt3.in") ;
	try {
		if (inSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Input file opeing failed." << endl ;
		exit (1) ;
	}
	ofstream outSt ("output.txt") ;
	try {
		if (outSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Output file opeing failed." << endl ;
		exit (1) ;
	}

	int numT ;
	inSt >> numT ;
	inSt.ignore (1, '\n') ;
	char string[101] ;
	for (int i =1, j =0 ; i <= numT ; i++) {
		
		inSt.getline (string, 101) ;

		outSt << "Case #" << i << ": " ;
		while (string[j] != NULL) {
			outSt << Change (string[j++]) ;
		}
		j =0 ;
		outSt << endl ; 
	}
	outSt.close () ;
	return 0 ;
}