#include <iostream>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main ()
{
	int L, D, N;
	cin >> L >> D >> N;
	vector<string> known;
	string tmpS;
	for (int i=0;i<D;++i)
	{
		cin >> tmpS;
		known.push_back(tmpS);
	}
	for (int i=0;i<N;++i)
	{
		vector<set<char> > pattern;
		string pat, tok;
		// Read pattern
		cin >> pat;
		for (int j=0; j<pat.length(); ++j)
		{
			if (pat[j] == '(')
			// Read token
			{
				int k;
				for (k=j; pat[k] != ')';++k);
				set<char> chars;
				for (int m=j+1; m<=k-1; ++m)
				{
					chars.insert(pat[m]);
				}
				pattern.push_back(chars);
				j = k; // Move the pointer to the end of the group
			}
			else
			{
				// Read single character
				set<char> onechar;
				onechar.insert(pat[j]);
				pattern.push_back(onechar);
			}
		}

		int matches = 0;
		for (int j=0; j<known.size(); ++j)
		{
			int charMatches = 0;
			for (int n=0; n < L; ++n)
			{
				if (pattern[n].count(known[j][n]) > 0)
					charMatches++;
			}
			if (charMatches == L)
				matches++;
		}
		cout << "Case #" << i + 1 << ": " << matches << endl;
	}
	return 0;
}

