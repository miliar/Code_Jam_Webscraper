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

struct word
{
	string s;
	int i;
};

word w[10010];
int u[32];
int mu[32];
int n, m;

bool match(string s, string mask)
{
	if (s.size() != mask.size())
		return false;
	for (int i = 0; i < (int)s.size(); i++)
	{
		if (mask[i] != '_' && mask[i] != s[i])
			return false;
		if (mask[i] == '_' && mu[s[i] - 'a'])
			return false;
	}
	return true;
}

int length(string s, string al)
{
	memset(u, 0, sizeof(u));
	string mask = "";
	for (int i = 0; i < (int)s.size(); i++)
		mask += "_";
	int res = 0, cnt = 0;
	memset(u, 0, sizeof(u));
	memset(mu, 0, sizeof(mu));
	for (int i = 0; i < n; i++)
	{
		if (match(w[i].s, mask))
		{
			cnt++;
			for (int j = 0; j < (int)w[i].s.size(); j++)
				u[w[i].s[j] - 'a'] = true;
		}
	}

	for (int ii = 0; ii < 26 && cnt > 1; ii++)
	{
		if (u[al[ii] - 'a'])
		{
			mu[al[ii] - 'a'] = true;
			bool guess = false;
			for (int i = 0; i < (int)s.size(); i++)
			{
				if (al[ii] == s[i])
				{
					mask[i] = s[i];
					guess = true;
				}
			}
			if (!guess)
				res++;

			cnt = 0;
			memset(u, 0, sizeof(u));
			for (int i = 0; i < n; i++)
			{
				if (match(w[i].s, mask))
				{
					cnt++;
					for (int j = 0; j < (int)w[i].s.size(); j++)
						u[w[i].s[j] - 'a'] = true;
				}
			}
		}
	}

//	cout << " " << s << " " << al << " " << res << endl;
	return res;
}

int main()
{
	freopen("B-small-attempt1.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(8);

	int tcn;
	scanf("%d", &tcn);
	char ch[32];

	for (int tc = 1; tc <= tcn; tc++)
	{
		scanf("%d%d", &n, &m);
		printf("Case #%d:", tc);
		gets(ch);
		for (int i = 0; i < n; i++)
		{
			gets(ch);
			w[i].s = ch;
			w[i].i = 0;
		}

		for (int i = 0; i < m; i++)
		{
			gets(ch);
			string al = ch;
			string res = w[0].s;
			int nres = 0;

			for (int j = 0; j < n; j++)
			{
				int z = length(w[j].s, al);
				if (nres < z)
				{
					nres = z;
					res = w[j].s;
				}
			}

			printf(" %s", res.c_str());
		}
		puts("");
	}

	return 0;
}
