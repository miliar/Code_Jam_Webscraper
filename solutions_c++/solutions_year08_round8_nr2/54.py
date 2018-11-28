#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <assert.h>
#include <memory.h>
#include <string>

using namespace std;

const double PI = 3.14159265358;
const int MAX_N = 301;
const int INF = 5000;

struct offer
{
	int a, b;
	int c;
};

int N;
map<string, int> colors;
vector<offer> offers;

struct state
{
	state(int _x, int _c1, int _c2) : x(_x), c1(_c1), c2(_c2) {}

	int x;
	int c1, c2;
};

bool operator < (const state& s1, const state& s2)
{
	if (s1.x != s2.x)
		return s1.x < s2.x;

	if (s1.c1 != s2.c1)
		return s1.c1 < s2.c1;

	if (s1.c2 != s2.c2)
		return s1.c2 < s2.c2;

	return false;
}

map<state, int> d;

int find_color(const std::string& s)
{
	if (colors.count(s))
		return colors[s];

	int cc = colors.size();
	return colors[s] = cc;
}

int finalize(int x, int c1, int c2, int c3)
{
	int res = 0, i = 0;

	while (x < 10000)
	{
		int best = -1;
		while (i < offers.size() && offers[i].a <= x)
		{
			if (offers[i].c == c1 || offers[i].c == c2 || offers[i].c == c3)
				best = max(best, offers[i].b+1);
			i++;
		}

		if (best <= x)
			return INF;

		x = best;
		res++;
	}

	return res;
}	

int solve(int x, int c1, int c2)
{
	if (x > 9999)
		return 0;

	state s(x, c1, c2);

	if (d.count(s))
		return d[s];

	int& res = d[s];
	res = INF;

	for (int j=0; j < offers.size() && offers[j].a <= x; j++)
		if (offers[j].b >= x)
		{
			if (offers[j].c == c1 || offers[j].c == c2)
				res = min(res, solve(offers[j].b+1, c1, c2)+1);
			else if (c1 == -1 || c2 == -1)
			{
				int cc1 = c1, cc2 = c2;
				if (cc1 == -1)
					cc1 = offers[j].c;
				else
					cc2 = offers[j].c;

				res = min(res, solve(offers[j].b+1, cc1, cc2)+1);
			}
			else
				res = min(res, finalize(offers[j].b+1, c1, c2, offers[j].c)+1);
		}

	return d[s];
}

bool ofcmp(const offer& x, const offer& y)
{
	return x.a < y.a;
}

void solve()
{
	// Sort offers
	sort(offers.begin(), offers.end(), ofcmp);
	
	// Solve
	d.clear();
	int res = solve(0, -1, -1);
	if (res >= INF)
		cout << "IMPOSSIBLE";
	else
		cout << res;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int tt=1; tt <= T; tt++)
	{
		colors.clear();
		offers.clear();

		cin >> N;
		for (int i=0; i < N; i++)
		{
			int a, b, c;
			string s;
			cin >> s >> a >> b;
			a--; b--;
			c = find_color(s);

			offer o;
			o.a = a;
			o.b = b;
			o.c = c;
			offers.push_back(o);
		}

		cout << "Case #" << tt << ": ";
		solve();
		cout << endl;
	}

	return 0;
}