#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
int main() {
	string abc = "abcdefghijklmnopqrstuvwxyz";
	string key = "yhesocvxduiglbkrztnwjpfmaq";
	string yhe = "ynficwlbkuomxsevzpdrjgthaq";
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int K;
	cin >> K;
	getline(cin, abc);
	for (int dataset = 1; dataset <= K; dataset++) {
		cout << "Case #" << dataset << ": ";
		string s;
		getline(cin, s);
		for (int i = 0; s[i] != 0; i++) {
			if (s[i] != ' ')
				cout << key[s[i]-'a'];
			else
				cout << ' ';
		}
		cout << endl;
	}
}
