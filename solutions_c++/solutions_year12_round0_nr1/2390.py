#include <iostream>
#include <map>
#include <fstream>
//#include "all.h"
using namespace std;


map<char, char> build_dict(){
	map<char, char> dict;

	string s = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string t = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	for(int i=0; i<s.length(); i++) {
		dict[s[i]] = t[i];
	}
	dict['q'] = 'z';
	dict['z'] = 'q';

	return dict;
}

string translate(string s, map<char, char> dict){
	for(int i=0; i<s.length(); i++)
		s[i] = dict[s[i]];
	return s;
}


int main(){
	string file = "A-small-attempt.in";
	freopen(file.c_str(), "r", stdin);
    int t;
    cin >> t;
    ofstream of;
    of.open("out.txt");

    map<char, char> dict = build_dict();
    string s;
    getline(cin, s);
    for(int i=0; i<t; i++) {
    	getline(cin, s);// cin >> s;
     	of << "Case #"<< i + 1 << ": " << translate(s, dict) << endl;
    }
    of.close();
    return 0;
}
