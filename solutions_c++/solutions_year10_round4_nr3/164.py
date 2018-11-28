#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define cell pair<int, int>

set<cell> s;
struct ev
{
	int x, y, type; // 0-add, 1-delete
	ev(int x, int y, int type) : x(x), y(y), type(type)
	{
	}
	friend bool operator < (const ev &a, const ev &b)
	{
		return MP(a.x, a.y) > MP(b.x, b.y);
	}
};

set<ev> e1, e2;

void init()
{
	for (set<cell>::iterator it = s.begin(); it != s.end(); it++)
	{
		int x = it->first, y = it->second;
		e1.insert(ev(x, y, 1));
		e1.insert(ev(x+1, y, 0));
		e1.insert(ev(x, y+1, 0));
	}
}

inline bool f(int x, int y)
{
	return s.find(MP(x, y)) != s.end();
}

void print(int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			printf("%c", f(j+1, i+1) ? '1' : '0');
		}
		printf("\n");
	}
	printf("\n");
}

void solvecase() {
	int r, x1, y1, x2, y2;
	scanf("%d", &r);
	s.clear();
	e1.clear();
	e2.clear();
	for (int i = 0; i < r; i++)
	{
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int x = x1; x <= x2; x++)
			for (int y = y1; y <= y2; y++)
				s.insert(MP(x, y));
	}
	init();
	int res = 0;
	while (!s.empty())
	{
		//print(5);
		set<cell> ch;
		e2.clear();
		for (set<ev>::iterator it = e1.begin(); it != e1.end(); it++)
		{
			int x = it->x, y = it->y;
			if (ch.find(MP(x, y)) != ch.end())
				continue;
			if (it->type == 0)
			{
				if (!f(x, y) && f(x - 1, y) && f(x, y - 1))
				{
					ch.insert(MP(x, y));
					s.insert(MP(x, y));
					e2.insert(ev(x+1, y, 0));
					e2.insert(ev(x, y+1, 0));
				}				
			} 
			else 
			{
				if (f(x, y) && !f(x-1, y) && !f(x, y-1))
				{
					ch.insert(MP(x, y));
					s.erase(MP(x, y));
					e2.insert(ev(x+1, y, 1));
					e2.insert(ev(x, y+1, 1));
				}
			}
		}
		e1 = e2;
		res++;
	}
	printf("%d", res);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("C-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}