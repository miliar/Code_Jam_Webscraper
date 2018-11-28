#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>

using namespace std;

bool match(const string& word, const vector<set<char> >& pattern)
{
	for (int i = 0; i < word.length(); ++i)
		if (pattern[i].count(word[i]) == 0)
			return false;

	return true;
}

int main(int argc, char* argv[])
{
	int L = 0;
	int D = 0;
	int N = 0;

	string firstLine;
	getline(cin, firstLine);
	stringstream ss(firstLine);
	ss >> L >> D >> N;

	vector<string> words(D);
	for (int i = 0; i < D; ++i)
		getline(cin, words[i]);

	for (int test = 1; test <= N; ++test)
	{
		int matches = 0;

		vector<set<char> > pattern(L);
		string patternStr;
		getline(cin, patternStr);

		int curToken = 0;
		int curPos = 0;
		bool isGroup = false;

		while (curPos < patternStr.length())
		{
			char curChar = patternStr[curPos];
			if (curChar == '(')
				isGroup = true;
			else if (curChar == ')')
			{
				isGroup = false;
				++curToken;
			}
			else
			{
				pattern[curToken].insert(curChar);
				if (!isGroup)
					++curToken;
			}

			++curPos;
		}

		for (int i = 0; i < D; ++i)
			if (match(words[i], pattern))
				++matches;

		cout << "Case #" << test << ": " << matches << endl;
	}

	return 0;
}
