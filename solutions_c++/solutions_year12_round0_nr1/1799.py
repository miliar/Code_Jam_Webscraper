#include <map>
#include <set>
#include <iostream>
#include <fstream>
#include <string>
#include <cassert>

using namespace std;

const size_t KnownCount = 3;

const char* KnownInputs[] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

const char* KnownOutputs[] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"
};

int main(int argc, char *argv[]) {
	map<char, char> mapping;
	mapping['q'] = 'z';
	mapping['z'] = 'q';

	for (size_t i = 0; i < KnownCount; ++i) {
		assert(strlen(KnownInputs[i]) == strlen(KnownOutputs[i]));
		for (size_t j = 0; j < strlen(KnownInputs[i]); ++j) {
			mapping[KnownInputs[i][j]] = KnownOutputs[i][j];
		}
	}

	for (char c = 'a'; c <= 'z'; ++c)
		assert(mapping.find(c) != mapping.end());

	ifstream input("input.txt");
	ofstream output("output.txt");

	size_t cases;
	input >> cases >> ws;
	for (size_t i = 1; i <= cases; ++i) {
		string line;
		getline(input, line);
		output << "Case #" << i << ": ";
		for (size_t j = 0; j < line.length(); ++j)
			output << mapping[line[j]];
		output << endl;
	}
}