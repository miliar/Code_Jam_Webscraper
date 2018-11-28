#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <bitset>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define dbg(x) {cerr << #x << " " << x << endl;}
#define dbgv(x) {cout << "{ "; for(int i = 0; i < (x).size(); ++i) cout << " " << (x)[i]; cout << " }\n";}
const double eps = 1e-9;
const LD pi = 3.1415926535897932384626433832795;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream

bool equal(LD x, LD y)
{
	return fabs(x - y) < eps;
}

struct spoint
{
	LD x, y;
	spoint() { x = y = 0; }
	spoint(LD xx, LD yy) { x = xx, y = yy; }
	LD distTo(spoint b) 
	{ 
		return sqrt( (x - b.x) * (x - b.x) + (y - b.y) * (y - b.y) ); 
	}
	bool equalTo(spoint b)
	{
		return equal(b.x, x) && equal(b.y, y);
	}
};
bool operator < (const spoint &a, const spoint &b)
{
	if(a.x < b.x - eps) return true;
	else if(equal(a.x, b.x)) return a.y < b.y - eps;
	return false;
}

struct svector
{
	spoint a;
	svector() { }
	svector(spoint b) { a = b; }
	svector normalize() 
	{
		svector b = a;
		LD d = b.a.distTo(spoint());
		if(!equal(d, 0))
			b = b.div(d);
		//else
		//	exit(-1);
		return b;
	}

	svector normal()
	{
		return svector(spoint(- a.y, a.x));
	}
	svector negate()
	{
		return svector(spoint(- a.x, - a.y));
	}
	LD scalar(svector b)
	{
		return a.x * b.a.x + a.y * b.a.y;
	}
	LD dot(svector b)
	{
		return a.x * b.a.y - a.y * b.a.x;
	}
	LD length()
	{
		return a.distTo(spoint());
	}
	svector sub(svector b)
	{
		return svector(spoint(a.x - b.a.x, a.y - b.a.y));
	}
	svector add(svector b)
	{
		return svector(spoint(a.x + b.a.x, a.y + b.a.y));
	}
	svector mul(svector b)
	{
		return svector(spoint(a.x * b.a.x, a.y * b.a.y));
	}
	svector div(svector b)
	{
		return svector(spoint(a.x / b.a.x, a.y / b.a.y));
	}
	svector sub(LD b)
	{
		return svector(spoint(a.x - b, a.y - b));
	}
	svector add(LD b)
	{
		return svector(spoint(a.x + b, a.y + b));
	}
	svector mul(LD b)
	{
		return svector(spoint(a.x * b, a.y * b));
	}
	svector div(LD b)
	{
		return svector(spoint(a.x / b, a.y / b));
	}

};

struct point
{
	LD x, y, r;
	point() { }
	point(LD x, LD y, LD r) : x(x), y(y), r(r) { }
};
point a[50];
int n;
LL cover[50][50][2];
LL get(LD r, spoint c)
{
	LL mask = 0;
	for(int i = 0; i < n; ++i)
	{
		if(c.distTo(spoint(a[i].x, a[i].y)) <= r - a[i].r + eps)
			mask |= (1LL << LL(i));
	}
	return mask;
}

bool check(LD r)
{
	LL all = (1LL << LL(n)) - 1;
	for(int i = 0; i < n; ++i)
	{
		for(int j = i + 1; j < n; ++j)
		{
			spoint p(a[i].x, a[i].y);
			spoint q(a[j].x, a[j].y);
			LD r1 = a[i].r;
			LD r2 = a[j].r;
			svector dir = svector(q).sub(svector(p)).normalize();
			LD d = p.distTo(q);
			LD x1 = r - r1;
			LD x2 = r - r2;
			LD a = (x1 * x1 - x2 * x2 + d * d) / (2.0 * d);
			svector c = dir.mul(a).add(p);
			LD h = sqrt(x1 * x1 - a * a);
			svector o1 = dir.normal().normalize().mul(h).add(c);
			svector o2 = dir.normal().negate().mul(h).add(c);
			cover[i][j][0] = get(r, o1.a);
			cover[i][j][1] = get(r, o2.a);
		}
		cover[i][i][0] = get(r, spoint(a[i].x, a[i].y));
		cover[i][i][1] = get(r, spoint(a[i].x, a[i].y));
	}
	for(int i = 0; i < n; ++ i)
	for(int j = i; j < n; ++j)
	for(int w = 0; w < 2; ++w)
		for(int k = 0; k < n; ++k)
		for(int l = k; l < n; ++l)
		for(int v = 0; v < 2; ++v)
			if((cover[i][j][w] | cover[k][l][v]) == all)
				return true;
	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
		{
			int x, y, r;
			scanf("%d%d%d", &x, &y, &r);
			a[i] = point(x, y, r);
		}
		LD l = 0, r = 9999999999.0f;
		for(int i = 0; i < 62; ++i)
		{
			LD m = (l + r) / 2;
			if(check(m))
				r = m;
			else
				l = m;
		}
		printf("Case #%d: %.7lf\n", z + 1, (double)l);
	}

	return 0;
}