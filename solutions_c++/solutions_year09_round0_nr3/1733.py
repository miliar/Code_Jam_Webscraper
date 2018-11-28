#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;


const char pattern[] = "welcome to code jam";
string str;
string::size_type len;


unsigned long long FindCount(string::size_type pos, int index)
{
	if (index == sizeof(pattern)/sizeof(pattern[0]) - 1)
	{
		return 1;
	}

	unsigned long long res = 0;

	for (string::size_type i = pos; i < len; ++i)
	{
		if (str[i] == pattern[index])
		{
			res = (res + FindCount(i + 1, index + 1)) % 1000000000000000;
		}
	}

	return res;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testn;
	cin >> testn;
	cin.get();

	for (int testi = 0; testi < testn; ++testi)
	{
		getline(cin, str);
		len = str.length();

		unsigned long long res = 0;

		for (string::size_type i = 0; i < len; ++i)
		{
			if (str[i] == pattern[0])
			{
				res = (res + FindCount(i + 1, 1)) % 1000000000000000;
			}
		}

		cout << "Case #" << testi + 1 << ": ";

		cout.fill('0');
		cout.width(4);
		cout << res % 10000 << endl;
	}

	return 0;
}