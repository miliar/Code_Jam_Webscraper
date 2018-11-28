#include <set>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <boost/unordered_map.hpp>

using namespace std;
typedef boost::unordered_map<string, bool> TABLE;

inline void cycle_shift(string& s)
{
	if (s.length() > 1)
	{
		s.append(1, s[0]);
		s.erase(0, 1);
	}
}

int main()
{
	size_t T = 0;
	cin >> T;

	const size_t COUNT = 2000000;
	vector<string> numbers(COUNT + 1);
	TABLE table;

	// init numbers cache
	for (size_t i = 1; i <= COUNT; ++i)
	{
		stringstream ss;
		ss << i;
		numbers[i] = ss.str();
		table[numbers[i]] = false;
	}

	for (size_t t = 0; t < T; ++t)
	{
		size_t A = 0, B = 0;
		cin >> A >> B;

		// mark valid range
		for (size_t i = A; i <= B; ++i)
			table[numbers[i]] = true;

		size_t pairs = 0;
		for (size_t i = A; i <= B; ++i)
		{
			if (!table[numbers[i]])
				continue;

			table[numbers[i]] = false; // mark as analysed

			string m = numbers[i];
			set<string> unique_pairs;
			for (size_t k = 1; k < m.length(); ++k)
			{
				cycle_shift(m);
				TABLE::iterator mit = table.find(m);
				if (mit != table.end() && mit->second)
					unique_pairs.insert(m);
			}
			pairs += unique_pairs.size();
		}

		cout << "Case #" << t + 1 << ": " << pairs << endl;

		// unmark valid range
		for (size_t i = A; i <= B; ++i)
			table[numbers[i]] = false;
	}

	return 0;
}