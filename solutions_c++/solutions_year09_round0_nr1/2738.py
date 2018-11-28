#include <iostream>
#include <string>
#include <vector>

using namespace std;

int l, d, n;
string temp;
vector<string> vocabulary;

struct Word
{
	vector< vector<char> > data;

	Word()
	{
		data.resize(l);
	}
};

Word word;

void Process(string value)
{
	word = Word();
	int counter = 0;

	for (int i = 0; i < value.length(); i++)
	{
		if (value[i] == '(')
		{
			int offset = 1;
			while (value[i + offset] != ')')
				word.data[counter].push_back(value[i + offset++]);
			i += offset;
			counter++;
		}
		else
			word.data[counter++].push_back(value[i]);
	}
}

bool Search(string value)
{
	for (int i = 0; i < d; i++)
	{
		for (int j = 0; j < value.length(); j++)
		{
			if (value[j] != vocabulary[i][j])
				break;

			if (j == value.length() - 1)
				return true;
		}
	}
	return false;
}

int Count(string value, int pos)
{
	int rez = 0;

	if (pos == l)
	{
		if (Search(value))
			return 1;
		return 0;
	}
	else if (pos > 0)
	{
		if (!Search(value))
			return 0;
	}

	for (int i = 0; i < (int)word.data[pos].size(); i++)
		rez += Count(value + word.data[pos][i], pos + 1);

	return rez;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);

	vocabulary.resize(d);
	for (int i = 0; i < d; i++)
		cin >> vocabulary[i];
	
	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		Process(temp);
		int rez = Count("", 0);
		cout << "Case #" << i + 1 << ": " << rez << endl;
	}

	return 0;
}