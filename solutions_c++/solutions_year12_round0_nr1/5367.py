
#include <iostream>
#include <string>
#include <map>
using namespace std;

int test()
{
	map<char, char> mapping;
	string input, output;	
	getline(cin, input);
	getline(cin, output);

	for (int i=0; i<(int)input.size(); i++) {
		mapping[input[i]] = output[i];
	}

	// map<char, char>::iterator iter;
	// for (iter = mapping.begin(); iter != mapping.end(); ++iter) {
	// 	cout << (*iter).first << " -> " << (*iter).second << endl;
	// }

	for (char k='a'; k<='z'; k++) {
		cout << "mapping['" << k << "'] = '" << mapping[k] << "';" << endl;
	}

	return 0;
}

int main()
{
	// test();
	// return 0;

	map<char, char> mapping;
	mapping['a'] = 'y';
	mapping['b'] = 'h';
	mapping['c'] = 'e';
	mapping['d'] = 's';
	mapping['e'] = 'o';
	mapping['f'] = 'c';
	mapping['g'] = 'v';
	mapping['h'] = 'x';
	mapping['i'] = 'd';
	mapping['j'] = 'u';
	mapping['k'] = 'i';
	mapping['l'] = 'g';
	mapping['m'] = 'l';
	mapping['n'] = 'b';
	mapping['o'] = 'k';
	mapping['p'] = 'r';
	mapping['q'] = 'z';
	mapping['r'] = 't';
	mapping['s'] = 'n';
	mapping['t'] = 'w';
	mapping['u'] = 'j';
	mapping['v'] = 'p';
	mapping['w'] = 'f';
	mapping['x'] = 'm';
	mapping['y'] = 'a';
	mapping['z'] = 'q';

	int n = 0, N;
	cin >> N;
	cin.ignore();
	while(n++ < N) {
		string s;
		getline(cin, s);
		cout << "Case #" << n << ": ";
		for (int i=0; i<(int)s.size(); i++) {
			if (mapping.find(s[i]) == mapping.end()) {
				cout << s[i];

			}  else {
				cout << mapping[s[i]];
			}
		}

		cout << endl;
	}

	return 0;
}

