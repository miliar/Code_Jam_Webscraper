#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int a, b, p;

void Load()
{
	scanf("%d%d%d", &a, &b, &p);
}

int rt[1200];
int ispr[1200];

int Root(int x)
{
	if (x != rt[x]) rt[x] = Root(rt[x]);
	return rt[x];
}

void Solve()
{
	int i;
	for (i = a; i <= b; i++)
	{
		rt[i] = i;
	}
	int j;
	memset(ispr, 0, sizeof(ispr));
	for (i = 2; i <= b; i++)
	{
		ispr[i] = 1;
		for (j = 2; j < i; j++)
		{
			if (i % j == 0) 
			{
				ispr[i] = 0;
				break;
			}
		}
	}
	for (i = a; i <= b; i++)
	{
		for (j = i + 1; j <= b; j++)
		{
			int k;
			for (k = p; k <= min(i, j); k++)
			{
				if (ispr[k] == 0) continue;
				if ((i % k == 0) && (j % k == 0))
				{
					rt[Root(i)] = Root(j);
					break;
				}
			}
		}
	}
	int ans = 0;
	for (i = a; i <= b; i++) if (Root(i) == i) ans++;
	cout << ans;
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