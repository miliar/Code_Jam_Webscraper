#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>

using namespace std;

int main()
{
	ifstream fin("d.in");
	ofstream fout("d.out");

	int T, N;

	fin >> N;

	for(T = 0; T < N; ++T)
	{
		int k, i, j;
		string s;

		fout << "Case #" << T + 1 << ": ";	

		fin >> k >> s;

		vector <int> perm;

		for(i = 0; i < k; ++i)
			perm.push_back(i);

		int best = 1000000000;

		do
		{
			string temp;

			for(i = 0; i < s.size() ; i+=k)
			{
				string t = s.substr(i, k);
				for(j = 0; j < t.size(); ++j)
					temp += t[perm[j]];
			}

			int b = 0;

			i = 0;

			while(i < temp.size())
			{
				j = i + 1;
				while(j < temp.size() && temp[j] == temp[i]) ++j;
				++b;
				i = j;
			}
			best = min(b , best);
		}while(next_permutation(perm.begin(), perm.end()));

		fout << best << endl;
	}
	return 0;
}