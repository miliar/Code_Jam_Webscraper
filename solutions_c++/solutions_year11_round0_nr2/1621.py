#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <map>
#include <vector>

using namespace std;

#define TEST 
#ifdef TEST
ifstream fin("B-large.in");
ofstream fout("b.out");
//#define fout cout
#else
#define fin cin
#endif

int enc[255];
string encs = "QWERASDF";

int main()
{
	int T;
	fin >> T;
	memset(enc, -1, sizeof enc);
	for (int i=0; i<encs.length(); i++) enc[encs[i]] = i;

	for (int cases =0; cases < T; cases++)
	{
		int C;
		int D;
		int N;
		char a[10][10];
		bool oppo[10][10];
		memset(a, 0, sizeof a);
		memset(oppo, 0, sizeof oppo);

		fin >> C;
		for (int i=0; i<C; i++)
		{
			string rule;
			fin >> rule;
			a[enc[rule[0]]][enc[rule[1]]] = a[enc[rule[1]]][enc[rule[0]]] = rule[2];
		}
		fin >> D;
		for (int i=0; i<D; i++)
		{
			string rule;
			fin >> rule;
			oppo[enc[rule[0]]][enc[rule[1]]] = oppo[enc[rule[1]]][enc[rule[0]]] = true;
		}

		fin >> N;
		string s;
		fin >> s;

		vector<char> list;
		for (int i=0; i<N; i++)
		{
			if (list.size() > 0)
			{
				bool processed = false;
				if (enc[list.back()] >= 0)
				{
					if (a[enc[list.back()]][enc[s[i]]] > 0)
					{
						int x = list.back();
						list.pop_back();
						list.push_back(a[enc[x]][enc[s[i]]]);
						processed = true;
					}
				}
				if (!processed)
				{
					for (int j=0; j<list.size(); j++)
						if (enc[list[j]] >= 0 && oppo[enc[list[j]]][enc[s[i]]])
						{
							list.clear();
							processed = true;
							break;
						}
				}
				if (!processed)
				{
					list.push_back(s[i]);
				}
			}
			else list.push_back(s[i]);
		}

		fout << "Case #" << cases+1 << ": [";

		for (int i=0; i<list.size(); i++)
		{
			fout << list[i];
			if (i != list.size() -1) fout << ", ";
		}
		fout << "]\n";
	}
	return 0;
}