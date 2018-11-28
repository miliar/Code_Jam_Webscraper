#include <fstream>
#include <iostream>
#include <string>
#include <map>
using namespace std;

ifstream fin("1.in");
#define cin fin

ofstream fout("1_omar.out");
#define cout fout

int main() {
	int number_of_cases, size;
	cin >> number_of_cases;

	map<char, char> translator;
	translator['a'] = 'y';
	translator['b'] = 'h';
	translator['c'] = 'e';
	translator['d'] = 's';
	translator['e'] = 'o';
	translator['f'] = 'c';
	translator['g'] = 'v';
	translator['h'] = 'x';
	translator['i'] = 'd';
	translator['j'] = 'u';
	translator['k'] = 'i';
	translator['l'] = 'g';
	translator['m'] = 'l';
	translator['n'] = 'b';
	translator['o'] = 'k';
	translator['p'] = 'r';
	translator['q'] = 'z';
	translator['r'] = 't';
	translator['s'] = 'n';
	translator['t'] = 'w';
	translator['u'] = 'j';
	translator['v'] = 'p';
	translator['w'] = 'f';
	translator['x'] = 'm';
	translator['y'] = 'a';
	translator['z'] = 'q';

	string input_line = "                                                                                                      ";
	cin.ignore();

	for (int kase = 1; kase <= number_of_cases; ++kase) {
		cout << "Case #" << kase << ": ";
		getline(cin, input_line);
		size = input_line.size();
		while (size--)
			if (translator.find(input_line[size]) != translator.end())
				input_line[size] = translator[input_line[size]];

		cout << input_line << endl;
	}

	return 0;
}
