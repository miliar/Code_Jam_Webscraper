#include <iostream>
#include <map>
#include <sstream>
#include <cstdlib>
#include <string>
#include <set>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <bitset>
#include <ctime>

using namespace std;

#define _TEST_TIME
//#define pi_assert(condition, __VA_ARGS__) if (condition) fprintf(stderr, __VA_ARGS__);

#ifdef _TEST_TIME
clock_t start_time;
void print_time()
{
	fprintf(stderr, "Time used: %.4lf\n", double(clock() - start_time) / CLOCKS_PER_SEC);
}
#endif

struct point_t
{
	double x, y;
	point_t() : x(0), y(0) {}
	point_t(double a, double b) : x(a), y(b) {}
};

struct circle_t
{
	point_t p;
	double r;
};

typedef long long int64;

vector<point_t> points;
int64 cover[5000];
circle_t cp[500], backup[500];
int N;

double dis(point_t a, point_t b) 
{
	return hypot(a.x - b.x, a.y - b.y);
}

void get_cross(circle_t a, circle_t b, vector<point_t> &ret)
{
	double D = dis(a.p, b.p);
	if (D > a.r + b.r) return;
	if (D < fabs(a.r - b.r)) return;

	double cosT = (a.r * a.r + D * D - b.r * b.r) / 2 / a.r / D;
//	double T = acos(cosT);
	double D1 = cosT * a.r;
	double H = sqrt(a.r * a.r - D1 * D1);

	double dx = b.p.x - a.p.x;
	double dy = b.p.y - a.p.y;
	dx /= D;
	dy /= D;
	double tx = -dy;
	double ty = dx;

	double mx = a.p.x + dx * D1;
	double my = a.p.y + dy * D1;
	ret.push_back(point_t(mx + H * tx, my + H * ty));
	ret.push_back(point_t(mx - H * tx, my - H * ty));
}

bool covered(point_t m, double R, circle_t c)
{
//	cout << dis(m, c.p) << ' ' << R - c.r + 1e-12 << endl;
	return dis(m, c.p) < R - c.r + 1e-12;
}

ostream& operator<<(ostream &os, point_t p)
{
	os << "[" << p.x << "," << p.y << "]";
}

bool check(double R)
{
	static int64 bits[60];
	int64 temp = 1;
	for (int i = 0; i <= N; ++i)
	{
		bits[i] = temp;
		temp = temp * 2;
	}

	points.clear();
	memcpy(backup, cp, sizeof(cp));
	for (int i = 0; i < N; ++i)
	{
		if (R < backup[i].r) return false;
		backup[i].r = R - backup[i].r;
	}

	for (int i = 0; i < N; ++i)
	{
		points.push_back(backup[i].p);
		//cout << i << " -> " << backup[i].p << " , " << backup[i].r << endl;
		for (int j = i + 1; j < N; ++j)
			get_cross(backup[i], backup[j], points);
	}

	memcpy(backup, cp, sizeof(cp));

	int m = points.size();
	for (int i = 0; i < m; ++i)
	{
		point_t &mid = points[i];
		cover[i] = 0;
		for (int j = 0; j < N; ++j)
			if (covered(mid, R, backup[j]))
				cover[i] |= bits[j];
		for (int j = 0; j < i; ++j)
			if ((cover[j] | cover[i]) == bits[N] - 1) return true;
		//cout << mid << ", " << R << ": " << cover[i] << endl;
	}
	return false;
}

void solve()
{
	int nCase;
	cin >> nCase;
	for (int curCase = 0; curCase < nCase; ++curCase)
	{
		cin >> N;
		for (int i = 0; i < N; ++i) cin >> cp[i].p.x >> cp[i].p.y >> cp[i].r;

		if (N == 1)
		{
			printf("Case #%d: %.8lf\n", curCase + 1, cp[0].r);	
			continue;
		}

		double lower = 0, upper = 3000;
		while (lower < upper - 1e-10)
		{
			double middle = (upper + lower) / 2;
			if (check(middle)) 
				upper = middle;
			else 
				lower = middle;
		}

//		if (N == 3)
		if (N < 0)
		{
			double answer = 1e30;
			for (int i = 0; i < 3; ++i)
			{
				for (int j = 0; j < 3; ++j) if (i != j)
				{
					int k = 3 - i - j;
					answer = min(answer, max(cp[i].r, (dis(cp[j].p, cp[k].p) + cp[j].r + cp[k].r) / 2));
				}
			}
			printf("Case #%d: %.8lf\n", curCase + 1, answer);	
		}
		printf("Case #%d: %.8lf\n", curCase + 1, (lower + upper) / 2);	
//		if (curCase == 1) break;
	}
}

int	main()
{
#ifdef _TEST_TIME
	start_time = clock();
#endif

	solve();

#ifdef _TEST_TIME
	print_time();
#endif
	return 0;
}
