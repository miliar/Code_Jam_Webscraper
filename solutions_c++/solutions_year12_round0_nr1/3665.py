#include<iostream>
#include<vector>
#include<fstream>
#include<map>
#include<string>

using namespace std;

void decode(const vector<string> & eng, const vector<string> & goog, map<char, char> * dict) {
	
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < eng[i].length(); ++j) {
			(*dict)[goog[i][j]] = eng[i][j];
		}
	}
	for (map<char, char>::iterator it = dict->begin(); it != dict->end(); ++it) {
		cout << it->first << " " << it->second << endl;
	}
	//int a;
	//cin >> a;
	(*dict)['z'] = 'q';
	(*dict)['q'] = 'z';

}

int main() {
	ifstream inp;
	ofstream out;
	inp.open("input.txt");
	out.open("output.txt");
	int t;
	inp >> t;
	vector<string> english;
	vector<string> googleres;
	english.push_back("our language is impossible to understand");
	english.push_back("there are twenty six factorial possibilities");
	english.push_back("so it is okay if you want to just give up");
	googleres.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	googleres.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	googleres.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
	
	map<char, char> dict;
	
	decode(english, googleres, &dict);
	inp.get();
		
	for (int test = 0; test < t; ++test) {
		string res = "";
		char c = inp.get();
		while (c != '\n') {
			res = res + dict[c];
			c = inp.get();
		}
		
		
		out << "Case #" << test + 1 << ": " << res << endl;

	}
	return 0;
}