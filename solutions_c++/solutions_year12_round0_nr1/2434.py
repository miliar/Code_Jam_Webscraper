/*
 *  SpeakingInTongues.cpp
 *  GoogleCodeJamPractice
 *
 *  Created by Elina Robeva on 4/14/12.
 *  Copyright 2012 Stanford University. All rights reserved.
 *
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;


int main() {
	freopen("/Users/erobeva/Downloads/A-small-attempt0 (2).in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOut.txt", "w", stdout);
	
	int a[26];
	
	for(int i = 0; i < 26; ++i){
		a[i] = -1;
	}

	a['y' - 'a'] = 'a'-'a';
	a['e' - 'a'] = 'o' - 'a';
	a['q' - 'a'] = 'z' - 'a';
	
	string str[3];
	string str_real[3];
	str[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	str_real[0] = "our language is impossible to understand";
	str[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	str_real[1] = "there are twenty six factorial possibilities";
	str[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	str_real[2] = "so it is okay if you want to just give up";
	
	for(int i = 0; i < 3; ++i) {
		for(int j = 0; j < str[i].length(); ++j) {
			if(str[i].at(j) != ' '){
				a[str[i].at(j) - 'a'] = str_real[i].at(j) - 'a';
			}
		}
	}
	
	int used[26];
	for(int i = 0; i < 26; ++i) {
		used[i] = 0;
	}
	for(int i = 0; i < 26; ++i){
		used[a[i]] = 1;
	}
	int rem = 0;
	for(int i = 0; i < 26; ++i) {
		if(used[i] == 0){
			rem = i;
		}
	}
	for(int i = 0; i < 26; ++i){
		if(a[i] == -1){
			a[i] = rem;
		}
//		cout << a[i] << " ";
	}
	
	int T;
	cin >> T;
	string dummy;
	getline(cin, dummy);
	for(int i = 0; i < T; ++i) {
		string exp;
		getline(cin, exp);
		//cout << exp << endl;
		//cin >> exp;
		cout << "Case #" << i+1 << ": ";
		for(int j = 0; j < exp.length(); ++j) {
			if (exp.at(j) == ' '){
				cout << " ";
			} else {
				cout << char('a' + a[exp.at(j) - 'a']);
			}
		}
		cout << endl;
	}

}
