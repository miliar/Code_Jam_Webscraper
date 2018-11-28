#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)
#define CL(x) memset(x, 0, sizeof(x));

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> VS;

struct dir
{
	map<string, int> mp;
};

vector<dir> h;
char str[1 << 20];
int cnt = 0;

void Add()
{
	for (int i = 0; str[i]; i++)
		if (str[i] == '/')
			str[i] = ' ';
	int r = 1;
	for (char *t = strtok(str, " "); t; t = strtok(0, " "))
	{
		string s(t);
		if (h[r].mp[s] == 0)
		{
			cnt++;
			h[r].mp[s] = h.size();
			h.resize(h.size() + 1);
		}
		r = h[r].mp[s];
	}
}

void Solve()
{
	h.resize(2);
	h[1].mp.clear();
	int n, m;
	scanf("%d %d", &n, &m);
	FOR(i, n)
	{
		scanf("%s", str);
		Add();
	}
	cnt = 0;
	FOR(i, m)
	{
		scanf("%s", str);
		Add();
	}
	printf("%d\n", cnt);
}

int main()
{
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}