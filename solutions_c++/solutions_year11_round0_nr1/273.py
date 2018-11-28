#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
using namespace std;

int T;
int testid;

int N;
queue<int> l;
queue<int> r;
vector<int> action;
void init()
{
	while (l.size() > 0) l.pop();
	while (r.size() > 0) r.pop();
	action.clear();
	scanf("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		string s; int p;
		cin >> s >> p;
		if (s == "O") 
		{
			l.push(p);
			action.push_back(1);
		}
		else 
		{
			r.push(p);
			action.push_back(2);
		}
	}
}

void york()
{
	int lp = 1; int rp = 1;
	int ans = 0;
	for (int i = 0; i < action.size(); ++i)
	{
		int act = action[i]; 
		if (act == 1)
		{
			int mt = abs(lp - l.front());
			lp = l.front();
			l.pop();
			ans += (mt + 1);

			if (r.size() > 0)
			{
				for (int t = 1; t <= mt + 1; ++t)
					if (r.front() != rp)
						rp += (r.front() - rp) / abs(r.front() - rp);
			}
		}
		else
		{
			int mt = abs(rp - r.front());
			rp = r.front();
			r.pop();
			ans += (mt + 1);

			if (l.size() > 0)
			{
				for (int t = 1; t <= mt + 1; ++t)
					if (l.front() != lp)
						lp += (l.front() - lp) / abs(l.front() - lp);
			}
		}
	}
	printf("Case #%d: %d\n", testid, ans);
}

int main()
{
	scanf("%d", &T);
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}

	return 0;
}



