#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

ifstream fin("input");
ofstream fout("output");

int main()
{
	int l, d, n, i, j, test, crt, used[16][32], sol; //lvl si litera
	string word;
	vector<string> dictionary;

	fin >> l >> d >> n;

	for(i = 0; i < d; ++i)
	{
		fin >> word;
		dictionary.push_back(word);
	}

	for(test = 1; test <= n; ++test)
	{
		fin >> word;
		int pos = 0, sz = word.length();
		memset(used, 0, sizeof(used));
		crt = 0;
		while(pos < sz)
		{
			if(word[pos] == '(')
			{
				++pos;
				while(word[pos] != ')')
				{
					used[crt][word[pos] - 'a'] = 1;
					++pos;
				}
			}
			else
			{
				used[crt][word[pos] - 'a'] = 1;
			}
			++pos;
			++crt;
		}
		sol = 0;
		for(i = 0; i < d; ++i)
		{
			for(j = 0; j < l && used[j][dictionary[i][j] - 'a']; ++j);
			sol += (j == l);
		}
		fout << "Case #" << test << ": " << sol << endl;
	}



	return 0;
}
