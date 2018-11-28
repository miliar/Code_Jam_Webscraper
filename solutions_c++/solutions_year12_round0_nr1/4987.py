#include <iostream>
#include <string>
#include <algorithm>
#define F(a, b) for (int a = 0; a < b; a++)

using std::begin;
using std::end;
using std::cin;
using std::cout;
using std::endl;
using std::getline;
using std::string;

const char *map = "yhesocvxduiglbkrztnwjpfmaq";

int main(int argc, char* argv[])
{
	int cases = 0;
	string line;
	cin >> cases;
	cin.ignore(1);

	F(i, cases){
		getline(cin, line);
		std::transform(begin(line), end(line), begin(line), [](char c) -> char { if (c == 32) return c; else return map[c-'a']; });
		cout << "Case #" << i+1 << ": " << line << endl;
	}
}
