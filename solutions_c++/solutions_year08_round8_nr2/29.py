#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

int n;
int clr[310];
int be[310], en[310];
map<string, int> cname;

void Load()
{
	scanf("%d", &n);
	cname.clear();
	int i;
	for (i = 0; i < n; i++)
	{
		char c = getchar();
		while (! ((c >= 'A') && (c <= 'Z')) ) c = getchar();
		string cc = "";
		while ((c >= 'A') && (c <= 'Z'))
		{
			cc += c;
			c = getchar();
		}
		if (cname.find(cc) == cname.end())
		{
			int cnum = cname.size();
			cname[cc] = cnum;
		}
		clr[i] = cname[cc];
		scanf("%d%d", &be[i], &en[i]);
	}
}

class State
{
public:
	int uc[3];
};

bool operator<(const State &a, const State &b)
{
	int i;
	for (i = 0; i < 3; i++)
	{
		if (a.uc[i] < b.uc[i]) return true;
		if (a.uc[i] > b.uc[i]) return false;
	}
	return false;
}

map<State, int> canbe[11000];

bool AddOffer(State &a, int p)
{
	int i;
	for (i = 0; i < 3; i++)
	{
		if (a.uc[i] == clr[p]) return true;
	}
	if (a.uc[2] != -1) return false;
	a.uc[2] = clr[p];
	if (a.uc[2] > a.uc[1])
	{
		int t = a.uc[2];
		a.uc[2] = a.uc[1];
		a.uc[1] = t;
	}
	if (a.uc[1] > a.uc[0])
	{
		int t = a.uc[0];
		a.uc[0] = a.uc[1];
		a.uc[1] = t;
	}
	return true;
}

void Solve()
{
	int i, j;
	for (i = 0; i <= 10000; i++)
	{
		canbe[i].clear();
	}
	State a;
	a.uc[0] = a.uc[1] = a.uc[2] = -1;
	canbe[0][a] = 0;
	for (i = 0; i < 10000; i++)
	{
		map<State, int>::iterator p;
		for (p = canbe[i].begin(); p != canbe[i].end(); p++)
		{
			for (j = 0; j < n; j++)
			{
				if (be[j] > i + 1) continue;
				if (en[j] < i + 1) continue;
				State b = p->first;
				if (AddOffer(b, j))
				{
					if (canbe[en[j]].find(b) == canbe[en[j]].end()) canbe[en[j]][b] = p->second + 1;
					else
					{
						int tgo = canbe[en[j]][b];
						if (tgo > p->second + 1)
						{
							canbe[en[j]][b] = p->second + 1;
						}
					}
				}
			}
		}
	}
	map<State, int>::iterator p;
	int mr = 2000000000;
	for (p = canbe[10000].begin(); p != canbe[10000].end(); p++)
	{
		mr = min(mr, p->second);
	}
	if (mr == 2000000000) printf("IMPOSSIBLE");
	else printf("%d", mr);
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