#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int ReadTime()
{
	char c = getchar();
	while (! ((c >= '0') && (c <= '9'))) c = getchar();
	int hr = 0;
	while ((c >= '0') && (c <= '9'))
	{
		hr *= 10;
		hr += c - '0';
		c = getchar();
	}
	while (! ((c >= '0') && (c <= '9'))) c = getchar();
	int mn = 0;
	while ((c >= '0') && (c <= '9'))
	{
		mn *= 10;
		mn += c - '0';
		c = getchar();
	}
	return hr * 60 + mn;
}

class Event
{
public:
	int time, type;
};

bool operator<(const Event &a, const Event &b)
{
	if (a.time < b.time) return true;
	if (a.time > b.time) return false;
	if (a.type < b.type) return true;
	if (a.type > b.type) return false;
	return false;
}

vector<Event> evt;

void Load()
{
	evt.clear();
	int na, nb, t;
	scanf("%d%d%d", &t, &na, &nb);
	int i;
	for (i = 0; i < na; i++)
	{
		int t1, t2;
		t1 = ReadTime();
		t2 = ReadTime() + t;
		Event a;
		a.time = t1;
		a.type = 1;
		evt.push_back(a);
		a.time = t2;
		a.type = 2;
		evt.push_back(a);
	}
	for (i = 0; i < nb; i++)
	{
		int t1, t2;
		t1 = ReadTime();
		t2 = ReadTime() + t;
		Event a;
		a.time = t1;
		a.type = 3;
		evt.push_back(a);
		a.time = t2;
		a.type = 0;
		evt.push_back(a);
	}
}

void Solve()
{
	sort(evt.begin(), evt.end());
	int ca, cb, na, nb;
	ca = cb = na = nb = 0;
	int i;
	for (i = 0; i < evt.size(); i++)
	{
		if (evt[i].type == 0) ca++;
		else if (evt[i].type == 2) cb++;
		else if (evt[i].type == 1)
		{
			if (ca == 0)
			{
				ca++;
				na++;
			}
			ca--;
		}
		else if (evt[i].type == 3)
		{
			if (cb == 0)
			{
				cb++;
				nb++;
			}
			cb--;
		}
	}
	cout << na << " " << nb;
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