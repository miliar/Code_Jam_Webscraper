#include <iostream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

bool isHappy(int n, int b)
{
	set<int> mark;

	while (n != 1)
	{
		if (mark.count(n) == 1)
			return false;
		mark.insert(n);

		int newN = 0;
		while (n != 0)
		{
			int d = n % b;
			newN += d * d;
			n /= b;
		}

		n = newN;
	}

	return true;
}

int findHappy(const set<int>& bases)
{
	for (int ans = 2; ans < 2000000000; ++ans)
	{
		bool ok = true;
		for (set<int>::const_iterator it = bases.begin(); it != bases.end(); ++it)
		{
			int b = *it;
			if (!isHappy(ans, b))
			{
				ok = false;
				break;
			}
		}

		if (ok)
			return ans;
	}

	return 0;
}

int main(int argc, char* argv[])
{
	string testS;
	getline(cin, testS);
	stringstream ss(testS);
	int T;
	ss >> T;
	for (int test = 0; test < T; ++test)
	{
		int ans = 0;

		getline(cin, testS);
		stringstream ss(testS);

		set<int> bases;
		do
		{
			int b;
			ss >> b;
			bases.insert(b);
		} while (ss);

		ans = findHappy(bases);

		cout << "Case #" << test + 1<< ": " << ans << endl;
	}

	return 0;
}
