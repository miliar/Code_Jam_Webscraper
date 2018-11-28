#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

string encrypt(string &s, char *table);

int main(int argc, char *argv[]) {
	const int T_LIMIT = 30; 
	vector<char> possibilities;

	char table[26];
	table['a' - 'a'] = 'y';
	table['b' - 'a'] = 'h';
	table['c' - 'a'] = 'e';
	table['d' - 'a'] = 's';
	table['e' - 'a'] = 'o';
	table['f' - 'a'] = 'c';
	table['g' - 'a'] = 'v';
	table['h' - 'a'] = 'x';
	table['i' - 'a'] = 'd';
	table['j' - 'a'] = 'u';
	table['k' - 'a'] = 'i';
	table['l' - 'a'] = 'g';
	table['m' - 'a'] = 'l';
	table['n' - 'a'] = 'b';
	table['o' - 'a'] = 'k';
	table['p' - 'a'] = 'r';
	table['q' - 'a'] = 'z';
	table['r' - 'a'] = 't';
	table['s' - 'a'] = 'n';
	table['t' - 'a'] = 'w';
	table['u' - 'a'] = 'j';
	table['v' - 'a'] = 'p';
	table['w' - 'a'] = 'f';
	table['x' - 'a'] = 'm';
	table['y' - 'a'] = 'a';
	table['z' - 'a'] = 'q';

	//if (argc == 2) {
		ifstream in;
		ofstream out;

		in.open("D:/input.txt");

		if (!in.is_open()) {
			cout << "Error opening file" << endl;
		}

		string s = "";
		int count = -1;
		int size = 0;
		int sizelimit = 1;
		vector<string> inputs;
		vector<string> outputs;

		while ((getline(in, s))) {
			if (count == -1) {
				size = atoi(s.c_str());
				sizelimit = size;
			}
			else {
				if ((s.length() <= 100) && (count < T_LIMIT)) {
					inputs.push_back(s);
				}
				count--;
			}

			count++;
		}

		for (unsigned int i = 0; i < inputs.size(); i++) {
			string convert = encrypt(inputs[i], table);
			outputs.push_back(convert);
		}

		//Print output
		out.open("D:/output.out", ios::trunc);
		for (unsigned int i = 0; i < outputs.size(); i++) {
			out << "Case #" << i + 1 << ": " << outputs[i] << endl;
		}
		out.close();
	//}

	in.close();

	return 0;
}

string encrypt(string &s, char *table) {
	string es = s;

	for (unsigned int i = 0; i < es.length(); i++) {
		if (es[i] != ' ') {
			es[i] = table[es[i] - 'a'];
		}
	}

	return es;
}