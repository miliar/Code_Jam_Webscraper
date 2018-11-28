#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <string>
using namespace std;

const int MAX_T = 30;
const int MAX_C = 255;

string lines[MAX_T];
vector<string> words;

char cmap[MAX_C];

string mapped(string s) {
	for (int i = 0; i < s.size(); i ++) 
		s[i] = cmap[s[i]];
	return s;
}

int main() {
	int T;
	cin >> T;
	getline(cin, lines[0]);
	for (int i = 0; i < T; i ++) {
		getline(cin, lines[i]);
		istringstream iss(lines[i]);
		copy(istream_iterator<string>(iss), 
				istream_iterator<string>(),
				back_inserter<vector<string> >(words));
	}

	memset(cmap, '$', sizeof(cmap));

	string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

	for (int i = 0; i < a.size(); i ++)
		cmap[a[i]] = b[i];
	cmap['q'] = 'z';
	cmap['z'] = 'q';
	for (int i = 0; i < T; i ++) {
		cout << "Case #" << i + 1 << ": " << mapped(lines[i]) << endl;
	}
}


