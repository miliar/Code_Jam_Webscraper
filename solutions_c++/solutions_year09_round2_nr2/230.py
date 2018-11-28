#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
	int t, cn, i;
	string n;
	multiset<char> tm;

	cin >> t;
	getline(cin, n);

	for (cn = 1; cn <= t; cn++)
	{
		tm.clear();
		getline(cin, n);

		int j = n.length() - 1;

		multiset<char>::iterator it;

		while (j >= 0)
		{
			tm.insert(n[j]);
			for (it = tm.begin(); it != tm.end(); it++)
				if (*it > n[j])
					break;
			if (it != tm.end())
				break;
			j--;
		}

		if (j >= 0)
		{
			n[j] = *it;
			tm.erase(it);
		}

		cout << "Case #" << cn << ": ";

		for (i = 0; i <= j; i++)
			cout << n[i];

		if (j < 0)
		{
			it = tm.begin();
			while (*it == '0')
				it++;
			cout << *it << '0';
			tm.erase(it);
		}

		for (it = tm.begin(); it != tm.end(); it++)
			cout << *it;
		cout << endl;
	}

	return 0;
}
