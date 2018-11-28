#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;

struct Dir
{
	map<string, Dir> dirs;
};

Dir root;
int Add(const string& s)
{
	vector<string> path;
	for (int i = 0; i < s.size(); )
	{
		i++;
		int a = i;
		while (i != s.size() && s[i] != '/')
		{
			i++;
		}
		path.push_back(s.substr(a, i - a));
	}
	Dir* c = &root;
	int res = 0;
	for (int i = 0; i < path.size(); i++)
	{
		string& g = path[i];
		if (c->dirs.count(g) == 0)
		{
			c->dirs[g] = Dir();
			res++;
		}
		c = &c->dirs[g];
	}
	return res;
}

void Go()
{
	int n, m;
	cin >> n >> m;
	string s;
	root.dirs.clear();
	for (int i = 0; i < n; i++)
	{
		cin >> s;
		Add(s);
	}
	int res = 0;
	for (int j = 0; j < m; j++)
	{
		cin >> s;
		res += Add(s);
	}
	cout << res;
}

int main()
{
#ifdef _DEBUG
	freopen("inp.txt", "r", stdin);
#else
	const string file_name = "A-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int yy = 1; yy <= t; yy++)
	{
		printf("Case #%d: ", yy);
		Go();
		printf("\n");
	}
	return 0;
}