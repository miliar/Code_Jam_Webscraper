/* 
 * Problem: Google Code Jam 2010 Round 2 Grazing Google Goats
 * Author: BYVoid (郭家寶 Guo Jiabao)
 * Time: 2010.6.5 23:44
 * State: Solved
 * Memo: 兩圓面積交
*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#define MATH_PI acos(-1)
using namespace std;

const int MAXN = 12,MAXM = 12;

struct point
{
    double x, y;
}P[MAXN];

double Answer;

double dis_point(point p1, point p2)
{
    double x1 = p1.x - p2.x;
    double y1 = p1.y - p2.y;
    return sqrt(x1 * x1 + y1 * y1);
}

double squares(double r)
{
    return MATH_PI * r * r;
}

double cosine(double b1, double b2, double b3)
{
    double b = b2 * b2 + b3 * b3 - b1 * b1;
    return b / b2 / b3 / 2;
}

void calc(point c1,double r1,point c2,double r2)
{
	double d, ssq, sqr_1, sqr_2;
	double a1, a2, ang1, ang2;
	d = dis_point(c1, c2);
	sqr_1 = squares(r1);
	sqr_2 = squares(r2);
	ssq = sqr_1 + sqr_2;
	if (d >= r1 + r2)
		Answer = 0;
	else if(d <= r1 - r2 && r1 > r2)
		Answer = sqr_2;
	else if(d <= r2 - r1 && r1 < r2)
		Answer = sqr_1;
	else
	{
		a1 = cosine(r2, r1, d);
		a2 = cosine(r1, r2, d);
		ang1 = acos(a1);
		ang2 = acos(a2);
		if(a1 > 0)
			ssq -= (sqr_1 * ang1 / MATH_PI - r1 * r1 * sin(ang1 * 2) / 2); 
		else
			ssq -= (sqr_1 * ang1 / MATH_PI + r1 * r1 * sin((MATH_PI - ang1) * 2) / 2); 
		if(a2 > 0)
			ssq -= (sqr_2 * ang2 / MATH_PI - r2 * r2 * sin(ang2 * 2) / 2);
		else
			ssq -= (sqr_2 * ang2 / MATH_PI + r2 * r2 * sin((MATH_PI - ang2) * 2) / 2);
		Answer = sqr_1 + sqr_2 - ssq;
	}
}

void solve()
{
	int i,N,M;
	scanf("%d%d",&N,&M);
	for (i=1;i<=N;i++)
	{
		scanf("%lf%lf",&P[i].x,&P[i].y);
	}
	for (i=1;i<=M;i++)
	{
		point Q;
		double r1,r2;
		scanf("%lf%lf",&Q.x,&Q.y);
		r1 = dis_point(P[1],Q);
		r2 = dis_point(P[2],Q);
		calc(P[1],r1,P[2],r2);
		printf("%.7lf",Answer);
		if (i < M)
			printf(" ");
		else
			printf("\n");
	}
	
}

int main()
{
	int T;
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
