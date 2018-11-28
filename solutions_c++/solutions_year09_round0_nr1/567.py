#include <iostream>
#include <set>
#include <string>

using namespace std;
string dict[10000];

int main()
{
	int L, D, N;
	cin >> L >> D >> N;
	for(int i = 0; i < D; i++)
	{
		cin >> dict[i];
	}
	for(int i = 1; i <= N; i++)
	{
		string pat;
		cin >> pat;
		bool fAdd = false;
		set<char> pattern[20];
		for(int j = 0, k = 0; j < pat.size(); j++)
		{
			if(pat[j] == '(')
				fAdd = true;
			else if(pat[j] == ')')
				fAdd = false;
			else
				pattern[k].insert(pat[j]);
			if(!fAdd)
			{
				k++;
			}
		}
		int ret = 0;
		for(int j = 0; j < D; j++)
		{
			bool found = true;
			for(int k = 0; k < dict[j].size(); k++)
			{
				if(pattern[k].count(dict[j][k]) == 0)
				{
					found = false;
					break;
				}
			}
			ret += found;
		}
		cout << "Case #" << i << ": " << ret << endl;

	}
	return 0;
}
