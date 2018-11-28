/*
 * main.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: greenvirag
 */

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>

using namespace std;

string _CODED = "ejp mysljylc kd kxveddknmc re jsicpdrysi" \
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" \
		"de kr kd eoya kw aej tysr re ujdr lkgc jv";

string _ORIGINAL = "our language is impossible to understand" \
		"there are twenty six factorial possibilities" \
		"so it is okay if you want to just give up";

map<char, char> codes;
map<char, char> decodes;

unsigned int iTestCase = 0;
unsigned int maxTestCase = 0;

ofstream file;

string decode (string input) {
	string decoded = "";

	for (unsigned int i = 0; i < input.size(); i++) {
		char j = input.at(i);
		if (j >= 'a' && j <= 'z') {
			decoded += decodes[j];
		} else if (j >= 'A' && j <= 'Z') {
			char k = j - ('A' - 'a');
			char l = decodes[k];
			decoded += l + ('A' - 'a');
		} else {
			decoded += j;
		}
	}

	return decoded;
}

void print(string result) {
	file << "Case #" << iTestCase << ": " << result << endl;
}

void read() {
	cin >> maxTestCase;
	cin.get();
	string sentence = "";
	for (unsigned int i = 0; i < maxTestCase; i++) {
		iTestCase++;
		getline(cin, sentence);
		print(decode(sentence));
	}
}


int main () {

	for (unsigned int i = 0; i < _CODED.size(); i++) {
		decodes.insert(make_pair(_CODED.at(i), _ORIGINAL.at(i)));
		codes.insert(make_pair(_ORIGINAL.at(i), _CODED.at(i)));
	}

	codes.insert(make_pair('a', 'y'));
	codes.insert(make_pair('o', 'e'));
	codes.insert(make_pair('z', 'q'));

	decodes.insert(make_pair('y', 'a'));
	decodes.insert(make_pair('e', 'o'));
	decodes.insert(make_pair('q', 'z'));

//	cout << decode(_CODED) << endl;

	file.open("result.txt");
	read();
	file.close();

	cout << "OK\n";

	return 0;
}


