#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

struct time
{
	int m1, m2, h1, h2;
};

struct tt
{
	int l, r;
};

bool cmp(const tt &l, const tt &r)
{
	if(l.l < r.l) return true; else if(l.l == r.l) return l.r < r.r; return false;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int r;
	cin >> r;
	for (int p = 1; p <= r; p++)
	{
		int t;
		cin >> t;
		int a, b;
		cin >> a >> b;
		int ares, bres;
		ares = a;
		bres = b;
		vector<time> av(a);
		vector<time> bv(b);
		vector<tt> at(a);
		vector<tt> bt(b);
		vector<tt> at1(a);
		vector<tt> bt1(b);
		for (int i = 0; i < a; i++)
			scanf("%d:%d %d:%d", &av[i].h1, &av[i].m1, &av[i].h2, &av[i].m2);
		for (int i = 0; i < b; i++)
			scanf("%d:%d %d:%d", &bv[i].h1, &bv[i].m1, &bv[i].h2, &bv[i].m2);
		for (int i = 0; i < a; i++)
		{
			at[i].l = av[i].h1 * 60 + av[i].m1;
			at[i].r = av[i].h2 * 60 + av[i].m2 + t;
		}
		for (int i = 0; i < b; i++)
		{
			bt[i].l = bv[i].h1 * 60 + bv[i].m1;
			bt[i].r = bv[i].h2 * 60 + bv[i].m2 + t;
		}	
		sort(at.begin(), at.end(), cmp);
		sort(bt.begin(), bt.end(), cmp);
		at1 = at;
		bt1 = bt;
		bool fl = true;
		for (int i = 0; i < a; i++)
			for (int j = 0; j < bt1.size(); j++)
			{
				if (at1[i].r <= bt1[j].l)
				{
					bres--;
					bt1.erase(bt1.begin() + j);
					break;
				}
			}
		at1 = at;
		bt1 = bt;
		for (int i = 0; i < b; i++)
			for (int j = 0; j < at1.size(); j++)
			{
				if (bt1[i].r <= at1[j].l)
				{
					ares--;
					at1.erase(at1.begin() + j);
					break;
				}
			}
		cout << "Case #" << p << ": " << ares << " " << bres << endl;
	}
	return 0;
}