#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <set>

using std::set;
using std::vector;
using std::string;

using std::fstream;
using std::cin;
using std::cout;
using std::istream;
using std::ostream;
using std::pair;

class Pattern
{
public:
	static vector<set<char> > Divide(const string &s)
	{
		vector<pair<int, int> > positions;

		int lastPosition = -1;
		for (int i = 0; i < s.size(); ++i)
		{
			if (lastPosition == -1)
			{
				if (s[i] != '(')
					positions.push_back(pair<int, int>(i, i));
				else
					lastPosition = i;
			}
			else if (s[i] == ')')
			{
				positions.push_back(pair<int, int>(lastPosition + 1, i - 1));
				lastPosition = -1;
			}
		}
		
		
		vector<set<char> > result;

		for (int i = 0; i < positions.size(); ++i)
		{
			set<char> currentSet;

			for (int j = positions[i].first; j <= positions[i].second; ++j)
				currentSet.insert(s[j]);
			
			result.push_back(currentSet);
		}

		return result;
	}
public:
	Pattern() {};
	vector<set<char> > symbols;

	friend istream& operator >> (istream &input, Pattern &pattern)
	{
		string s;
		input >> s;
		pattern.symbols = Pattern::Divide(s);
		return input;
	}

	bool Match(const string &s)
	{
		if (s.size() != symbols.size())
			return false;

		for (int i = 0; i < s.size(); ++i)
			if (symbols[i].find(s[i]) == symbols[i].end())
				return false;

		return true;
	}
};

class Dictionary
{
public:
	vector<string> words;

	int MatchNumber(Pattern &p)
	{
		int result = 0;
		for (int i = 0; i < words.size(); ++i)
			if (p.Match(words[i]))
				++result;
		return result;
	}

	void read(istream &input, int n)
	{
		string s;
		for (int i = 0; i < n; ++i)
		{
			input >> s;
			words.push_back(s);
		}
	}
};

int main()
{
	fstream input("input.txt", std::ios::in);
	fstream output("output.txt", std::ios::out);

	int L, D, N;
	input >> L >> D >> N;

	Dictionary Dic;
	Dic.read(input, D);

	for (int i = 0; i < N; ++i)
	{
		Pattern P;
		input >> P;
		output << "Case #" << (i + 1) << ": " << Dic.MatchNumber(P) << std::endl;
	}
	return 0;
}