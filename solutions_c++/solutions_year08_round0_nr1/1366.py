#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define PB push_back
#define For(i,n) for (i = 0; i < n; i++)
#define bend(v) v.begin (), v.end ()

ifstream fin("input.in");
ofstream fout("output.out");

vector<string> engines;
vector<string> queries;
int memo[101][1001];

int doit(int sInd, int qInd)
{
	if (qInd == queries.size())
		return 0;

	int &res = memo[sInd][qInd];
	if (res != -1) return res;

	res = 1000000000;

	if (engines[sInd] != queries[qInd])
		res = doit(sInd, qInd + 1);
	else
	{
		for (int i = 0; i < engines.size(); i++)
		{
			if (i == sInd)
				continue;

			res = min(res, 1 + doit(i, qInd));
		}
	}

	return res;
}

int main ()
{
	int tno;
	fin >> tno;

	for (int t = 0; t < tno; t++)
	{
		int sno;
		fin >> sno;

		engines.clear();
		char name[100];
		fin.getline(name, 99);
		for (int i = 0; i < sno; i++)
		{
			string s;
			
			fin.getline(name, 99);
			s = name;
			engines.PB(name);
		}

		int qno;
		fin >> qno;

		queries.clear();
		fin.getline(name, 99);
		for (int i = 0; i < qno; i++)
		{
			string s;
			//char name[100];
			fin.getline(name, 99);
			s = name;
			queries.PB(name);
		}

		int res = 1000000000;
		memset(memo, -1, sizeof(memo));

		for (int i = 0; i < engines.size(); i++)
			res = min(res, doit(i, 0));

		fout << "Case #" << t + 1 << ": " << res << endl;
		
	}

	return 0;
}