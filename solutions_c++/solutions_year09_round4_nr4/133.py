#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long Int;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = a; i < b; i++)
#define RFOR(i, a, b) for(i = a - 1; i >= b; i--)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size()) 
#define ALL(a) (a).begin(),(a).end() 

#define PB push_back
#define MP make_pair

#define MAX 64

int X[64];
int Y[64];
int R[64];
Int Mask[1 << 17];

double dist(double x, double y)
{
	return sqrt(x*x + y*y);
}

pair<int, pair<double, double> > F(int a, int b, double r)
{
	double d = dist(0.0 + X[a] - X[b], 0.0 + Y[a] - Y[b]);
	if(d + R[a] + R[b] > r + r)
		return MP(0, MP(0.0, 0.0));

	double dx = X[b] - X[a];
	double dy = Y[b] - Y[a];
	dx /= d;
	dy /= d;

	double x = X[a] - dx*R[a] + dx*(d + R[a] + R[b])/2;
	double y = Y[a] - dy*R[a] + dy*(d + R[a] + R[b])/2;

	return MP(1, MP(x, y));
}

vector<pair<double, double> > F(double x1, double y1, double r1, double x2, double y2, double r2)
{
	vector<pair<double, double> > res;
	double d = dist(x1 - x2, y1 - y2);
	if(d > r1 + r2)
		return res;
	if(r1 > r2 + d)
		return res;
	if(r2 > r1 + d)
		return res;

	double dx = x2 - x1;
	double dy = y2 - y1;

	double x = x1 + dx*r1/(r1 + r2);
	double y = y1 + dy*r1/(r1 + r2);

	double h = sqrt(r1*r1 - d*d*r1*r1/(r1 + r2)/(r1 + r2));
	
	double xx1 = x + dy*h/d;
	double yy1 = y - dx*h/d;
	double xx2 = x - dy*h/d;
	double yy2 = y + dx*h/d;

	res.PB(MP(xx1, yy1));
	res.PB(MP(xx2, yy2));

	return res;
}

pair<int, pair<double, double> > F(int a, int b, int c, double r)
{
	if(r < R[a] || r < R[b] || r < R[c])
		return MP(0, MP(0.0, 0.0));
	if(a == b && b == c)
		return MP(1, MP(X[a] + 0.0, Y[a] + 0.0));
	if(a == b)
		return F(b, c, r);
	if(b == c)
		return F(a, b, r);

	int I[] = {a, b, c};
	int i, j;
	FOR(i, 0, 3)
	{
		a = I[i];
		b = I[(i + 1) % 3];
		c = I[(i + 2) % 3];

		vector< pair<double, double> > res = F(X[a], Y[a], r - R[a], X[b], Y[b], r - R[b]);
		FOR(j, 0, SIZE(res))
			if(dist(X[c] - res[j].first, Y[c] - res[j].second) <= r - R[c])
				return MP(1, res[j]);
	}
	
	return MP(0, MP(0.0, 0.0));
}

int SolveTest(int test)
{
	int N;
	scanf("%d", &N);
	int i, j, k, l;
	FOR(i, 0, N)
		scanf("%d%d%d", &X[i], &Y[i], &R[i]);

	double Min = 0, Max = 10000;
	int t;
	FOR(t, 0, MAX)
	{
		double Mid = (Min + Max)/2;
		int cnt = 0;
		FOR(i, 0, N)
			FOR(j, 0, i + 1)
				FOR(k, 0, j + 1)
				{
					pair<int, pair<double, double> > res = F(i, j, k, Mid);
					if(res.first)
					{
						double x = res.second.first;
						double y = res.second.second;

						Int mask = 0;
						FOR(l, 0, N)
							if(dist(X[l] - x, Y[l] - y) <= Mid - R[l])
								mask |= 1LL << l;

						Mask[cnt] = mask;
						++cnt;
					}
				}
		
		int found = 0;
		FOR(i, 0, cnt)
			if(found == 0)
				FOR(j, 0, i + 1)
					if((Mask[i] | Mask[j]) == (1LL << N) - 1)
					{
						found = 1;
						break;
					}

		if(found)
			Max = Mid;
		else
			Min = Mid;
	}

	printf("Case #%d: %.7lf\n", test + 1, Max);

	return 0;
}

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	char buf[1 << 10];
	gets(buf);
	int T, t;
	sscanf(buf, "%d", &T);
	FOR(t, 0, T)
		SolveTest(t);

	return 0;
};
