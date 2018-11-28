#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int MaxN = 105;

int N;

int main()
{
	int Ncase;
	freopen("0.b_large.in", "r", stdin);
	freopen("0.b_large.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		int Ncomb, Nconf, N;
		string seq;
		int combine[26][26], conflict[26][26];
		memset(combine, -1, sizeof combine);
		memset(conflict, 0, sizeof conflict);
		cin >> Ncomb;
		for (int i = 0; i < Ncomb; ++i)
		{
			string comb;
			cin >> comb;
			combine[comb[0]-'A'][comb[1]-'A'] = combine[comb[1]-'A'][comb[0]-'A'] = comb[2]-'A';
		}
		cin >> Nconf;
		for (int i = 0; i < Nconf; ++i)
		{
			string conf;
			cin >> conf;
			conflict[conf[0]-'A'][conf[1]-'A'] = conflict[conf[1]-'A'][conf[0]-'A'] = 1;
		}
		cin >> N;
		cin >> seq;

		vector<char> result;
		result.clear();
		result.push_back(seq[0]);
		for (int i = 1; i < N; ++i)
		{
			result.push_back(seq[i]);
			while (result.size() > 1)
				if (combine[result[result.size()-2]-'A'][result[result.size()-1]-'A'] != -1)
				{
					char tmp = combine[result[result.size()-2]-'A'][result[result.size()-1]-'A'] + 'A';
					result.pop_back();
					result.pop_back();
					result.push_back(tmp);
				}
				else break;

			for (int j = 0; j < result.size(); ++j)
				for (int k = j+1; k < result.size(); ++k)
					if (conflict[result[j]-'A'][result[k]-'A'])
					{
						result.clear();
						break;
					}
		}

		cout << "Case #" << run+1 << ": [";
		for (int i = 0; i < result.size(); ++i)
		{
			if (i > 0) cout << ", ";
			cout << result[i];
		}
		cout << "]" << endl;
	}
}
