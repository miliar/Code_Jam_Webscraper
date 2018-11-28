#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <cassert>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> VI;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back

#define NMAX 205

int timeToInt(string t)
{
	return atoi(t.substr(0, 2).c_str()) * 60 + atoi(t.substr(3, 2).c_str());
}

struct Trip
{
	int dep, arr;
	char start;
};

bool Cmp(const Trip& t1, const Trip& t2)
{
	if (t1.dep != t2.dep) return t1.dep < t2.dep;
	return t1.arr < t2.arr;
}
int n1, n2, n;
int t;
Trip trip[NMAX];
bool g[NMAX][NMAX];
bool used[NMAX];

bool can(Trip& t1, Trip& t2)
{
	if (t1.start == t2.start) return false;
	return t2.dep >= t1.arr + t;
}

void solve(int test)
{
	memset(g, 0, sizeof(g));
	memset(used, 0, sizeof(used));

	scanf("%d", &t);
	scanf("%d %d\n", &n1, &n2);	
	string s1, s2;
	n = n1 + n2;
	forn(i, n)
	{
		cin >> s1 >> s2;		
		trip[i].dep = timeToInt(s1);
		trip[i].arr = timeToInt(s2);
		if (i < n1) trip[i].start = 'A';
		else trip[i].start = 'B';
	}

	sort(trip, trip + n1 + n2, Cmp);
	forn(i, n)
	{
		forn(j, n)
		{
			g[i][j] = can(trip[i], trip[j]);
		}
	}
	int a1 = 0, a2 = 0;
	forn(i, n)
	{
		if (!used[i])
		{
			used[i] = true;
			if (trip[i].start == 'A') a1++; else a2++;
		}
		for (int j = i + 1; j < n; j++)
		{
			if (g[i][j] && !used[j])
			{
				used[j] = true;
				break;
			}
		}
	}

	printf("Case #%d: %d %d\n", test, a1, a2);
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; scanf("%d\n", &tc);	
	forn(it, tc)
	{
		solve(it + 1);
	}
	return 0;
}
