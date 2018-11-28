#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int l, d, n;
	cin >> l >> d >> n;
	cin.get();

	vector<string> words(d);
	vector<bool> fl(d);

	for (int i = 0; i < d; ++i)
	{
		getline(cin, words[i]);
	}

	string str;

	for (int i = 0; i < n; ++i)
	{
		fill(fl.begin(), fl.end(), true);

		getline(cin, str);
		string::size_type len = str.length();

		string::size_type j = 0;
		int curPos = 0;
		int matchCount = d;

		while (j < len)
		{
			if (str[j] == '(')
			{
				string::size_type last = str.find(')', j + 1);
				string &pattern = str.substr(j + 1, last - j - 1);

				for (int k = 0; k < d; ++k)
				{
					if (fl[k] && pattern.find(words[k][curPos]) == string::npos)
					{
						fl[k] = false;
						--matchCount;
					}
				}

				j = last + 1;
			}
			else
			{
				for (int k = 0; k < d; ++k)
				{
					if (fl[k] && words[k][curPos] != str[j])
					{
						fl[k] = false;
						--matchCount;
					}
				}

				++j;
			}

			++curPos;
		}

		cout << "Case #" << i + 1 << ": " << matchCount << endl;
	}

	return 0;
}