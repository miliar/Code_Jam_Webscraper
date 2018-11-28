// 2012_Q_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <set>
#include <string>
#include <map>
#include <fstream>
#include <iostream>

using namespace std;

typedef map< char, char> CHMAP;
CHMAP chmap;
set<char> norset;


char *gg = "ejp mysljylc kd kxveddknmc re jsicpdrysi" \
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" \
"de kr kd eoya kw aej tysr re ujdr lkgc jv";

char *nor = "our language is impossible to understand" \
"there are twenty six factorial possibilities" \
"so it is okay if you want to just give up";

int _tmain(int argc, _TCHAR* argv[]) {
	chmap['q'] = 'z';
	chmap[' '] = ' ';
	norset.insert('z');
	norset.insert(' ');
	size_t len = strlen(gg);
	for (size_t i = 0; i < len; ++i) {
		chmap[gg[i]] = nor[i];
		norset.insert(nor[i]);
	}
	char ggmis = 0;
	char normis = 0;
	for (char i = 'a' ; i <= 'z'; ++i) {
		if (chmap.find(i) == chmap.end()) {
			ggmis = i;
		}
		if (norset.find(i) == norset.end()) {
			normis = i;
		}
	}
	chmap[ggmis] = normis;
	

	// Solve
	size_t T = 0;
	cin >> T;
	string line;
	for (size_t i = 0; i < T; ++i) {
		do {
		getline(cin, line);
		} while(line.empty());
		cout << "Case #" << i+1 << ": ";
		for(string::iterator itr = line.begin(); itr != line.end(); ++itr) {
			std::cout << chmap.find(*itr)->second;
		}
		cout << endl;
	}

	return 0;
}

