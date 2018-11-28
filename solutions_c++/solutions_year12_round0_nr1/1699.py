//
//  main.cpp
//  GCJ2012QA
//
//  Created by Seki Inoue on 12/04/14.
//  Copyright (c) 2012年 UNIPRO Inc. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

char letters_map[26];

void learn() {
	char p[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv azq";
	char a[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up yqz";
	
	for (int i = 0; i < sizeof(p)/sizeof(char); i++) {

		char l = p[i];
		if (l != ' ') {
			letters_map[l-'a'] = a[i];
		}

	}
	
	for (char c = 'a'; c <= 'z'; c++) {
		bool found = false;
		for (int i = 0; i < 26; i++) {
			if (letters_map[i] == c) {
				found = true;
			}
		}
		if (!found) {
			cout << c << " was not found" << endl;
		}
	}
}

void solve() {
	ifstream ifs( "Input.txt" );
    
	
    int T = 0;
    ifs >> T;
    for (int i = 0; i < T+1; i++) {
		string p;
		string a;
		getline(ifs, p);
		bool undetemined = false;
		for (int k = 0; k < p.size(); k++) {
			if (p[k] == ' ') {
				a += ' ';
			}else if (letters_map[p[k]-'a']) {
				a += letters_map[p[k]-'a'];
			}else {
				undetemined = true;
				a += "?";
			}
		}
		if (undetemined) {
			cout << "undetemined :\n"<< p << "->\n" << a << endl;
		}else {
			cout << "Case #" << i << ": " << a << endl;
		}
	}
}

int main(int argc, const char * argv[])
{
	
	memset(letters_map, 0, sizeof(letters_map));
	
	learn();
	
	solve();
	
    return 0;
}

