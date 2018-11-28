#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	int L, D, N;
	cin >> L >> D >> N;
	ofstream dict("dictionary.txt");
	ofstream sed("sedfile");

	string str;
	getline(cin, str);
	for (int i = 0; i < D; i++) {
		getline(cin, str);
		dict << str << endl;
	}

	for (int i = 0; i < N; i++) {
		getline(cin, str);
		string s;
		for (int j = 0; j < str.size(); j++) {
			s += str[j];
			if (str[j] == '(') {
				j++;
				s += str[j];
				j++;
				while (str[j] != ')') {
					s += '|';
					s += str[j];
					j++;
				}
				s += str[j];
			}
		}
		sed << "echo \"Case #" << i+1 << ":\" `grep -E \"" << s << "\" dictionary.txt | wc -l`" << endl;
	}
	return 0;
}

