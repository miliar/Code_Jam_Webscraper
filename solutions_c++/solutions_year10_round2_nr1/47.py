#include <stdio.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

int N, M;

int dircnt;
string dirname[10005];
map<string, int> subdir[10005];

char path[10000];
int mkdir()
{
	int curdir = 0;
	int mk = 0;
	for (char* p = path; *p;)
	{
		++p;
		string name = "";
		while (*p && *p != '/')
			name += *(p++);
		if (subdir[curdir].find(name) == subdir[curdir].end())
		{
			dirname[dircnt] = name;
			subdir[curdir].insert(make_pair(name, dircnt++));
			++mk;
		}
		curdir = subdir[curdir][name];
	}
	return mk;
}

int main()
{
	int nround;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &nround);
	for (int round = 0; round < nround; ++round)
	{
		scanf("%d%d", &N, &M);
		dircnt = 1;
		for (int i = 0; i < 10005; ++i)
			subdir[i].clear();
		for (int i = 0; i < N; ++i)
		{
			scanf("%s", path);
			mkdir();
		}
		int ans = 0;
		for (int i = 0; i < M; ++i)
		{
			scanf("%s", path);
			ans += mkdir();
		}
		fprintf(stderr, "%d\n", dircnt);
		printf("Case #%d: %d\n", round + 1, ans);
	}

	return 0;
}
