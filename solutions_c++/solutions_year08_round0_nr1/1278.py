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

int bestswitch(int se, int qind, vector <int> & eng, vector <vector <int> > & table)
{
	if (qind >= eng.size()) return 0;
	if (table[se][qind] != -1) return table[se][qind];
	if (se == eng[qind]) return table[se][qind] = 2000000000;

	int i, j;

	for(i = qind; i < eng.size() && se != eng[i]; ++i);

	int best = 2000000000;
	for(j = 0; j < table.size(); ++j)
	{
		if (j != se) 
		{
			int res = bestswitch(j, i, eng, table) + 1;
			best = min(best, res);
		}
	}
	return table[se][qind] = best;
}
int main()
{
	int T, N;
	ifstream fin("a.in");
	ofstream fout("a.out");

	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		int s, q, i;

		fout << "Case #" << T << ": ";
		fin >> s;
		vector <string> name(s);

		getline(fin, name[0]);
		for(i = 0; i < s; ++i)
			getline(fin, name[i]);

		fin >> q;
		if (q == 0)
		{
			fout << "0" << endl;
			continue;
		}
		vector <int> eng(q);
		string temp;

		getline(fin, temp);
		for(i = 0; i < q; ++i)
		{
			getline(fin, temp);
			eng[i] = find(name.begin(), name.end(), temp) - name.begin();
		}

		vector <vector <int> > table(s, vector <int> (q, -1));

		int bestres = 2000000000;
		for(i = 0; i < s; ++i)
			bestres = min(bestswitch(i, 0, eng, table), bestres);

		fout << bestres - 1 << endl;		
	}
	return 0;
}