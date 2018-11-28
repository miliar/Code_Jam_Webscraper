#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testn;
	cin >> testn;
	cin.get();

	string str;

	for (int testi = 0; testi < testn; ++testi)
	{
		getline(cin, str);
		str = "0000000000" + str;

		assert(next_permutation(str.begin(), str.end()));

		string::size_type len = str.length();

		cout << "Case #" << testi + 1 << ": ";

		for (string::size_type i = str.find_first_not_of('0'); i < len; ++i)
		{
			cout << str[i];
		}

		cout << endl;
	}

	return 0;
}