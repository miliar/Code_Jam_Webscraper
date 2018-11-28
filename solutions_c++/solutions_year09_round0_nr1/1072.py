#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

int l, d, n;
vector<string> s;

void Load()
{
	scanf("%d%d%d", &l, &d, &n);
	char c = getchar();
	while (c != 10) c = getchar();
	s.clear();
	int i;
	for (i = 0; i < d; i++)
	{
		c = getchar();
		string cs = "";
		while (! ((c == 10) || (c == EOF)))
		{
			if (c >= 'a' && c <= 'z') cs += c;
			c = getchar();
		}
		s.push_back(cs);
	}
}

string cpat;
vector<int> p;

void Solve()
{
	cpat = "";
	char c = getchar();
	while (! ((c == 10) || (c == EOF)))
	{
		if ((c >= 'a' && c <= 'z') || c == '(' || c == ')') cpat += c;
		c = getchar();
	}
	p.clear();
	int i;
	for (i = 0; i < cpat.length();)
	{
		if (cpat[i] == '(')
		{
			int cur = 0;
			while (cpat[i] != ')')
			{
				if ((cpat[i] >= 'a') && (cpat[i] <= 'z'))
				{
					cur |= 1 << (cpat[i] - 'a');
				}
				i++;
			}
			p.push_back(cur);
			i++;
		}
		else
		{
			p.push_back(1 << (cpat[i] - 'a'));
			i++;
		}
	}
//	for (i = 0; i < l; i++) cerr << p[i] << " ";
//	cerr << "\n";
	int ans = 0;
	for (i = 0; i < d; i++)
	{
		int j;
		int f = 1;
		for (j = 0; j < l; j++)
		{
			int y = s[i][j] - 'a';
			if (!(p[j] & (1 << y)))
			{
				f = 0;
				break;
			}
		}
		ans += f;
	}
	printf("%d", ans);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	Load();
	int i;
	for (i = 0; i < n; i++)
	{
		printf("Case #%d: ", i + 1);
		Solve();
		printf("\n");
	}
	return 0;
}