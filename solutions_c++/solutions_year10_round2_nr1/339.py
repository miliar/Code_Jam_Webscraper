#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
using namespace std;
struct Dir
{
	map<string, Dir*> subs;
	~Dir()
	{
		for (map<string, Dir*>::iterator it = subs.begin();
			it != subs.end(); ++it)
			delete it->second;
	}
	bool has(string name)
	{
		if (subs.find(name) != subs.end())
			return true;
		else
			return false;
	}
	void insert(string name)
	{
		subs.insert(make_pair(name, new Dir));
	}
};

char in[128];

int main()
{
	int T;
	scanf("%d", &T);
	for (int idx = 1; idx <= T; ++idx)
	{
		printf("Case #%d: ", idx);
		int n, m;
		int res = 0;
		Dir root;
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", in);
			for (int j = 0; j < strlen(in); ++j)
			{
				if (in[j] == '/') in[j] = ' ';
			}
			istringstream is(in);
			string name;
			Dir* cur = &root;
			while (is >> name)
			{
				cur->insert(name);
				cur = cur->subs[name];
			}
		}
		for (int i = 0; i < m; ++i)
		{
			scanf("%s", in);
			for (int j = 0; j < strlen(in); ++j)
			{
				if (in[j] == '/') in[j] = ' ';
			}
			istringstream is(in);
			string name;
			Dir* cur = &root;
			while (is >> name)
			{
				if (!cur->has(name))
				{
					cur->insert(name);
					++res;
				}
				cur = cur->subs[name];
			}
		}
		printf("%d\n", res);
	}
	return 0;
}