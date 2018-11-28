/*
 * $File: prog.cc
 * $Date: Sat May 26 23:29:19 2012 +0800
 * $Author: jiakai <jia.kai66@gmail.com>
 */

// f{{{ 

#include <stdint.h>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <limits>

#define ITER_VECTOR(v, var) \
	for (typeof((v).begin()) var = (v).begin(); var != (v).end(); var ++)

#define ITER_VECTOR_IDX(v, var) \
	for (typeof((v).size()) var = 0; var < (v).size(); var ++)

using namespace std;

// f}}}

namespace Solve
{
	const double G = 3, K = 2, TIME_DELTA = 0.01, DENSITY = 1, EPS = 1e-8;
	const int MAX_SIM = 100000;
	// f{{{ Vector
	struct Vector
	{
		double x, y;

		explicit Vector(double x_ = 0, double y_ = 0):
			x(x_), y(y_)
		{}

		/*!
		 * \brief p0到p1的向量
		 */
		Vector(const Vector &p0, const Vector &p1):
			x(p1.x - p0.x), y(p1.y -p0.y)
		{}

		double cross(const Vector &v) const
		{ return x * v.y - y * v.x; }

		double dot(const Vector &v) const
		{ return x * v.x + y * v.y; }

		Vector operator + (const Vector &v) const
		{ return Vector(x + v.x, y + v.y); }

		Vector& operator += (const Vector &v)
		{ x += v.x; y += v.y; return *this; }

		Vector operator - (const Vector &v) const
		{ return Vector(x - v.x, y - v.y); }

		Vector& operator -= (const Vector &v)
		{ x -= v.x; y -= v.y; return *this; }

		Vector operator * (double f) const
		{ return Vector(x * f, y * f); }

		bool is_zero() const
		{ return fabs(x) < EPS && fabs(y) < EPS; }

		double mod_sqr() const
		{ return x * x + y * y; }

		double mod() const
		{ return sqrt(mod_sqr()); }

		Vector get_normalized() const
		{ double m = mod(); assert(m > EPS); m = 1 / m; return Vector(x * m, y * m); }

		void set_zero() 
		{ x = y = 0; }

		void neg()
		{ x = -x; y = -y; }
	};
	// f}}}
	int width, height;
	double get_rand(double max)
	{ return rand() / (RAND_MAX + 1.0) * max; }
	struct Circle
	{
		Vector a, p, velocity;
		int r;
		double mass;

		bool test_intersect(const Circle &c) const
		{
			return Vector(p, c.p).mod() <= r + c.r + EPS;
		}

		Vector get_force(const Circle &c) const // force on this by c
		{
			Vector pline(p, c.p);
			return pline.get_normalized() * (-G * mass * c.mass / (pline.mod_sqr() + EPS));
		}

		void init()
		{
			p.x = get_rand(width);
			p.y = get_rand(height);
			velocity = Vector();
		}

		Circle() = default;
		Circle(int radius):
			r(radius), mass(M_PI * r * r * DENSITY)
		{
			init();
		}
	};
	vector<Circle> circles;

	bool simulate();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int casenu = 1; casenu <= ncase; casenu ++)
	{
		circles.clear();

		int n;
		fscanf(fin, "%d%d%d", &n, &width, &height);
		while (n --)
		{
			int r;
			fscanf(fin, "%d", &r);
			circles.push_back(Circle(r));
		}
		bool ok = false;
		while (!ok)
		{
			int num = 0;
			for (auto &c: circles)
				c.init();
			ok = true;
			while (!simulate())
			{
				if ((num ++) >= MAX_SIM)
				{
					ok = false;
					break;
				}
			}
			if (!ok)
				fprintf(stderr, "case %d rerun...\n", casenu);
		}
		fprintf(fout, "Case #%d: ", casenu);
		for (auto &c: circles)
			fprintf(fout, "%.5lf %.5lf ", c.p.x, c.p.y);
		fputc('\n', fout);

	}
}

bool Solve::simulate()
{
	bool done = true;
	for (auto &c0: circles)
	{
		Vector fsum(c0.velocity * (-K));
		for (auto &c1: circles)
			if (&c0 != &c1 && c0.test_intersect(c1))
			{
				done = false;
				fsum += c0.get_force(c1);
			}
		c0.a = fsum * (1.0 / c0.mass);
	}
	if (done)
		return true;
	for (auto &c0: circles)
	{
		auto &a = c0.a;
		c0.p += c0.velocity * TIME_DELTA + a * (TIME_DELTA * TIME_DELTA * 0.5);
		c0.velocity += a * TIME_DELTA;
		if (c0.p.x < 0)
			c0.p.x = 0, c0.velocity.neg();
		if (c0.p.y < 0)
			c0.p.y = 0, c0.velocity.neg();
		if (c0.p.x > width)
			c0.p.x = width, c0.velocity.neg();
		if (c0.p.y > height)
			c0.p.y = height, c0.velocity.neg();
	}
	return false;
}

// f{{{ main
int main()
{
#if defined(INPUT) && defined(OUTPUT) && !defined(STDIO) && !defined(ONLINE_JUDGE)
	FILE *fin = fopen(INPUT, "r"),
		 *fout = fopen(OUTPUT, "w");
	Solve::solve(fin, fout);
	fclose(fin);
	fclose(fout);
#else
	Solve::solve(stdin, stdout);
#endif
}
// f}}}
// vim: filetype=cpp foldmethod=marker foldmarker=f{{{,f}}}

