#include <assert.h>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::map;
using std::string;
using std::vector;

vector<string> ParseInput(const string& filename) {
	vector<string> res;

	std::ifstream fin;
	fin.open(filename.c_str(), std::ifstream::in);
	if (fin.fail()) {
		cout << "Failed to open " << filename << endl;
		return res;
	}

	int num_sequences;
	string newline_str;
	fin >> num_sequences;
	std::getline(fin, newline_str);
	for (int i = 0; i < num_sequences; ++i) {
		string line;
		std::getline(fin, line);
		res.push_back(line);
	}

	fin.close();

	return res;
}

// Alternatively, we could load the sample input and generate the mapping programmatically
map<char, char> GetGooglereseMapping() {
	map<char, char> googlerese;
	googlerese.insert(std::make_pair('a','y'));
	googlerese.insert(std::make_pair('b','h'));
	googlerese.insert(std::make_pair('c','e'));
	googlerese.insert(std::make_pair('d','s'));
	googlerese.insert(std::make_pair('e','o'));
	googlerese.insert(std::make_pair('f','c'));
	googlerese.insert(std::make_pair('g','v'));
	googlerese.insert(std::make_pair('h','x'));
	googlerese.insert(std::make_pair('i','d'));
	googlerese.insert(std::make_pair('j','u'));
	googlerese.insert(std::make_pair('k','i'));
	googlerese.insert(std::make_pair('l','g'));
	googlerese.insert(std::make_pair('m','l'));
	googlerese.insert(std::make_pair('n','b'));
	googlerese.insert(std::make_pair('o','k'));
	googlerese.insert(std::make_pair('p','r'));
	googlerese.insert(std::make_pair('q','z'));
	googlerese.insert(std::make_pair('r','t'));
	googlerese.insert(std::make_pair('s','n'));
	googlerese.insert(std::make_pair('t','w'));
	googlerese.insert(std::make_pair('u','j'));
	googlerese.insert(std::make_pair('v','p'));
	googlerese.insert(std::make_pair('w','f'));
	googlerese.insert(std::make_pair('x','m'));
	googlerese.insert(std::make_pair('y','a'));
	googlerese.insert(std::make_pair('z','q'));
	return googlerese;
}

string Translate(const string& input, map<char, char>& googlerese) {
	string res;
	int len = input.length();
	for (int i = 0; i < len; ++i) {
		if (input[i] == ' ')
			res.push_back(input[i]);
		else
			res.push_back(googlerese[input[i]]);
	}
	return res;
}

int main(int argc, char** argv) {

	vector<string> input_lines = ParseInput(string(argv[1]));
	int num_lines = input_lines.size();

	map<char, char> googlerese = GetGooglereseMapping();
	assert(googlerese.size() == 26);

	std::ofstream fout;
	fout.open("output.txt",std::ofstream::out);
	if (fout.fail()) {
		cout << "Failed to open output.txt for writing." << endl;
		return 1;
	}

	for (int i = 0; i < num_lines; ++i) {
		string normal_text = Translate(input_lines[i], googlerese);
		cout << "Case #" << i+1 << ": " << normal_text << endl;
		fout << "Case #" << i+1 << ": " << normal_text << endl;
	}

	fout.close();
	return 0;
}