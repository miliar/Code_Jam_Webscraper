#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

#define sz size()

map<char, char> voc;
void init() {
	string s1, s2;
	s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	s2 = "our language is impossible to understand";
	for(int i = 0; i < s1.sz; i++) {
		voc[s1[i]] = s2[i];
	}

	s1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s2 = "there are twenty six factorial possibilities";
	for(int i = 0; i < s1.sz; i++) {
		voc[s1[i]] = s2[i];
	}

	s1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	s2 = "so it is okay if you want to just give up";
	for(int i = 0; i < s1.sz; i++) {
		voc[s1[i]] = s2[i];
	}
	voc['z'] = 'q';
	voc['q'] = 'z';
}
int main() {
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	init();
	string s;
	int t;
	cin >> t;
	getline(cin, s);
	for(int i = 1; i <= t; i++) {
		getline(cin, s);
		cout << "Case #" << i << ": ";
		for(int i = 0; i < s.sz; i++) {
			cout << voc[s[i]];
		}
		cout << endl;
	}
 	return 0;
}
