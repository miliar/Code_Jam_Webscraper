#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

int c;
map<int, int> have;

void Load()
{
	have.clear();
	scanf("%d", &c);
	int i;
	for (i = 0; i < c; i++)
	{
		int p, v;
		scanf("%d%d", &p, &v);
		have[p] += v;
	}
}

void Solve()
{
	long long ans = 0;
	int f = 1;
	while (f)
	{
		f = 0;
		map<int, int>::iterator p;
		map<int, int> add;
		add.clear();
		for (p = have.begin(); p != have.end(); p++)
		{
			if (p->second > 1)
			{
				add[p->first - 1] += p->second / 2;
				add[p->first + 1] += p->second / 2;
				ans += p->second / 2;
				p->second %= 2;
				f = 1;
			}	
		}
		for (p = add.begin(); p != add.end(); p++) 
		{
			have[p->first] += p->second;
		}
	}
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