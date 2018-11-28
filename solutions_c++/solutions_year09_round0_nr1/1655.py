#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned int		LetterSet;
typedef vector<LetterSet>	Word;
typedef vector<Word>		Dictionary;

void read_word(Word &w)
{
	char in[1024];
	cin.getline(in, 1024);

	stringstream ss(in);

	w.clear();

	char c;
	while (ss >> c)
	{
		LetterSet tmp = 0;
		if (c == '(')
		{
			while (ss >> c, c != ')')
			{
				tmp |= 1 << (c - 'a');
			}
		}
		else 
		{
			tmp |= 1 << (c - 'a');
		}
		w.push_back(tmp);
	}
}
void write_word(Word &w)
{
	for (int i = 0; i < (int)w.size(); ++i)
	{
		cout << '(';
		for (int j = 0; j < 'z' - 'a'; ++j)
		{
			if ((w[i] >> j) & 1)
			{
				cout << (char)('a' + j);
			}
		}
		cout << ')';
	}
	cout << endl;	
}
bool match(Word &l, Word &r)
{
	for (int i = 0; i < (int)l.size(); ++i)
	{
		if ((l[i] & r[i]) == 0)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int l, d, n;
	Dictionary dict;

	cin >> l >> d >> n >> ws;

	dict.resize(d);
	for (int i = 0; i < d; ++i)
	{
		read_word(dict[i]);
	}

	for (int i = 0; i < n; ++i)
	{
		Word in;
		read_word(in);
	
		int count = 0;

		for (int j = 0; j < d; ++j)
		{
			if (match(in, dict[j]))
			{
				++count;
			}
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}

	return 0;
}