#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <cstdio>
#include <cassert>

using namespace std;

typedef vector<int>		VI;
typedef vector<VI>		VVI;

const int oo = 1000000000;

int readint()
{
	string line;
	getline(cin, line);
	stringstream buf(line);
	int res;
	buf >> res;
	return res;
}

int maximum(const VVI &ar, int forbidden)
{
	int res = -1, val = -1;
	for (int i = 0; i < ar.size(); i++)
		if (i != forbidden && ar[i].back() > val)
		{
			val = ar[i].back();
			res = i;
		}
	return res;
}

int main()
{
	int kase = 0;
	for (int kases = readint(); kases; kases--)
	{
		int n = readint();
		map<string,int> t;
		VVI p(n);
		for (int i = 0; i < n; i++)
		{
			string x;
			getline(cin, x);
			t[x] = i;
		}
		int q = readint();
		for (int i = 0; i < q; i++)
		{
			string x;
			getline(cin, x);
			assert(t.find(x) != t.end());
			p[t[x]].push_back(i);
		}
		for (int i = 0; i < n; i++)
		{
			p[i].push_back(oo);
			reverse(p[i].begin(), p[i].end());
		}

		VI it(n, 0);
		int res = 0, pos = 0;
		int type = maximum(p, -1);
		int val = p[type].back();
		while (val < oo)
		{
			res++;
			for (int i = 0; i < n; i++)
				while (p[i].back() <= val)
					p[i].pop_back();
			type = maximum(p, type);
			val = p[type].back();
		}
		printf("Case #%d: %d\n", ++kase, res);
	}
	return 0;
}
