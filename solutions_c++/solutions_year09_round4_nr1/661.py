#include <iostream>
#include <sstream>

#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>

using namespace std;

int readInt()
{
	string s;
	getline(cin, s);
	stringstream ss(s);
	int ans = 0;
	ss >> ans;

	return ans;
}

int main(int argc, char* argv[])
{
	int T = readInt();
	for (int test = 1; test <= T; ++test)
	{
		int ans = 0;

		int N = readInt();
		list<string> a;
		for (int i = 0; i < N; ++i)
		{
			string s;
			getline(cin, s);
			a.push_back(s);
		}

		for (int i = 0; i < N; ++i)
		{
			list<string>::iterator it = a.begin();
			for (int j = i; j < N; ++j, ++it)
			{
				std::size_t p = it->find_last_of("1");
				if (p == string::npos || p <= i)
				{
					ans += j - i;
					a.erase(it);
					break;
				}
			}
		}

		cout << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}
