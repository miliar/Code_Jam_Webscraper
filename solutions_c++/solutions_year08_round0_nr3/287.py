#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define all(c) (c).begin(), (c).end()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

map<string, map<string, int> > ids;
int id(string cat, string s) {
	map<string,int>& m = ids[cat];
	if (m.count(s) == 0) m[s] = si(m)-1;
	return m[s];
}

const double EPS = 1e-12;
const double PI = acos(-1);
double f,R,t,r,g;
double d0, radius, radius2, gap;

double G(double x) {
	return (x * sqrt(radius2 - x*x) + radius2 * asin(x / radius)) / 2.0;
}
double integral(double a, double b, double f) {
	return G(b) - G(a) - (b-a) * f;
}


#define dist(a,b) ((a)*(a) + (b)*(b))
double area(double x0, double y0, double x1, double y1) {
	if (dist(x1,y1) < radius2 + EPS) return (x1 - x0) * (y1 - y0);
	if (dist(x0,y0) > radius2 - EPS) return 0;

	double up = x0, down = x1;
	double tmp = radius2 - y1*y1;
	if (tmp > 0) up >?= sqrt(tmp);
	tmp = radius2 - y0*y0;
	if (tmp > 0) down <?= sqrt(tmp);
	return integral(x0,down,y0) - integral(x0,up,y1);
}

void init() {
	ids.clear();
}

void print(int cas, double res) {
	printf("Case #%d: %0.8lf\n",cas,res);
}


int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int _t; cin >> _t;
	forsn(cas,1,_t+1) {
		init();
		cin >> f >> R >> t >> r >> g;

		d0 = r + f;
		gap = g + 2*r;
		radius = R - t - f;
		radius2 = radius * radius;

		if (g < 2*f + EPS ||  R < t + f + EPS) {
			print(cas,1);
			continue;
		}

		double res = 0;
		for (double x = d0; x < radius + EPS; x += gap)
			for (double y = d0; x*x + y*y < radius2 + EPS; y += gap) {
				res += area(x,y,x + g-2*f,y + g-2*f);
			}

		double area = PI * R * R;
		res = 1 - (4 * res) / area;

		print(cas,res);

	}
	return 0;
}

