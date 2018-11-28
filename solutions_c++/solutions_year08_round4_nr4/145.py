#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int k;
char s[1100];
int n;

void Load()
{
	scanf("%d", &k);
	char c = getchar();
	while (! ((c >= 'a') && (c <= 'z')) ) c = getchar();
	n = 0;
	while ((c >= 'a') && (c <= 'z'))
	{
		s[n] = c;
		n++;
		c = getchar();
	}
}

int mans;
int was[10];
int cp[10];
char ns[1100];

void Check()
{
	int i, j;
	for (i = 0; i < n; i += k)
	{
		for (j = 0; j < k; j++)
		{
			ns[i + j] = s[i + cp[j]];
		}
	}
	int cans = 1;
	for (i = 1; i < n; i++)
	{
		if (ns[i] != ns[i - 1]) cans++;
	}
	if (cans < mans) mans = cans;
}

void Gen(int pos)
{
	if (pos == k) 
	{
		Check();
		return;
	}
	int i;
	for (i = 0; i < k; i++)
	{
		if (was[i] != 0) continue;
		was[i] = 1;
		cp[pos] = i;
		Gen(pos + 1);
		was[i] = 0;
	}
}

void Solve()
{
	mans = n;
	memset(was, 0, sizeof(was));
	Gen(0);
	cout << mans;
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