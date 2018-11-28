#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	string s;
	fin >> T;
	for (int n=1; n<=T; ++n)
	{
		fin >> s;
		map<char, int> m;
		string ret;
		for (size_t i=0; i<s.size(); ++i)
		{
			char ss = s[i];
			if (m.count(ss) == 0)
			{
				if (m.empty())
					m[ss] = 1;
				else if (m.size() == 1)
					m[ss] = 0;
				else
					m[ss] = m.size();
			}
		}
		int base = m.size() < 2 ? 2 : m.size();
		unsigned long long result = 0, mult = 1;
		for (size_t i=0; i<s.size(); ++i)
		{
			result += m[s[s.size()-i-1]] * mult;
			mult *= base;
		}

		fout << "Case #" << n << ": " << result << endl;
	}

	return 0;
}

