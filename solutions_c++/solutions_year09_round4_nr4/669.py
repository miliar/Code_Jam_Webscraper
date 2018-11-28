#include <iostream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#define ldb long double
#define LL long long
#define sqr(a) (a) * (a)
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-6;
const int INF = 2147483647 / 2;
using namespace std;

class Point
{
	public:
		ldb x, y;
		ldb r;
		Point (){}
		Point (ldb x, ldb y, ldb r) : x(x), y(y), r(r){}
};


bool operator < (const Point &a, const Point &b)
{
	return a.x < b.x - eps || fabs(a.x - b.x) < eps && a.y < b.y - eps || fabs(a.x - b.x) < eps
	&& fabs(a.y - b.y) < eps && a.r < b.r - eps;
}

bool operator == (const Point &a, const Point &b)
{
	return fabs(a.x - b.x) < eps && fabs(a.y - b.y) < eps && (a.r - b.r) < eps;
}

bool operator != (const Point &a, const Point &b)
{
	return !(a == b);
}


vector <Point> all;
int n;
Point p[100];


void Load()
{
	int i;
	int j;
	cin >> n;
	for (i = 1; i <= n; i++)
	{
		cin >> p[i].x >> p[i].y >> p[i].r;
	}
}


inline ldb Distance(const Point &a, const Point &b)
{
	return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
}


int CircleIntersection(const Point &a, const Point &b, ldb rad, Point &p1, Point &p2)
{
	if (Distance(a, b) + a.r + b.r < rad - eps) return 0;
	ldb A = 2 * (b.x - a.x);
	ldb B = 2 * (b.y - a.y);
	ldb C = sqr(a.x) - sqr(b.x) + sqr(a.y) - sqr(b.y) + sqr(rad - b.r) - sqr(rad - a.r);
//	cerr << A << " " << B << " " << C << " ";
	ldb d = sqrt(A * A + B * B);
	A /= d;
	B /= d;
	C /= d;
	ldb t = -(A * a.x + B * a.y + C);
//	cerr << "rad = " << rad - a.r << " " << t << "\n";
	if (fabs(rad - a.r) < fabs(t) - eps)
	{
		return 0;
	}
	if (fabs(sqr(rad - a.r) - sqr(t)) < eps)
	{
		p1.x = a.x + A * t;
		p1.y = a.y + B * t;
//		cerr << "Point at " << p1.x << " " << p1.y << "\n";
		return 1;
	}
	d = sqrt(sqr(rad - a.r) - sqr(t));
	p1.x = a.x + A * t + d * (-B);
	p1.y = a.y + B * t + d * A; 
	p2.x = a.x + A * t - d * (-B);
	p2.y = a.y + B * t - d * A;
	return 2;
}


inline bool CircleIICircle(Point &a, Point &b)
{                         	
//	cerr << Distance(a, b) + a.r << " " << b.r << "\n";
	return Distance(a, b) < b.r + eps && Distance(a, b) + a.r < b.r + eps;
}


int check(ldb rad)
{
	int i, j, k;
	all.clear();

	Point p1, p2;
	int t;
	for (i = 1; i <= n; i++)
	{
		all.push_back(p[i]);
		for (j = i + 1; j <= n; j++)
		{
			t = CircleIntersection(p[i], p[j], rad, p1, p2);	
		//	cerr << i << " " << j << " " << t << "\n";
			if (t == 2)
			{
				all.push_back(p1);
				all.push_back(p2);
			}
			else if (t == 1)
			{
				all.push_back(p1);
			}
		}
	}
	for (i = 0; i < all.size(); i++)
	{
		all[i].r = rad;
	}
//	cerr << "ok";
	sort(all.begin(), all.end());
	all.erase(unique(all.begin(), all.end()), all.end());
//	cerr << "Size = " << all.size() << "\n";
	for (i = 0; i < all.size(); i++)
	{
	//	cerr << all[i].x << " " << all[i].y << " " << all[i].r << "\n";
		for (j = i + 1; j < all.size(); j++)
		{
		
			for (k = 1; k <= n; k++)
			{
				if (!(CircleIICircle(p[k], all[i]) || CircleIICircle(p[k], all[j])))
				{
				//	cerr << "Nea " << i << " " << j << " " << k << "\n";
				//	if (i == 0 && j == 4 && k == 1)
				//	{
				//		cerr << p[k].x << " " << p[k].y << " " << p[k].r << " " << Distance(p[k], all[i]) + p[k].r << " " << all[i].r << "\n";
				//	}
					break;
				}
			}
			if (k == n + 1)
			{
				return 1;
			}
		}
	}
	return 0;
}

void Solve(int Test)
{
	
	cout << "Case #" << Test << ": ";
	if (n == 1)
	{
		cout << p[1].r << "\n";
		return;
	}
	else if (n == 2)
	{
		cout << max(p[1].r, p[2].r) << "\n";
		return;
	}

	int i, q;
	ldb l = 0.0;
	ldb r = 10000.0, res, mid;   
//	cerr << check(9.76563) << "\n";
	
	for (i = 1; i <= 100; i++)
	{
		mid = (l + r) / 2.00;
		q = check(mid);
		if (q == 1)
		{
			r = mid;
			res = r; 
	   	}
	   	else
	   	{
	   		l = mid;
	   	}
	}
	
	
	cout << res << "\n";
}



#define file "d"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(6);
	cin >> T;
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}