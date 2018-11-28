#include "glooglerese.h"
#include <iostream>
#include <tr1/unordered_map>
using namespace std;
using namespace std::tr1;

Glooglerese::Glooglerese()
{
}

int main() {

	const char EOL = '\n';
	char car;
	char car_in_english;
	int T;

	// Create our map, The key will be an integer value and each key will hold a string value
	typedef unordered_map<char, char> Dictionnary;
	Dictionnary myDic;

	// Initialize the Dictionnary : Googlerese <-> English
	myDic['a']='y';
	myDic['b']='h';
	myDic['c']='e';
	myDic['d']='s';
	myDic['e']='o';
	myDic['f']='c';
	myDic['g']='v';
	myDic['h']='x';
	myDic['i']='d';
	myDic['j']='u';
	myDic['k']='i';
	myDic['l']='g';
	myDic['m']='l';
	myDic['n']='b';
	myDic['o']='k';
	myDic['p']='r';
	myDic['q']='z';
	myDic['r']='t';
	myDic['s']='n';
	myDic['t']='w';
	myDic['u']='j';
	myDic['v']='p';
	myDic['w']='f';
	myDic['x']='m';
	myDic['y']='a';
	myDic['z']='q';
	myDic[' ']=' ';


	// Number of test cases
	cin >> T;
	cin.get(car); // + EOL

	// Lecture
	for (int t = 0; t < T; t++) {
		cin.get(car);
		cout << "Case #" << t+1 << ": ";
		// Stops when it reaches end-of-line character or end-of-file
		while(!cin.fail() && car!=EOL ) {
			car_in_english = myDic[car];
			cout << car_in_english;
			cin.get(car);
		}
		cout << endl;
	}


	return 0;
}
