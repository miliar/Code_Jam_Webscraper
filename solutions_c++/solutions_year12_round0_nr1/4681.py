#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <cstdlib>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]) {

	map<char, char> lanMap;

	lanMap['z'] = 'q';
	lanMap['q'] = 'z';

	ifstream input("test.in");
	ifstream output("test.out");

	string wordin, wordout;
	
	while (input >> wordin && output >> wordout) {
		for (size_t i = 0; i < wordin.size(); ++i) {
			lanMap[wordin[i]] = wordout[i];
		}
	}
/*
	for (map<char, char>::iterator itr = lanMap.begin();
			itr != lanMap.end(); ++itr) {
		cout << itr->first << " -> " << itr->second << endl;
	}
*/
	input.close();
	output.close();


	/* finish building map */

	ifstream in("A-small-attempt0.in");
	string line, word;
	
	getline(in, line);
	int n = atoi(line.c_str());

	for (int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ":";
		getline(in, line);
		stringstream tokenizer;
		tokenizer << line;
		while (tokenizer >> word) {
			cout << " ";
			for (size_t j = 0; j < word.size(); ++j)
				cout << lanMap[word[j]];
		}
		cout << endl;
	}

	in.close();

	return 0;
}

