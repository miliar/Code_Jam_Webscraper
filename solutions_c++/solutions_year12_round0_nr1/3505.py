#include <iostream>
#include <string>
using namespace std;

char char_map(char c)
{
	string in[4] = {
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jvqey",
		"aozyeq"
	};
	string out[4] = {
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give upzoa",
		"yeqaoz"
	};

	for (int i = 0; i < 4; i++)
	{
		int index = in[i].find(c);
		if (index == string::npos)
			continue;

		return out[i][index];
	}

	return c;
}

int main()
{
	int t, i;

	cin >> t;
	cin.ignore();
	for (int i = 1; i <= t; i++)
	{
		string line;
		getline(cin, line);

		for (int i = 0; i < line.size(); i++)
		{
			line[i] = char_map(line[i]);
		}

		cout << "Case #" << i << ": " << line << endl;
	}

	return 0;
}
