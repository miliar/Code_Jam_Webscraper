#include <cmath>
#include <cstdio>
#include <vector>

using std::vector;

inline double max(const double& a, const double& b) {return a > b ? a : b;}

struct point
{
	point() {}
	point(const int& xx, const int& ww) : x(xx), w(ww) {}

	int x;
	int w;
};

class region
{
public:
	region() {}
	region(const vector<point>& v);
	
	void merge(const region& r, const int& d);
	void find_dispersion(const int& d);

	double from;
	double to;
	double cost;

	vector<point> points;
};

region::region(const vector<point>& v)
{
	points = vector<point>(v);
}

void region::merge(const region& r, const int& d)
{
	for (int i = 0; i < (int)r.points.size(); i++)
		points.push_back(r.points[i]);

	find_dispersion(d);		
}

double find_cost(const vector<point>& points, const int& d, const double& mid)
{
	int count = 0;
	
	for (int i = 0; i < (int)points.size(); i++)
		count += points[i].w;

	double from, to;

	if (count % 2)
	{
		from = mid - (count/2) * d;
		to = mid + (count/2) * d;
	} else
	{
		from = mid - (count/2 - 0.5) * d;
		to = mid + (count/2 - 0.5) * d;
	}
	
	double cost = 0;
	int cpi = 0;
	for (int i = 0; i < (int)points.size(); i++)
		for (int j = 0; j < points[i].w; j++)
		{
			double endpos = from + cpi*d;
			double currpos = points[i].x;
			if (std::abs(endpos-currpos) > cost) cost = std::abs(endpos-currpos);
			cpi++;
		}
		
	return cost;
}

void region::find_dispersion(const int& d)
{	
	double lo = points[0].x;
	double hi = points.back().x;
	double md = (lo+hi) / 2;
	
	while (hi-lo > 1e-8)
	{
		double loval = find_cost(points, d, (lo+md)/2);
		double mdval = find_cost(points, d, md);
		double hival = find_cost(points, d, (md+hi)/2);
	
		if (loval < mdval && loval < hival)
			hi = md;
		else if (hival < mdval && hival < loval)
			lo = md;
		else {lo = (lo+md)/2; hi=(md+hi)/2;}
		
		md = (lo+hi) / 2;
	}
	
	cost = find_cost(points, d, md);
	
	int count = 0;
	
	for (int i = 0; i < (int)points.size(); i++)
		count += points[i].w;

	if (count % 2)
	{
		from = md - (count/2) * d;
		to = md + (count/2) * d;
	} else
	{
		from = md - (count/2 - 0.5) * d;
		to = md + (count/2 - 0.5) * d;
	}
}

int main()
{
	int tests;
	std::scanf("%d", &tests);
	for (int currtest = 1; currtest <= tests; currtest++)
	{
		int p, d;
		std::scanf("%d%d", &p, &d);
		
		vector<vector<point> > points(1);
		for (int i = 0; i < p; i++)
		{
			point pt;
			std::scanf("%d%d", &(pt.x), &(pt.w));

			if (i == 0 || pt.x - points.back().back().x < d)
				points.back().push_back(pt);
			else points.push_back(vector<point>(1, pt));
		}
		
		vector<region> regions(points.size());
		for (int i = 0; i < (int)regions.size(); i++)
		{
			regions[i] = region(points[i]);
			regions[i].find_dispersion(d);
		}
			
		bool final = false;
		while (!final)
		{
			final = true;
			for (int i = 1; i < (int)regions.size(); i++)
				if (regions[i].from - regions[i-1].to < d)
				{
					regions[i-1].merge(regions[i], d);
					for (int j = i; j < (int)regions.size()-1; j++)
						regions[j] = regions[j+1];
					regions.pop_back();
					final = false;
					break;
				}
		}
		
		double ans = 0;
		for (int i = 0; i < (int)regions.size(); i++)
			if (regions[i].cost > ans) ans = regions[i].cost;
			
		std::printf("Case #%d: %.12lf\n", currtest, ans);
	}

	return 0;
}
