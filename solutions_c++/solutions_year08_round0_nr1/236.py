#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int s, q;
string eng[110];
string qry[1100];

void Load()
{
	scanf("%d", &s);
	int i;
	char c = getchar();
	while (c != 10) c = getchar();
	for (i = 0; i < s; i++)
	{
		eng[i] = "";
		c = getchar();
		while (c != 10)
		{
			eng[i] += c;
			c = getchar();
		}
	}
	scanf("%d", &q);
	c = getchar();
	while (c != 10) c = getchar();
	for (i = 1; i <= q; i++)
	{
		qry[i] = "";
		c = getchar();
		while (c != 10)
		{
			qry[i] += c;
			c = getchar();
		}
	}
}

int lpos[1100][110];
int res[1100];

void Solve()
{
	memset(lpos, 0, sizeof(lpos));
	int i, j;
	for (i = 1; i <= q; i++)
	{
		for (j = 0; j < s; j++)
		{
			if (qry[i] == eng[j]) lpos[i][j] = i;
			else lpos[i][j] = lpos[i - 1][j];
		}
	}
	memset(res, 0x7F, sizeof(res));
	res[0] = 0;
	for (i = 1; i <= q; i++)
	{
		for (j = 0; j < s; j++)
		{
			int t = lpos[i][j];
			if (res[i] > res[t] + 1) res[i] = res[t] + 1;
		}
	}
	if (res[q] == 0) res[q] = 1;
	cout << res[q] - 1;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}