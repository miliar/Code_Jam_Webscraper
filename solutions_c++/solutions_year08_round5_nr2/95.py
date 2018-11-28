#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>
#include <cmath>
#include <numeric>
#include <deque>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long ll;

#define NMAX 20
#define MMAX 230
#define INF 1000000009

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

struct Pos
{
	int a, y, b;
	int t1, t2;
};

inline bool operator<(const Pos& p1, const Pos& p2)
{
	if (p1.a != p2.a) return p1.a < p2.a;
	if (p1.b != p2.b) return p1.b < p2.b;
	if (p1.y != p2.y) return p1.y < p2.y;
	if (p1.t1 != p2.t1) return p1.t1 < p2.t1;
	return p1.t2 < p2.t2;
}

char a[NMAX][NMAX];
int n, m;
map<Pos, int> d;
deque<Pos> q;
Pos st;
int finx, finy;
int next[MMAX][4];

bool valid(int x, int y)
{
	return (x >= 0 && y >= 0 && x < n && y < m && a[x][y] == '.');
}

void go0(Pos u, Pos v)
{
	if (v.b > v.y)
	{
		swap(v.b, v.y);
		swap(v.t1, v.t2);
	}
	if (d.count(v) == 0)
	{		
		d.insert(mp(v, d[u]));
		q.push_front(v);
	}
}

void go1(Pos u, Pos v)
{
	if (v.b > v.y)
	{
		swap(v.b, v.y);
		swap(v.t1, v.t2);
	}
	if (d.count(v) == 0)
	{
		d.insert(mp(v, d[u] + 1));
		q.push_back(v);
	}	
}
void solve(int test)
{
	scanf("%d %d\n", &n, &m);
	int N = n * m;
	forn(i, n)
	{
		forn(j, m)
		{
			scanf("%c", &a[i][j]);
			if (a[i][j] == 'O')
			{
				st.a = i * m + j;
				st.b = st.y = N;
				st.t1 = st.t2 = 0;
				a[i][j] = '.';	
			}
			else if (a[i][j] == 'X')
			{
				a[i][j] = '.';
				finx = i;
				finy = j;				
			}
		}
		scanf("\n");
	}	

	forn(i, n)
	{
		forn(j, m)
		{
			if (a[i][j] == '.')
			{
				forn(k, 4)
				{
					int x = i;
					int y = j;
					while (valid(x + dx[k], y + dy[k]))
					{
						x += dx[k];
						y += dy[k];
					}
					next[i * m + j][k] = x * m + y;
				}
			}
		}
	}
	
	d.clear();
	d.insert(mp(st, 0));
	q.clear();
	q.push_back(st);

	Pos u, v;
	while (!q.empty())
	{
		u = q.front(); q.pop_front();
		forn(k, 4)
		{
			v = u;
			v.b = next[u.a][k];
			v.t1 = k;
			if (v.t1 == v.t2 && v.b == v.y) continue;

			go0(u, v);
		}
		forn(k, 4)
		{
			v = u;
			v.y = next[u.a][k];
			v.t2 = k;
			if (v.t1 == v.t2 && v.b == v.y) continue;

			go0(u, v);
		}

		forn(k, 4)
		{
			if (u.b == u.a && k == u.t1 && u.y != N)
			{
				v = u;
				v.a = u.y;
				go1(u, v);
				if (v.a / m == finx && v.a % m == finy)
				{
					printf("Case #%d: %d\n", test, d[v]);
					return;
				}
			}			
			else if (u.y == u.a && k == u.t2 && u.b != N)
			{
				v = u;
				v.a = u.b;
				go1(u, v);
				if (v.a / m == finx && v.a % m == finy)
				{
					printf("Case #%d: %d\n", test, d[v]);
					return;
				}
			}
		}


		forn(k, 4)
		{
			int x = u.a / m + dx[k];
			int y = u.a % m + dy[k];
			if (valid(x, y))
			{
				v = u;
				v.a = x * m + y;
				go1(u, v);
				if (v.a / m == finx && v.a % m == finy)
				{
					printf("Case #%d: %d\n", test, d[v]);
					return;
				}
			}
		}
					
	}
	printf("Case #%d: THE CAKE IS A LIE\n", test);
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
