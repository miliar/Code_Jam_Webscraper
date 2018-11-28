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

int Count()
{
	int rez = 0;
	bool tmp;

	for (int i = 0; i < d; i++)
	{
		for (int j = 0; j < l; j++)
		{
			tmp = false;
			for (int u = 0; u < (int)word.data[j].size(); u++)
			{
				if (word.data[j][u] == vocabulary[i][j])
				{
					tmp = true;
					break;
				}
			}
			if (!tmp)
				break;
		}
		if (tmp)
			rez++;
	}
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
		int rez = Count();
		cout << "Case #" << i + 1 << ": " << rez << endl;
	}

	return 0;
}