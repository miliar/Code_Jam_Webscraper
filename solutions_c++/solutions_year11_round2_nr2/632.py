#include <cstdio>
#include <algorithm>

namespace Solve
{
	const int NPOINT_MAX = 205;
	const double PRECESION = 1e-10;
	struct Point
	{
		int pos, cnt;
		inline bool operator < (const Point &p) const
		{ return pos < p.pos; }
	};
	Point point[NPOINT_MAX];
	int npoint, min_gap;

	bool test(double max_move);
	double work();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		fscanf(fin, "%d%d", &npoint, &min_gap);
		for (int i = 0; i < npoint; i ++)
			fscanf(fin, "%d%d", &point[i].pos, &point[i].cnt);
		fprintf(fout, "Case #%d: %.9lf\n", casenu, work());
	}
}

double Solve::work()
{
	std::sort(point, point + npoint);
	double right = 1;
	while (!test(right))
		right *= 2;
	double left = 0;
	while (right - left > PRECESION)
	{
		double mid = (left + right) * 0.5;
		if (test(mid))
			right = mid;
		else
			left = mid;
	}
	return left;
}

bool Solve::test(double max_move)
{
	double p = point[0].pos - max_move - 1;
	for (int i = 0; i < npoint; i ++)
	{
		double left = point[i].pos - max_move;
		if (p < left)
			p = left;
		p += min_gap * (point[i].cnt - 1);
		if (p > point[i].pos + max_move)
			return false;
		p += min_gap;
	}
	return true;
}

int main()
{
	Solve::solve(stdin, stdout);
}

