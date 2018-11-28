#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#pragma warning (disable: 4996)

using namespace std;

struct pt { double x[3]; };
struct op { double a[3][3]; };
struct tri { pt p[3]; };

pt mulp(op & t, pt & p)
{
	pt x = { { 0, 0, 0 } };
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			x.x[i] += t.a[i][j] * p.x[j];
	return x;
}

op mult(op & t, op & a)
{
	op x = { { { 0, 0, 0 }, { 0, 0, 0 }, { 0, 0, 0 } } };
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			for (int k = 0; k < 3; k++)
				x.a[i][j] += t.a[i][k] * a.a[k][j];
	return x;
}

int main()
{
	int ncase;
	scanf("%d", & ncase);
	for (int cas = 1; cas <= ncase; cas++)
	{
		tri a, b;
		scanf("%lf %lf %lf %lf %lf %lf",
			& a.p[0].x[0], & a.p[0].x[1], 
			& a.p[1].x[0], & a.p[1].x[1], 
			& a.p[2].x[0], & a.p[2].x[1]);
		scanf("%lf %lf %lf %lf %lf %lf",
			& b.p[0].x[0], & b.p[0].x[1], 
			& b.p[1].x[0], & b.p[1].x[1], 
			& b.p[2].x[0], & b.p[2].x[1]);
		a.p[0].x[2] = a.p[1].x[2] = a.p[2].x[2] = 1;
		b.p[0].x[2] = b.p[1].x[2] = b.p[2].x[2] = 1;

		op tr = { { {1, 0, 0}, {0, 1, 0}, {0, 0, 1} } };
		op t1 = { { {1, 0, -b.p[0].x[0]}, {0, 1, -b.p[0].x[1]}, {0, 0, 1} } };
		op t2 = { { {1, 0, b.p[0].x[0]}, {0, 1, b.p[0].x[1]}, {0, 0, 1} } };
		op t3 = { { {1, 0, -a.p[0].x[0]}, {0, 1, -a.p[0].x[1]}, {0, 0, 1} } };
		tr = mult(t3, tr);
		b.p[0] = mulp(t1, b.p[0]);
		b.p[1] = mulp(t1, b.p[1]);
		b.p[2] = mulp(t1, b.p[2]);
		a.p[0] = mulp(t3, a.p[0]);
		a.p[1] = mulp(t3, a.p[1]);
		a.p[2] = mulp(t3, a.p[2]);

		double da = sqrt((a.p[0].x[0] - a.p[1].x[0])*(a.p[0].x[0] - a.p[1].x[0]) + (a.p[0].x[1] - a.p[1].x[1])*(a.p[0].x[1] - a.p[1].x[1]));
		double db = sqrt((b.p[0].x[0] - b.p[1].x[0])*(b.p[0].x[0] - b.p[1].x[0]) + (b.p[0].x[1] - b.p[1].x[1])*(b.p[0].x[1] - b.p[1].x[1]));
		op s1 = { { {1/db, 0, 0}, {0, 1/db, 0}, {0, 0, 1} } };
		op s2 = { { {db, 0, 0}, {0, db, 0}, {0, 0, 1} } };
		op s3 = { { {1/da, 0, 0}, {0, 1/da, 0}, {0, 0, 1} } };
		tr = mult(s3, tr);
		b.p[0] = mulp(s1, b.p[0]);
		b.p[1] = mulp(s1, b.p[1]);
		b.p[2] = mulp(s1, b.p[2]);
		a.p[0] = mulp(s3, a.p[0]);
		a.p[1] = mulp(s3, a.p[1]);
		a.p[2] = mulp(s3, a.p[2]);

		double sina = a.p[1].x[1];
		double cosa = a.p[1].x[0];
		double sinb = b.p[1].x[1];
		double cosb = b.p[1].x[0];
		op r1 = { { {cosb, sinb, 0}, {-sinb, cosb, 0}, {0, 0, 1}}};
		op r2 = { { {cosb, -sinb, 0}, {sinb, cosb, 0}, {0, 0, 1}}};
		op r3 = { { {cosa, sina, 0}, {-sina, cosa, 0}, {0, 0, 1}}};
		tr = mult(r3, tr);
		b.p[0] = mulp(r1, b.p[0]);
		b.p[1] = mulp(r1, b.p[1]);
		b.p[2] = mulp(r1, b.p[2]);
		a.p[0] = mulp(r3, a.p[0]);
		a.p[1] = mulp(r3, a.p[1]);
		a.p[2] = mulp(r3, a.p[2]);

		tr = mult(r2, tr);
		tr = mult(s2, tr);
		tr = mult(t2, tr);
		
		double x0 = tr.a[0][2];
		double y0 = tr.a[1][2];
		while (true)
		{
			tr = mult(tr, tr);
			if (fabs(tr.a[0][0]) + fabs(tr.a[0][1]) + fabs(tr.a[1][0]) + fabs(tr.a[1][1]) < 1e-20)
				break;
			x0 = tr.a[0][2];
			y0 = tr.a[1][2];
		}
		x0 = tr.a[0][2];
		y0 = tr.a[1][2];

		printf("Case #%d: %.6f %.6f\n", cas, x0, y0);
		/*
		printf("%.3f %.3f %.3f\n%.3f %.3f %.3f\n%.3f %.3f %.3f\n",
			tr.a[0][0], tr.a[0][1], tr.a[0][2], 
			tr.a[1][0], tr.a[1][1], tr.a[1][2], 
			tr.a[2][0], tr.a[2][1], tr.a[2][2]);
		printf("%.3f %.3f %.3f\n%.3f %.3f %.3f\n%.3f %.3f %.3f\n",
			b.p[0].x[0], b.p[0].x[1], b.p[0].x[2],
			b.p[1].x[0], b.p[1].x[1], b.p[1].x[2],
			b.p[2].x[0], b.p[2].x[1], b.p[2].x[2]);
		*/
	}

	return 0;
}
