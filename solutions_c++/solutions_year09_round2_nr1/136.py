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
const string FILENAME = "gcj";

char ss[10000000];

int cnt;
int ll[1000000], rr[1000000];
char nam[1000000][100];
double ww[1000000];

void wait(int &pos, char c, char c1 = -1, char c2 = -1)
{
	while (ss[pos] != c && ss[pos] != c1 && ss[pos] != c2)
		++pos;
}

void skip(int &pos, char c)
{
	while (ss[pos] == c)
		++pos;
}

int bt(int &pos)
{
	int res = ++cnt;

	wait(pos, '(');
	++pos;
	skip(pos, ' ');
	sscanf(&ss[pos], "%lf", &ww[cnt]);

	wait(pos, ' ', ')');
	skip(pos, ' ');
	if (ss[pos] == ')')
	{
		ll[res] = rr[res] = -1;
		nam[res][0] = 0;
	}
	else
	{
		sscanf(&ss[pos], "%s", nam[cnt]);
		wait(pos, ' ');
		ll[res] = bt(pos);
		rr[res] = bt(pos);
	}

	wait(pos, ')');
	++pos;
	return res;
}


int nn,n,m,len,pos,k;
char s[1000000], s1[1000000];

set<string> nams;

double Get(double p, int v)
{
	if (v == -1)
		return p;
	p *= ww[v];
	if (nams.find(nam[v]) != nams.end())
		return Get(p, ll[v]);
	else
		return Get(p, rr[v]);
}

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	scanf("%d", &nn);
	for (int ii=1; ii<=nn; ++ii)
	{
		scanf("%d", &n);
		gets(s);
		len = 0;
		for (int i=0; i<n; ++i)
		{
			gets(&ss[len]);
			len += (int)strlen(&ss[len]);
			ss[len++] = ' ';
			ss[len] = 0;
		}

		cnt = -1;
		pos = 0;
		bt(pos);

		printf("Case #%d:\n", ii);

		scanf("%d", &n);
		gets(s);
		for (int i=0; i<n; ++i)
		{
			nams.clear();
			scanf("%s %d", s, &k);
			for (int i=0; i<k; ++i)
			{
				scanf("%s", s1);
				nams.insert(s1);
			}
			gets(s1);

			printf("%.10lf\n", Get(1.0, 0));
		}
	}

	return 0;
} 