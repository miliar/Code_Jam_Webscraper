#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

namespace Solve
{
	const int NPOINT_MAX = 1050,
		  NCUT_MAX = 1050,
		  NITER = 1000;
	struct Point
	{
		double x, y;
		double cross_product(const Point &p) const
		{ return x * p.y - y * p.x; }
		void set_mid(const Point &p1, const Point &p2, double v)
		{
			x = v;
			y = (v - p1.x) / (p2.x - p1.x) * (p2.y - p1.y) + p1.y;
		}
	};
	Point point[2][NPOINT_MAX], pquery[NPOINT_MAX];
	int npoint[2], npquery;

	inline bool cmp_inc(const Point &a, const Point &b)
	{ return a.x < b.x; }
	inline bool cmp_dec(const Point &a, const Point &b)
	{ return a.x > b.x; }

	void add_point(const Point *pt, int npt, double a, double b);
	double get_area(double left, double right);

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		fprintf(fout, "Case #%d:\n", casenu);
		int w, ncut;
		fscanf(fin, "%d%d%d%d", &w, npoint, npoint + 1, &ncut);
		for (int i = 0; i < 2; i ++)
		{
			for (int j = 0; j < npoint[i]; j ++)
				fscanf(fin, "%lf%lf", &point[i][j].x, &point[i][j].y);
			point[i][npoint[i] ++].x = -1;
			point[i][npoint[i] ++].x = w + 1;
		}
		sort(point[0], point[0] + npoint[0], cmp_inc);
		sort(point[1], point[1] + npoint[1], cmp_inc);
		double tgt_area = get_area(0, w) / ncut, prev_pos = 0;
		for (int i = 1; i < ncut; i ++)
		{
			double left = prev_pos, right = w;
			for (int j = 0; j < NITER; j ++)
			{
				double mid = (left + right) * 0.5;
				if (get_area(prev_pos, mid) < tgt_area)
					left = mid;
				else
					right = mid;
			}
			prev_pos = left;
			fprintf(fout, "%.9lf\n", left);
		}
	}
}

void Solve::add_point(const Point *pt, int npt, double a, double b)
{
	bool first = false;
	double pmin = min(a, b),
		   pmax = max(a, b);
	for (int i = 0; i < npt; i ++)
	{
		if (pt[i].x >= pmin && pt[i].x <= pmax)
		{
			if (!first)
			{
				first = true;
				pquery[npquery ++].set_mid(pt[i - 1], pt[i], a);
			}
			pquery[npquery ++] = pt[i];
		} else if (first)
		{
			pquery[npquery ++].set_mid(pt[i - 1], pt[i], b);
			return;
		}
	}
	for (int i = 1; i < npt; i ++)
		if (a >= min(pt[i].x, pt[i - 1].x) && a <= max(pt[i].x, pt[i - 1].x))
		{
			pquery[npquery ++].set_mid(pt[i - 1], pt[i], a);
			pquery[npquery ++].set_mid(pt[i - 1], pt[i], b);
			return;
		}
}

double Solve::get_area(double left, double right)
{
	npquery = 0;
	add_point(point[0], npoint[0], left, right);
	double ans = 0;
	for (int i = 1; i < npquery; i ++)
		ans += (pquery[i].x - pquery[i - 1].x) * (pquery[i].y + pquery[i - 1].y);
	npquery = 0;
	add_point(point[1], npoint[1], left, right);
	for (int i = 1; i < npquery; i ++)
		ans -= (pquery[i].x - pquery[i - 1].x) * (pquery[i].y + pquery[i - 1].y);
	return fabs(ans) * 0.5;

	/*
	double ans = 0;
	for (int i = 0; i < npquery; i ++)
		ans += pquery[i].cross_product(pquery[(i + 1) % npquery]);
	return fabs(ans) * 0.5;
	*/
}

int main()
{
	Solve::solve(stdin, stdout);
}

