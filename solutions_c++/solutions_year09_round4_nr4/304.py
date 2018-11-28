#include <stdio.h>
#include <math.h>
#include <algorithm>
//#define DEBUG
using namespace std;
typedef double LD;

struct Circle
{
	LD x, y;
	LD r;

	void Read()
	{
		scanf("%lf%lf%lf", &x, &y, &r);
	}
	bool Inside(const Circle& p) const
	{
		return Dist2(*this, p) <= (p.r-r)*(p.r-r);
	}
	friend int Dist2(const Circle& p, const Circle& q)
	{
		return (p.x-q.x)*(p.x-q.x) + (p.y-q.y)*(p.y-q.y);
	}
};


int n;
Circle p[64];

bool Calc(const Circle& c1, const Circle& c2, LD R, Circle& ans1, Circle& ans2)
{
	LD x1 = c1.x;
	LD x2 = c2.x;
	LD y1 = c1.y;
	LD y2 = c2.y;
	x2 -= x1;
	y2 -= y1;
	LD r1 = R-c1.r;
	LD r2 = R-c2.r;

	if (fabs(y2) < 1e-8)
	{
		LD x = (x2*x2 + r1*r1 - r2*r2)/2/x2;
		LD d = r1*r1 - x*x;
		if (d < -1e-8) return false;
		if (d <= 0.0) d = 0.0;
		ans1.x = ans2.x = x;
		ans1.y = -sqrt(d);
		ans2.y = +sqrt(d);
//		printf("%%");
	}
	else
	{
		LD z = (x2*x2 + y2*y2 + r1*r1 - r2*r2)/2;
		LD p = -x2/y2;
		LD q = z/y2;
		LD a = 1+p*p;
		LD b = p*q;
		LD c = q*q - r1*r1;
		LD d = b*b-a*c;
//	printf("*** D=%.7lf\n", d);
//	printf("*** X2=%.7lf\n", x2);
//	printf("*** A=%.7lf B=%.7lf C=%.7lf\n", a, b, c);
//	printf("*** Z=%.7lf P=%.7lf Q=%.7lf\n", z, p, q);

		if (d < -1e-8) return false;
		if (d <= 0.0) d = 0.0;
		ans1.x = (-b-sqrt(d))/a;
		ans2.x = (-b+sqrt(d))/a;
		ans1.y = p*ans1.x + q;
		ans2.y = p*ans2.x + q;
//		printf("!");
	}

	ans1.x += x1;
	ans1.y += y1;
	ans2.x += x1;
	ans2.y += y1;
	ans1.r = R;
	ans2.r = R;

//	printf("*** R=%.7lf x=%.7lf y=%.7lf\n", R, ans1.x, ans1.y);
//	printf("*** R=%.7lf x=%.7lf y=%.7lf\n", R, ans2.x, ans2.y);
	
	return true;
}

bool Can(LD R)
{
	for (int i=0; i<n; i++)
		if (p[i].r > R) return false;

	for (int i=0; i<n; i++)
	{
		for (int j=i+1; j<n; j++)
		{
			Circle c[2];
			if (Calc(p[i], p[j], R, c[0], c[1]))
			{
				for (int cc=0; cc<2; cc++)
				{
					int cnt = 0;
					for (int k=0; k<n; k++)
						if (!p[k].Inside(c[cc]))
							cnt++;
					if (cnt <= 1)
					{
#ifdef DEBUG
						printf("R=%.7lf cnt=%d i=%d j=%d\n", R, cnt, i, j);
#endif
						return true;
					}


					for (int i1=0; i1<n; i1++)
					{
						for (int j1=i1+1; j1<n; j1++)
						{
							Circle c1[2];
							if (Calc(p[i1], p[j1], R, c1[0], c1[1]))
							{
								for (int cc1=0; cc1<2; cc1++)
								{
									for (int l=0; l<n; l++)
										if (!p[l].Inside(c[cc]) && !p[l].Inside(c1[cc1])) break;
									if (l == n)
									{
#ifdef DEBUG
										printf("R=%.7lf i=%d j=%d\n", R, i1, j1);
#endif

										return true;
									}
								}
							}
						}
					}
				}
			}
		}
	}
	return false;
}

LD Solve()
{
	scanf("%d", &n);
	for (int i=0; i<n; i++)
		p[i].Read();

	if (n == 1)
		return p[0].r;
	if (n == 2)
		return max(p[0].r, p[1].r);


//	Circle c1, c2;
//	Calc(p[0], p[1], 12, c1, c2);
//	return 0.0;


	LD l = 0.5;
	LD r = 1e10;
	while (r-l > 1e-6)
	{
		LD c = (l+r)/2;
		if (Can(c))
			r = c;
		else
			l = c;
	}
	return l;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i=1; i<=t; i++)
	{
		printf("Case #%d: %.6lf\n", i, Solve());
	}
	return 0;
}
