#include <cstdio>
#include <memory.h>
#include <iostream>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <functional>
#include <set>
#include <map>
#include <cstring>
#include <string>

#define MOD 10009

using namespace std;

int S;

vector< vector<int> > expr;
char buf[1024];

int cnt[MOD];

int letter[26];
int N;
vector<string> words;

long long ans[11];

void add_expr(char *term)
{
	int a, b, c, d;
	int len = strlen(term);
	/*
	for (a = 0;a <= (len >= 1);a++)
	{
		for (b = 0;b <= (len >= 2);b++)
		{
			for (c = 0;c <= (len >= 3);c++)
			{
				for (d = 0;d <= (len >= 4);d++)
				{
					vector<int> d;
					if (len >= 1)
						d.push_back(term[0] - 'a' + a * 26);
					if (len >= 2)
						d.push_back(term[1] - 'a' + b * 26);
					if (len >= 3)
						d.push_back(term[2] - 'a' + c * 26);
					if (len >= 4)
						d.push_back(term[3] - 'a' + d * 26);

					expr.push_back(d);
				}
			}
		}
	}
	*/
	vector<int> x;
	if (len >= 1)
		x.push_back(term[0] - 'a');
	if (len >= 2)
		x.push_back(term[1] - 'a');
	if (len >= 3)
		x.push_back(term[2] - 'a');
	if (len >= 4)
		x.push_back(term[3] - 'a');

	expr.push_back(x);
}

void get_expr()
{
	char *ptr = strtok(buf, "+");
	for (;ptr;ptr = strtok(NULL, "+"))
		add_expr(ptr);
}

long long eval()
{
	int i;
	long long s = 0;
	for (i = 0;i < expr.size();i++)
	{
		int j;
		long long r = 1;
		for (j = 0;j < expr[i].size();j++)
			r *= letter[expr[i][j]];
		s += r;
	}
	return s;
}

void go(int sel)
{
	if (sel)
	{
		ans[sel] += eval();
		ans[sel] %= MOD;
	}

	if (sel == S)
		return;
	int x, i;
	for (x = 0;x < N;x++)
	{
		for (i = 0;i < words[x].size();i++)
			letter[words[x][i] - 'a']++;

		go(sel + 1);

		for (i = 0;i < words[x].size();i++)
			letter[words[x][i] - 'a']--;
	}
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		expr.clear();
		scanf("%s", buf);
		get_expr();

		memset(cnt, 0, sizeof(cnt));

		cnt[0] = 1;

		scanf("%d", &S);

		scanf("%d", &N);

		words.clear();

		memset(ans, 0, sizeof(ans));

		int i;
		for (i = 0;i < N;i++)
		{
			string d;
			cin >> d;
			words.push_back(d);
		}
		go(0);

		printf("Case #%d:", ti);
		for (i = 1;i <= S;i++)
			printf(" %d", ans[i]);
		printf("\n");
	}
	return 0;
}
