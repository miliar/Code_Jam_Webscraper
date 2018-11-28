#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <math.h>
#include <stdio.h>

const double PI = 3.141592653589793238;

using namespace std;

struct Point
{
	Point(double xx = 0, double yy = 0)
	{
		x = xx;
		y = yy;
	}
	double x, y;
};

struct Pologon 
{
	vector<Point> ps;

	void print()
	{
		cout << "Ps: ";
		for (int i = 0; i <ps.size(); ++i)
			cout <<"(" << ps[i].x << "," << ps[i].y << ")  ";
		cout << endl;
	}
};

struct Chod
{
	vector<Point> ps;
};

double getXorY(double xy, double r)
{
	double ret2 = r * r - xy * xy;

	return sqrt(ret2);
}

/************************************************************************/
/* 
(x+g, y+g) out of circle r
*/
/************************************************************************/
void getPC(Pologon& p, Chod& c, double x0, double y0, double g, double r)
{
	double x1 = getXorY(y0,r);
	double y1 = getXorY(x0, r);

	if (x1 <= x0 + g && y1 <= y0 + g)
	{
		p.ps.push_back(Point(x0, y0));
		p.ps.push_back(Point(x1, y0));
		p.ps.push_back(Point(x0, y1));

		c.ps.push_back(Point(x1, y0));
		c.ps.push_back(Point(x0, y1));
	}
	else if (x1 <= x0 + g)
	{
		p.ps.push_back(Point(x0, y0));
		p.ps.push_back(Point(x1, y0));

		double tempx = getXorY(y0+g,r);
		p.ps.push_back(Point(tempx, y0+g));

		p.ps.push_back(Point(x0, y0+g));

		c.ps.push_back(Point(x1, y0));
		c.ps.push_back(Point(tempx, y0+g));

	}
	else if (y1 <= y0 + g)
	{
		p.ps.push_back(Point(x0, y0));
		p.ps.push_back(Point(x0 + g, y0));

		double tempy = getXorY(x0 + g, r);
		p.ps.push_back(Point(x0+g, tempy));

		p.ps.push_back(Point(x0, y1));

		c.ps.push_back(Point(x0+g, tempy));
		c.ps.push_back(Point(x0, y1));
	}
	else
	{
		double tempx = getXorY(y0+g, r);
		double tempy = getXorY(x0 + g, r);

		p.ps.push_back(Point(x0, y0));
		p.ps.push_back(Point(x0+g,y0));
		p.ps.push_back(Point(x0+g,tempy));
		p.ps.push_back(Point(tempx,y0+g));
		p.ps.push_back(Point(x0,y0+g));

		c.ps.push_back(Point(x0+g,tempy));
		c.ps.push_back(Point(tempx,y0+g));

	}

}

bool inOronCircle(double x, double y, double r)
{
	return x*x + y*y <= r*r;
}
void getPCs(double sx, double sy, double g, double len, double r, 
			vector<Pologon>&ps, vector<Chod> &cs)
{

	/*cout << "sx = " << sx << endl;
	cout <<"sy = " << sy << endl;
	cout << "g = " << g << endl;
	cout << "len = " << len << endl;
	cout <<"r = " << r << endl;
	*/

	double x = sx;
	double y = sy;

	while (x < r)
	{
		y = sy;
		while (y < r && x*x + y*y < r*r)
		{
			if (inOronCircle(x+g, y+g, r))
			{
				Pologon p;
				p.ps.push_back(Point(x,y));
				p.ps.push_back(Point(x+g,y));
				p.ps.push_back(Point(x+g, y+g));
				p.ps.push_back(Point(x, y+g));

				ps.push_back(p);
			}
			else
			{
				Pologon p;
				Chod c;
				getPC(p, c, x, y, g, r);

				ps.push_back(p);
				cs.push_back(c);
			}

			y+=len+g;		
		}

		x+=len+g;
	}
}


double getPA(Pologon const & p)
{
	vector<Point> v = p.ps;

	int n = p.ps.size();

	v.push_back(v[0]);

	double ret = 0;

	for (int i =0 ;i < n; ++i)
	{
		ret += (v[i].x + v[i+1].x)*(v[i+1].y - v[i].y);
	}

	return ret/2;
}

double dist(Point a, Point b)
{
	double diffx = a.x - b.x;
	double diffy = a.y - b.y;

	return sqrt(diffy*diffy + diffx * diffx);
}

double getCA(Chod c, double r)
{
	Point a = c.ps[0];
	Point b = c.ps[1];

	Point mid((a.x +b.x)/2, (a.y + b.y)/2);

	double h = dist(mid, Point(0,0));
	double be = dist(a, b);

	double area = h * be /2;

	double theta = area * 2 / r /r;

	theta = asin(theta);

	double circleA = r *r * theta /2;

	double ret = circleA - area;

	return ret;
}
//f, R, t, r and g separated by exactly one
int main()
{
	int N;

	cin >> N;
	for (int i = 1; i <= N; ++i)
	{
		double i_f, i_R, i_t, i_r, i_g;
		cin>>i_f >> i_R >> i_t >> i_r >> i_g;

		double r = i_R - i_t - i_f;
		double g = i_g - 2*i_f;
		double len = 2*i_r + 2*i_f;

		double sx = i_r + i_f;
		double sy = sx;

		vector<Pologon> ps;
		vector<Chod> cs;


		getPCs(sx,sy, g, len, r, ps, cs);

		double hole = 0;
		for (int j = 0; j < ps.size(); ++j)
		{
			hole += getPA(ps[j]);
		}

		for (int j = 0; j < cs.size(); ++j)
		{
			hole += getCA(cs[j], r);
		}

		double sCir = PI * i_R * i_R /4;

		double ret = 1 -hole/sCir;

		printf("Case #%d: %0.6f\n", i,ret);



		/*
		//////////////////////////////////////////////////////////////////////////
		for (int j = 0; j < ps.size(); ++j)
		{
		ps[j].print();
		}
		cout << endl << cs.size() << endl; 

		cout <<endl <<"-----------------------" << endl;
		//////////////////////////////////////////////////////////////////////////
		*/

	}
	return 0;
}