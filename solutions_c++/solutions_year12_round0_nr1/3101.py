#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#include <string>
#include <iostream>
#include <istream>
#include <sstream>

using namespace std;

char map[] = {
				'y',	// a
				'h',	// b
				'e',	// c
				's',	// d
				'o',	// e
				'c',	// f
				'v',	// g
				'x',	// h
				'd',	// i
				'u',	// j
				'i',	// k
				'g',	// l
				'l',	// m
				'b',	// n
				'k',	// o
				'r',	// p
				'z',	// q
				't',	// r
				'n',	// s
				'w',	// t
				'j',	// u
				'p',	// v
				'f',	// w
				'm',	// x
				'a',	// y
				'q'		// z
};

int main() {
	unsigned short T;
	string line;
	getline(cin,line);
	
	T = atoi(line.c_str());
		
	for (unsigned short t = 1; t <= T; t++) {
		getline(cin, line);
		
		cout << "Case #" << t << ": ";
		
		for (unsigned short i = 0; i < line.length(); i++) {
			if (line.c_str()[i] == ' ')	cout << ' ';
			else						cout << map[line.c_str()[i] - 'a'];
		}
		
	 	cout << endl;
	}
	
	return 0;	
}
