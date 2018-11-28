#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <cassert>
#include <iterator>

using namespace std;

string googlerese(map<char, char> langMap, const string& word) {
	string output;
	for (unsigned int i = 0; i < word.length(); i++)
		output.push_back(langMap[word[i]]);

	return output;
}

void loadLangMap(map<char, char>& langMap) {
	langMap['a'] = 'y';
	langMap['b'] = 'h';
	langMap['c'] = 'e';
	langMap['d'] = 's';
	langMap['e'] = 'o';
	langMap['f'] = 'c';
	langMap['g'] = 'v';
	langMap['h'] = 'x';
	langMap['i'] = 'd';
	langMap['j'] = 'u';
	langMap['k'] = 'i';
	langMap['l'] = 'g';
	langMap['m'] = 'l';
	langMap['n'] = 'b';
	langMap['o'] = 'k';
	langMap['p'] = 'r';
	langMap['q'] = 'z';
	langMap['r'] = 't';
	langMap['s'] = 'n';
	langMap['t'] = 'w';
	langMap['u'] = 'j';
	langMap['v'] = 'p';
	langMap['w'] = 'f';
	langMap['x'] = 'm';
	langMap['y'] = 'a';
	langMap['z'] = 'q';
}

int main ()
{
	map<char,char> langMap;
	loadLangMap(langMap);

	int n;
	cin >> n;

	string line;

	getline(cin, line);
	assert(line == "");
	ostringstream os;
	for (int i = 1; i <= n; i++) {
		getline(cin, line);

		istringstream is(line);
		string word;
		string space = "";
		os << "Case #" << i << ": ";
		while (is >> word) {
			os << space << googlerese(langMap, word);
			space = " ";
		}
		os << endl;
	}

	cout << os.str();

	return 0;
}
