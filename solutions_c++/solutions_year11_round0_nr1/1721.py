#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

const int D[3] = {-1, 0, 1};

struct State
{
	int n, x, y;
};

#define NMAX 105

int d[NMAX][NMAX][NMAX];
bool used[NMAX][NMAX][NMAX];
queue<State> q;


void update(State& u, State& v)
{
	if (v.x < 0 || v.x > 99) return;
	if (v.y < 0 || v.y > 99) return;
	if (used[v.n][v.x][v.y]) return;
	used[v.n][v.x][v.y] = true;
	d[v.n][v.x][v.y] = d[u.n][u.x][u.y] + 1;
	q.push(v);
}

void solve(int tc)
{
	printf("Case #%d: ", tc);

	int n;

	cin >> n;

	while (!q.empty()) q.pop();

	vector<int> pos;
	vector<int> types;

	forn(i, n)
	{
		string ty;
		int ps;
		cin >> ty >> ps;
		pos.pb(ps - 1);
		types.pb(int(ty == "B"));
	}

	forn(i, n + 1)
	{
		forn(x, 100)
		{	
			forn(y, 100)
			{
				used[i][x][y] = false;
			}
		}
	}

	d[0][0][0] = 0;
	used[0][0][0] = true;


	State st = {0, 0, 0};
	q.push(st);

	while (!q.empty())
	{
		State u = q.front();
		q.pop();

		if (u.n == n)
		{
			printf("%d\n", d[u.n][u.x][u.y]);
			return;
		}

		if (types[u.n] == 0 && pos[u.n] == u.x)
		{
			forn(i, 3)
			{
				State v = {u.n + 1, u.x, u.y + D[i]};
				update(u, v);
			}
		}

		if (types[u.n] == 1 && pos[u.n] == u.y)
		{
			forn(i, 3)
			{
				State v = {u.n + 1, u.x + D[i], u.y};
				update(u, v);
			}
		}

		forn(i, 3)
		{
			forn(j, 3)
			{
				State v = {u.n, u.x + D[i], u.y + D[j]};
				update(u, v);
			}
		}
	}

}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
	int tc;
	cin >> tc;
	forn(it, tc) solve(it + 1);
    return 0;
}
            
