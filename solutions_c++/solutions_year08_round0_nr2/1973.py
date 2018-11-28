#define _CRT_SECURE_NO_DEPRECATE 
#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 
using namespace std; 

struct Item
{
	int st, wh, s, e, id;

	Item(int st_, bool wh_, int s_, int e_, int id_): 
		st(st_), wh(wh_), s(s_), e(e_), id(id_) 
	{
	}

	bool operator<(const Item& r) const
	{
		if (s != r.s) return s > r.s;
		if (wh != r.wh) return wh==0;
		return id < r.id; // to prevent exception of stl
	}
};

int T, Na, Nb;
priority_queue<Item> q;
int cnt[2], r[2];
int m1,h1,m2,h2;

int main()
{
	int Cases;
	scanf("%d", &Cases);

	for (int Case=0; Case<Cases; ++Case)
	{
		int idsource=0;
		scanf("%d%d%d", &T, &Na, &Nb);
		for (int i=0; i<Na; ++i)
		{
			scanf("%d:%d%d:%d", &h1, &m1, &h2, &m2);
			q.push(Item(0, 0, h1*60+m1, h2*60+m2,idsource++));
		}
		for (int i=0; i<Nb; ++i)
		{
			scanf("%d:%d%d:%d", &h1, &m1, &h2, &m2);
			q.push(Item(1, 0, h1*60+m1, h2*60+m2,idsource++));
		}
		r[0] = 0;
		r[1] = 0;
		cnt[0] = 0;
		cnt[1] = 0;
		while (true)
		{
			if (q.empty()) break;

			Item c = q.top(); 
			q.pop();
			if (c.wh==1)		// train
				++cnt[c.st];
			else				// station
			{
				if (cnt[c.st])
					--cnt[c.st];
				else
					++r[c.st];
				q.push(Item(1-c.st, 1, c.e+T, -1, idsource++));
			}
		}
		printf("Case #%d: %d %d\n", Case+1, r[0], r[1]);
	}
	return 0;
} 
