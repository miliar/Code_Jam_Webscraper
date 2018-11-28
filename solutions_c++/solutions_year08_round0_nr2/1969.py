//#pragma comment(linker, "/STACK:10000000")
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <stack>
#include <queue>
#include <cmath>
using namespace std;
typedef long long lint;

struct Event
{
	int time;
	int s;
	Event(int time = 0, int s = 0) : time(time), s(s) {}
};
inline bool operator<(Event a, Event b)
{
	return a.time < b.time;
}

int Ans[2];
int Cur[2];

vector<Event> B;
vector<Event> E;

bool Solve(int test)
{
	int t;
	scanf("%d", &t);
	int na, nb;
	int n[2];
	scanf("%d %d", n, n + 1);
	for(int k = 0; k < 2; ++k)
		for(int i = 0; i < n[k]; ++i)
		{
			int h, m;
			scanf("%d:%d", &h, &m);
			int time = 60 * h + m;
			if(!time)
				time = 24 * 60;
			B.push_back(Event(time, k));
			scanf("%d:%d", &h, &m);
			time = 60 * h + m;
			if(!time)
				time = 24 * 60;
			E.push_back(Event(time + t, k));
		}
	sort(B.begin(), B.end());
	sort(E.begin(), E.end());
	B.push_back(Event(48 * 60, 0));
	E.push_back(Event(48 * 60, 0));
	int b = 0;
	int e = 0;
	for(int i = 0; i < 2; ++i)
	{
		Ans[i] = 0;
		Cur[i] = 0;
	}
	while(1)
	{
		if(B[b].time < E[e].time)
		{
			if(!Cur[B[b].s])
			{
				Cur[B[b].s] = 1;
				Ans[B[b].s]++;
			}
			Cur[B[b].s]--;
			b++;
		}
		else
		{
			if(E[e].time == 48 * 60)
				break;
			Cur[1 - E[e].s]++;
			e++;
		}
	}
	printf("Case #%d: %d %d\n", test, Ans[0], Ans[1]);
	B.clear();
	E.clear();
	return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
#endif
	int t = 0;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	//while(Solve(++t));
	return 0;
}