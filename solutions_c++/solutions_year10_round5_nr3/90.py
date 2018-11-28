/*
 * $File: c.cpp
 * $Date: Sat Jun 12 23:41:20 2010 +0800
 */

#include <map>
using namespace std;

namespace Solve
{
	typedef map<int, int> Mii;
	Mii data;
	bool next();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase = 0;
	fscanf(fin, "%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		data.clear();
		int c;
		fscanf(fin, "%d", &c);
		while (c --)
		{
			int p, v;
			fscanf(fin, "%d%d", &p, &v);
			data[p] = v;
		}
		int ans = 0;
		while (next())
			ans ++;
		fprintf(fout, "Case #%d: %d\n", id, ans);
	}
}

bool Solve::next()
{
	int max_val = 0;
	Mii::iterator max_pos = data.end();
	for (Mii::iterator iter = data.begin(); iter != data.end(); iter ++)
		if (iter->second > max_val)
		{
			max_val = iter->second;
			max_pos = iter;
		}
	if (max_val == 1)
		return false;
	data[max_pos->first - 1] ++;
	data[max_pos->first + 1] ++;
	max_pos->second -= 2;
	if (max_val == 2)
		data.erase(max_pos);
	return true;
}

int main()
{
	Solve::solve(stdin, stdout);
}

