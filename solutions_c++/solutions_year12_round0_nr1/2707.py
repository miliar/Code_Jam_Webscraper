#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream in = ifstream("test.txt");
	ofstream out = ofstream("answer.txt");
	int T;
	in >> T;
	string s;
	string cipher = "ynficwlbkuomxsevzpdrjgthaq";
	for (int i = 0; i < cipher.size(); ++i)
		for (int j = i + 1; j < cipher.size(); ++j) 
			if (cipher[i] == cipher[j])
				cout << "WA!" << endl;
	getline(in, s);
	for (int i = 1; i <= T; ++i) {
		getline(in, s);
		string ans(s.size(), ' ');
		for (int j = 0; j < s.size(); ++j)
			if (s[j] != ' ')
				ans[j] = 'a' + cipher.find(s[j]);
		out << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}