#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define memfill(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))
#define bound(x, y, n, m) x >= 0 && y >= 0 && x < n && y < m
#define MAX_N 1001

int n0, n1, dd;
int a0, a1;

int getTime(char *s)
{
	return (s[0] - '0') * 600 + (s[1] - '0') * 60 + (s[3] - '0') * 10 + (s[4] - '0');
}

struct rec
{
	int pt, ar, time;

	bool operator< (rec r) const
	{
		if (time != r.time)
			return time < r.time;
		if (ar != r.ar)
			return ar > r.ar;
		return 0;
	}
};

rec events[MAX_N];
int ec;

void addEvent(int pt, int ar, int time)
{
	events[ec].pt = pt;
	events[ec].ar = ar;
	events[ec++].time = time;
}

void solve()
{
	a0 = a1 = 0;
	sort(events, events + ec);
	int cur0 = 0, cur1 = 0;
	for (int i = 0; i < ec; i++)
		if (events[i].ar)
			if (events[i].pt)
				cur0++;
			else
				cur1++;
		else
			if (events[i].pt)
				if (cur1)
					cur1--;
				else
					a1++;
			else
				if (cur0)
					cur0--;
				else
					a0++;

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test_num;
	scanf("%d", &test_num);
	for (int test_count = 0; test_count < test_num; test_count++)
	{
		scanf("%d%d%d", &dd, &n0, &n1);
		ec = 0;
		for (int i = 0; i < n0; i++)
		{
			char dts[90], ats[90];
			scanf("%s%s", dts, ats);
			addEvent(0, 0, getTime(dts));		
			addEvent(0, 1, getTime(ats) + dd);		
		}
		for (int i = 0; i < n1; i++)
		{
			char dts[90], ats[90];
			scanf("%s%s", dts, ats);
			addEvent(1, 0, getTime(dts));		
			addEvent(1, 1, getTime(ats) + dd);		
		}
		solve();
		printf("Case #%d: %d %d\n", test_count + 1, a0, a1);
	}
	return 0;
}