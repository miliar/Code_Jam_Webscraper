#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
	fstream fin("1.txt", fstream::in);
	fstream fout("1.out.txt", fstream::out);
	int L = 0;
	int D = 0;
	int N = 0;
	fin>>L>>D>>N;

	vector<string> word;
	for (int i = 0; i < D; ++i)
	{
		string w;
		fin>>w;
		word.push_back(w);
	}

	for (int i = 0; i < N; ++i)
	{
		string p;
		fin>>p;
		vector<string> pattern(L, "");
		int k = -1;
		bool sameGroup = false;
		for (int i = 0; i < p.size(); ++i)
		{
			if (p[i] == '(')
			{
				sameGroup = true;
				++k;
			}
			if (p[i] == ')')
			{
				sameGroup = false;
			}

			if(p[i] != '(' && p[i] != ')')
			{
				if(!sameGroup)
				{
					++k;
				}
				pattern[k] += p[i];
			}
		}

		int r = 0;

		for (int i = 0; i < word.size(); ++i)
		{
			int j = 0;
			for (j = 0; j < L; ++j)
			{
				bool found = false;
				for (int m = 0; m < pattern[j].size(); ++m)
				{
					if (word[i][j] == pattern[j][m])
					{
						found = true;
						break;
					}
				}
				if (!found)
				{
					break;
				}
			}
			if (j >= L)
			{
				++r;
			}
		}
		fout<<"Case #"<<i+1<<": "<<r<<endl;
	}
	return 0;
}