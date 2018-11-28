#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

map<char, char>  GetCode() {
	map<char, char> code;
	code['a'] = 'y';
	code['b'] = 'h';
	code['c'] = 'e';
	code['d'] = 's';
	code['e'] = 'o';
	code['f'] = 'c';
	code['g'] = 'v';
	code['h'] = 'x';
	code['i'] = 'd';
	code['j'] = 'u';
	code['k'] = 'i';
	code['l'] = 'g';
	code['m'] = 'l';
	code['n'] = 'b';
	code['o'] = 'k';
	code['p'] = 'r';
	code['q'] = 'z';
	code['r'] = 't';
	code['s'] = 'n';
	code['t'] = 'w';
	code['u'] = 'j';
	code['v'] = 'p';
	code['w'] = 'f';
	code['x'] = 'm';
	code['y'] = 'a';
	code['z'] = 'q';
	code[' '] = ' ';

	return code;
}

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

template <class AnswerType>
AnswerType SolveTestCase(map<char, char>& code) {
	string str;
	getline(cin, str);
	string res(str.size(), 0);
	for (size_t i = 0; i < str.size(); i++) {
		res[i] = code[str[i]];
	}
	return res;
}

int main()
{
	map<char, char> code = GetCode();
	//freopen("input.txt", "r", stdin);
	freopen("small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;
	string str;
	getline(cin, str);

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<string>(code) );

	return 0;
}