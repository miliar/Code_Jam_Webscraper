#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const long double EPS = 1e-9;
const long double PI = 3.1415926535897932384626433832795;

typedef long double ld;
typedef long long i64;
typedef pair <int, int> PII;

int vn;
vector <string> v[10240];
vector <int> to[10240];
char ch[1024];

int add(char *s)
{
	int res = 0, cur = 0;
	while (*s)
	{
		if (*s == '/') s++;
		string str = "";
		while (*s && *s != '/')
		{
			str += *s;
			s++;
		}

		bool b = true;
		for (int i = 0; i < (int)v[cur].size(); i++)
		{
			if (v[cur][i] == str)
			{
				b = false;
				cur = to[cur][i];
				break;
			}
		}
		if (b)
		{
			res++;
			vn++;
			v[vn].clear();
			to[vn].clear();
			v[cur].push_back(str);
			to[cur].push_back(vn);
			cur = vn;
		}
	}
	return res;
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tcn, n, m;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		vn = 0;
		v[0].clear();
		to[0].clear();
		scanf("%d%d", &n, &m);
		while (n--)
		{
			scanf("%s", ch);
			add(ch);
		}
		int ans = 0;
		while (m--)
		{
			scanf("%s", ch);
			ans += add(ch);
		}
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}
