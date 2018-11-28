#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
#define LL long long
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }
#define fo(i, n) for (int i = 0; i < (n); i++)
#define foz(i, a) for (int i = 0; i < (a).size(); i++)

typedef double gbase;
const gbase geps = 1e-9;

struct Point
{
	gbase x, y;
	Point(gbase x = 0, gbase y = 0) : x(x), y(y) {}
	Point to(const Point &p) const { return Point(p.x - x, p.y - y); }
	gbase dot(const Point &p) const { return p.x * x + p.y * y; }
	gbase cross(const Point &p) const { return x * p.y - y * p.x; }
	gbase len2() const { return x*x + y*y; }
	double len() const { return sqrt(len2()); }
	Point normalized() const { double t = len(); return Point(x/t, y/t); }
	friend Point operator + (const Point &a, const Point &b) { return Point(a.x + b.x, a.y + b.y); }
	friend Point operator - (const Point &a, const Point &b) { return Point(a.x - b.x, a.y - b.y); }
	friend Point operator * (gbase k, const Point &p) { return Point(p.x * k, p.y * k); }
	friend Point operator * (const Point &p, gbase k) { return Point(p.x * k, p.y * k); }
	friend bool operator < (const Point &u, const Point &v) { return false; }
};


void init()
{

}

#define maxn 10

int n, m;
int res;
int a[maxn];
int u[maxn], v[maxn];
bool g[maxn][maxn];
int resa[maxn];

vector<int> rooms;

bool check(int k)
{
	int need = (1<<k) - 1;
	fo(i, rooms.size())
	{
		int have = 0;
		fo(j, n) if (rooms[i] & (1<<j)) have |= 1 << a[j];
		if (have != need) return false;
	}
	return true;
}

void go(int cur, int k)
{
	if (cur == n)
	{
		if (k > res && check(k))
		{
			res = k;
			fo(i, n) resa[i] = a[i];
		}			
		return;
	}
	a[cur] = k;
	go(cur + 1, k + 1);
	fo(i, k)
	{
		a[cur] = i;
		go(cur + 1, k);
	}
}

Point p[maxn];

int getnext(int i, int j)
{
	double mindot = 1e20;
	int res = -1;
	fo(k, n) if (g[j][k] && k != i) { 
		Point a = p[i].to(p[j]).normalized();
		Point b = p[j].to(p[k]).normalized();
		if (a.cross(b) > 0)
		{	
			double x = a.dot(b);
			if (x < mindot)
			{
				mindot = x;
				res = k;
			}
		}
	}
	return res;
}

void solvecase()
{
	scanf("%d%d", &n, &m);
	fo(i, m) scanf("%d", &u[i]);
	fo(i, m) scanf("%d", &v[i]);
	fo(i, n) fo(j, n) g[i][j] = false;
	fo(i, m) {
		g[u[i]-1][v[i]-1] = true;
		g[v[i]-1][u[i]-1] = true;
	}
	fo(i, n) g[i][(i+1)%n] = true;

	set<int> tmp;
	fo(i, n) {
		double ang = (double) i / n * (2 * pi);
		p[i] = Point(cos(ang), sin(ang));
	}

	fo(i, n) fo(j, n) if (g[i][j])
	{
		int st = i;
		int x = 1<<st;
		int cur = j, prev = i;
		while (cur != st)
		{
			x |= 1<<cur;
			int next = getnext(prev, cur);
			prev = cur, cur = next;
		}
		tmp.insert(x);
	}

	rooms.clear();
	for (set<int>::iterator it = tmp.begin(); it != tmp.end(); it++) rooms.push_back(*it);
	res = 0;
	go(0, 0);
	printf("%d\n", res);
	fo(i, n) printf("%d ", resa[i] + 1);
}



void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
		fflush(stdout);
	}
}

#define problem_letter "C"
//#define fname "test"
//#define fname problem_letter "-small-attempt0"
#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
//#define fname problem_letter "-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}