#include <iostream>
#include <string>
#include <fstream>
#include <map>
using namespace std;


int main() {

	map<char, char> ciphermap;
	map<char, char>::iterator it;
	ciphermap['y'] = 'a';
	ciphermap['n'] = 'b';
	ciphermap['f'] = 'c';
	ciphermap['i'] = 'd';
	ciphermap['c'] = 'e';
	ciphermap['w'] = 'f';
	ciphermap['l'] = 'g';
	ciphermap['b'] = 'h';
	ciphermap['k'] = 'i';
	ciphermap['u'] = 'j';
	ciphermap['o'] = 'k';
	ciphermap['m'] = 'l';
	ciphermap['x'] = 'm';
	ciphermap['s'] = 'n';
	ciphermap['e'] = 'o';
	ciphermap['v'] = 'p';
	ciphermap['z'] = 'q';
	ciphermap['p'] = 'r';
	ciphermap['d'] = 's';
	ciphermap['r'] = 't';
	ciphermap['j'] = 'u';
	ciphermap['g'] = 'v';
	ciphermap['t'] = 'w';
	ciphermap['h'] = 'x';
	ciphermap['a'] = 'y';
	ciphermap['q'] = 'z';

	string readstring;
	
	ifstream fin;
	
	fin.open("input.txt");
	
	int numcases;
	fin >> dec >> numcases;
	fin >> ws;
//	fscanf(&fin,"%d\n", &numcases);
	
//	cout << numcases << endl;
	
	int readcases = numcases;
	while(readcases > 0) {
		getline(fin, readstring);
		
		cout << "Case #" << numcases - readcases + 1 << ": ";
		
		for(int i = 0; i < readstring.size(); i++) {
			cout << ciphermap.find(readstring[i])->second;
		}
		cout << endl;
		
		readcases--;
	}

	return 0;
}
