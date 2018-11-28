/*
 * googleres.cpp
 *
 *  Created on: Apr 13, 2012
 *      Author: kazemjahanbakhsh
 */
#include <iostream>
#include <sstream>

using namespace std;

void translate(char *, int);

int main(){
	string input;
	getline (cin, input);

	int cases;

	stringstream ss(input); // Could of course also have done ss("1234") directly.

	ss >> cases;
	//cout << "no of cases: " << cases << endl;
	string *inputs = new string [cases];
	for(int i = 0; i < cases; i++){
		getline (cin, inputs[i]);
	}
	//map was constructed from given sample, figure out q and z by hint!
	char gmap[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	//run the translation
	for(int i = 0; i < cases; i++){
		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < inputs[i].size(); j++) {
			char c = inputs[i][j];
			if (c == ' ') {
				cout << c;
			}
			else {
				cout << gmap[c - 'a'];
			}
		}
		cout << endl;
	}
}

