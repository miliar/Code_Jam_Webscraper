#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct group
{
	bool valid[26];

	group()
	{
		for (int i = 0; i < 26; i++)
			valid[i] = false;
	}
};

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int L, D, N;
	cin >> L >> D >> N;

	vector<string> dictionary(D);
	for (int i = 0; i < D; i++)
	{
		cin >> dictionary[i];
	}

	for (int t = 0; t < N; t++)
	{
		vector<group> pattern;

		string regex;
		cin >> regex;

		for (size_t i = 0; i < regex.size(); i++)
		{
			group g;

			if (regex[i] == '(')
			{
				int j = i + 1;
				for (size_t j = i + 1; j < regex.size(); j++)
				{
					if (regex[j] == ')')
					{
						i = j;
						break;
					}
					else
					{
						g.valid[regex[j] - 'a'] = true;
					}
				}
			}
			else
			{
				g.valid[regex[i] - 'a'] = true;
			}
			pattern.push_back(g);
		}

		int result = 0;
		for (int i = 0; i < D; i++)
		{
			bool valid = true;
			for (int j = 0; j < L; j++)
			{
				if (!pattern[j].valid[dictionary[i][j] - 'a'])
				{
					valid = false;
					break;
				}
			}
			if (valid)
				result++;
		}
		cout << "Case #" << t + 1 << ": " << result << endl;
	}
	return 0;
}
