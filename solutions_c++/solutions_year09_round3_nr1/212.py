#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <ctype.h>

using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

const int val[20] = {1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19};

int main()
{
	int used[64], cat[64], cnt;
	string text;
	int t, test, i;
	long long aux, sol;

	fin >> t;

	for(test = 1; test <= t; ++test)
	{
		fin >> text;
		int sz = text.size();
		cnt = 0;
		memset(cat, 0, sizeof(cat));
		memset(used, 0, sizeof(used));
		for(i = 0; i < sz; ++i)
		{
			if(isdigit(text[i]))
			{
				if(!used[text[i] - '0'])
				{
					++cnt;
					used[text[i] - '0'] = 1;
					cat[text[i] - '0'] = val[cnt - 1];
				}
			}
			else
			{
				if(!used[text[i] - 'a' + 10])
				{
					++cnt;
					used[text[i] - 'a' + 10] = 1;
					cat[text[i] - 'a' + 10] = val[cnt - 1];
				}
			}
		}
		if(cnt == 1)
		{
			cnt = 2;
		}
		long long aux = 1;
		sol = 0;
		for(i = sz - 1; i >= 0; --i)
		{
			/*
			if(isdigit(text[i]))
			{
				fout << "-" << cat[text[i] - '0'] << "-" << endl;
			}
			else
			{
				fout << "-" << cat[text[i] - 'a' + 10] << "-" << endl;
			}
			*/
			if(isdigit(text[i]))
			{
				sol += (long long)aux * (long long)cat[text[i] - '0'];
			}
			else
			{
				sol += (long long)aux * (long long)cat[text[i] - 'a' + 10];
			}
			//fout << aux << " " << sol << endl;
			aux = (long long) aux * (long long) cnt;
		}
		fout << "Case #" << test << ": " << sol << endl;
	}



	return 0;
}
