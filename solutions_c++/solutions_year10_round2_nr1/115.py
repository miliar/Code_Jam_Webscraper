const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

int ii, nn;

struct item
{
	string name;
	map<string, item> childs;
	set<string> childs_nams;
	bool friend operator < (const item &x, const item &y)
	{
		return x.name < y.name;
	}
};

item root;
int res;

void add(item &r, string nam)
{
	if (r.childs_nams.find(nam) == r.childs_nams.end())
	{
		r.childs_nams.insert(nam);
		item t;
		t.name = nam;
		r.childs[nam] = t;
		++res;
	}
}

void process(item &r, string s)
{
	size_t pos = s.find("/");
	if (pos > 1000000000)
		add(r, s);
	else
	{
		string sub = s.substr(0, pos);
		add(r, sub);
		s.erase(0, pos+1);
		process(r.childs[sub], s);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &nn);
	for (ii=0; ii<nn; ++ii)
	{
		int n,m;
		scanf("%d%d\n", &n, &m);

		res = 0;

		root.childs.clear();
		root.childs_nams.clear();

		for (int i=0; i<n; ++i)
		{
			char s[1000];
			gets(s);
			string s1(s);
			s1.erase(0, 1);
			process(root, s1);
		}

		res = 0;
		
		for (int i=0; i<m; ++i)
		{
			char s[1000];
			gets(s);
			string s1(s);
			s1.erase(0, 1);
			process(root, s1);
		}

		printf("Case #%d: %d\n", ii+1, res);
	}
	return 0;
}
