#include <cstdio>
#include <vector>
#include <utility>

using namespace std;

int width;
vector< pair<double, double> > upper;
vector< pair<double, double> > lower;
int N;

double interpolate(const pair<double, double> &p, const pair<double, double> &q, double x)
{
	double ratio = (x - p.first) / (q.first - p.first);
	return p.second + ratio * (q.second - p.second);
}

void find_cut(double cx, const vector< pair<double, double> > &line, int &idx, double &cy)
{
	int i;
	for (i = 0;i < line.size();i++)
	{
		if (line[i].first > cx)
			break;
	}
	if (i == line.size())
	{
		idx = -1;
		return;
	}

	idx = i;
	cy = interpolate(line[i - 1], line[i], cx);
	//printf("%lf, %lf => %lf, %lf ==> %lf, %lf\n", line[i - 1].first, line[i - 1].second, line[i].first, line[i].second, cx, cy);
}

double get_area(double cut_line)
{
	vector< pair<double, double> > points;
	
	double cy;
	int cidx;
	find_cut(cut_line, lower, cidx, cy);

	if (cidx == -1)
	{
		for (int i = 0;i < lower.size();i++)
			points.push_back(lower[i]);
	}
	else
	{
		for (int i = 0;i < cidx;i++)
			points.push_back(lower[i]);
		points.push_back(make_pair(cut_line, cy));
	}

	find_cut(cut_line, upper, cidx, cy);
	if (cidx == -1)
	{
		for (int i = upper.size() - 1;i >= 0;i--)
			points.push_back(upper[i]);
	}
	else
	{
		points.push_back(make_pair(cut_line, cy));
		for (int i = cidx - 1;i >= 0;i--)
			points.push_back(upper[i]);
	}

	double v = 0;
	for (int i = 0;i < points.size();i++)
	{
		pair<double, double> &p = points[i];
		pair<double, double> &q = points[(i + 1) % points.size()];
		//printf("%lf %lf\n", p.first, p.second);

		v += (p.first * q.second);
		v -= (p.second * q.first);
	}

	if (v < 0) v *= -1;

	return v;
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int ti = 1;ti <= tc;ti++)
	{
		upper.clear();
		lower.clear();
		fprintf(stderr, "Case %d\n", ti);
		printf("Case #%d:\n", ti);
		int L, U;
		scanf("%d %d %d %d", &width, &L, &U, &N);
		for (int i = 0;i < L;i++)
		{
			int p, q;
			scanf("%d %d", &p, &q);
			lower.push_back(make_pair(p, q));
		}
		for (int i = 0;i < U;i++)
		{
			int p, q;
			scanf("%d %d", &p, &q);
			upper.push_back(make_pair(p, q));
		}

		double area = get_area(width);
		fprintf(stderr, "%lf\n", area);

		for (int i = 1;i < N;i++)
		{
			double needed_area = area * i / N;

			double st = 0;
			double ed = width;
			for (int it = 0;it < 200;it++)
			{
				double mid = (st + ed) / 2;
				double area = get_area(mid);
				//printf("%lf => %lf\n", mid, area);
				if (area > needed_area)
					ed = mid;
				else
					st = mid;
			}
			printf("%.10lf\n", (st + ed) / 2);
		}
	}
	return 0;
}
