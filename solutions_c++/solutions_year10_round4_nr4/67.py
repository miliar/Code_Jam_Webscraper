class Line
{
public:
	Point p1, p2;
	Line() {} 
	Line(long double a, long double b, long double c);
	Line(const Point &a, const Point &b) { p1 = a; p2 = b; }
	void BuildEq(long double &a, long double &b, long double &c);
};

class Circle : public Point
{
public:
	long double r;
	Circle(long double a, long double b, long double c)
	{
		x = a;
		y = b;
		r = c;
	}
	Circle()
	{
	}
};

class Segment : public Line
{
public:
	Segment() {}
	Segment(const Point &a, const Point &b) { p1 = a; p2 = b; }
};

int Intersect(const Line &a, const Line &b, Point &r);
int Intersect(const Line &a, const Circle &b, Point &r1, Point &r2);
int Intersect(const Circle &a, const Circle &b, Point &r1, Point &r2);
int Intersect(const Segment &a, const Segment &b, Point &r);
int Intersect(const Segment &a, const Circle &b, Point &r1, Point &r2);

Line::Line(long double a, long double b, long double c)
{
	if (fabs(a) < eps)
	{
		if (fabs(b) < eps) throw "botva";
		p1.x = 0;
		p1.y = -c / b;
	}
	else
	{
		p1.y = 0;
		p1.x = -c / a;
	}
	p2.x = p1.x - b;
	p2.y = p1.y + a;
}

void Line::BuildEq(long double &a, long double &b, long double &c)
{
	a = p1.y - p2.y;
	b = p2.x - p1.x;
	c = -a * p1.x - b * p1.y;
}

int Intersect(const Line &a, const Line &b, Point &r)
{
	long double a1, b1, c1, a2, b2, c2;
	a1 = a.p2.y - a.p1.y;
	b1 = -(a.p2.x - a.p1.x);
	c1 = a1 * a.p1.x + b1 * a.p1.y;
	a2 = b.p2.y - b.p1.y;
	b2 = -(b.p2.x - b.p1.x);
	c2 = a2 * b.p1.x + b2 * b.p1.y;
	long double d = a1 * b2 - b1 * a2;
	if (fabs(d) < eps) return 0;
	r.x = (c1 * b2 - b1 * c2) / d;
	r.y = (a1 * c2 - c1 * a2) / d;
	return 1;
}

void BuildPerpendicular(const Point &p, const Line &a, Point &r)
{
	Line b;
	b.p1 = p;
	b.p2.x = p.x + (a.p2.y - a.p1.y);
	b.p2.y = p.y - (a.p2.x - a.p1.x);
	Intersect(a, b, r);
}

int Intersect(const Line &a, const Circle &b, Point &r1, Point &r2)
{
	long double aa, bb, cc;
	aa = (a.p2.x - a.p1.x) * (a.p2.x - a.p1.x) + (a.p2.y - a.p1.y) * (a.p2.y - a.p1.y);
	bb = 2 * (a.p2.x - a.p1.x) * (a.p1.x - b.x) + 2 * (a.p2.y - a.p1.y) * (a.p1.y - b.y);
	cc = (a.p1.x - b.x) * (a.p1.x - b.x) + (a.p1.y - b.y) * (a.p1.y - b.y) - b.r * b.r; 
	long double d = bb * bb - 4 * aa * cc;
	if (d < -eps) return 0;
	long double t1, t2;
	int r;
	if (d < eps)
	{
		r = 1;
		t1 = t2 = -bb / (2 * aa);
	}
	else
	{
		d = sqrt(d);
		r = 2;
		t1 = (-bb - d) / (2 * aa);
		t2 = (-bb + d) / (2 * aa);
	}
	r1.x = a.p1.x + t1 * (a.p2.x - a.p1.x);
	r1.y = a.p1.y + t1 * (a.p2.y - a.p1.y);
	r2.x = a.p1.x + t2 * (a.p2.x - a.p1.x);
	r2.y = a.p1.y + t2 * (a.p2.y - a.p1.y);
	return r;
}

int Intersect(const Circle &a, const Circle &b, Point &r1, Point &r2)
{
	long double d = Dist(a, b);
	if (d > a.r + b.r + eps) return 0;
	if (a.r > b.r + d + eps) return 0;
	if (b.r > a.r + d + eps) return 0;
	long double aa, bb, cc;
	aa = -2 * a.x + 2 * b.x;
	bb = -2 * a.y + 2 * b.y;
	cc = a.x * a.x + a.y * a.y - b.x * b.x - b.y * b.y - a.r * a.r + b.r * b.r;
	return Intersect(Line(aa, bb, cc), a, r1, r2);
}

int Intersect(const Segment &a, const Segment &b, Point &r)
{
	long double a1, b1, c1, a2, b2, c2;
	a1 = (a.p2.x - a.p1.x);
	b1 = -(b.p2.x - b.p1.x);
	c1 = b.p1.x - a.p1.x;
	a2 = (a.p2.y - a.p1.y);
	b2 = -(b.p2.y - b.p1.y);
	c2 = b.p1.y - a.p1.y;
	long double d = a1 * b2 - b1 * a2;
	if (fabs(d) < eps) return 0;
	long double t1 = (c1 * b2 - b1 * c2) / d;
	long double t2 = (a1 * c2 - c1 * a2) / d;
	if (t1 < -eps || t1 > 1 + eps) return 0;
	if (t2 < -eps || t2 > 1 + eps) return 0;
	r.x = a.p1.x + t1 * (a.p2.x - a.p1.x);
	r.y = a.p1.y + t1 * (a.p2.y - a.p1.y);
	return 1;
}

int Intersect(const Segment &a, const Circle &c, Point &rp1, Point &rp2)
{
	int t = Intersect((const Line&)a, c, rp1, rp2);
	int ans = 0;
	Point sp1, sp2;
	sp1 = a.p1;
	sp2 = a.p2;
//	long double d = max(max(fabs(sp1.x), fabs(sp1.y)), max(fabs(sp2.x), fabs(sp2.y)));
//	d = 1.0 / d;
//	d *= d;
	if (t > 0)
	{
		if ((a.p1 - rp1) * (a.p2 - rp1) < -eps) ans++;
	}
	if (t > 1)
	{
		if ((a.p1 - rp2) * (a.p2 - rp2) < -eps) 
		{
			if (ans == 0) rp1 = rp2;
			ans++;
	    }
	}
	return ans;
}
