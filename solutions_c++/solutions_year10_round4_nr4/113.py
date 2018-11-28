#include <iostream>  
#include <vector>  
#include <cmath>  
#include <cstdio>  

using namespace std;

#define pi acos(-1.0)
#define sqr(x) ((x) * (x))
#define dis2(a, b) (sqrt(sqr(a.x - b.x) + sqr(a.y - b.y)))

struct point
{
	double x, y;
};

struct circle
{
	point c;
	double r;
};

double IntersectionArea(circle cir1, circle cir2)
{  
	double A1, A2, d, ang1, ang2;
	circle ctmp;
	if (cir1.r < cir2.r)  
	{  
		ctmp = cir1;
		cir1 = cir2;
		cir2 = ctmp;	
	}
	double ret = 0;  
	A1 = pi * sqr(cir1.r);  
	A2 = pi * sqr(cir2.r);  
	d = dis2(cir1.c, cir2.c);

	if (d >= cir1.r + cir2.r) return 0;  
	if (d <= cir1.r - cir2.r) return A2;  

	ang1 = acos((sqr(cir1.r)+ sqr(d) - sqr(cir2.r)) / 2 / cir1.r/ d);  
	ang2 = acos((sqr(cir2.r)+ sqr(d) - sqr(cir1.r)) / 2 / cir2.r/ d);  

	ret -= sqr(cir1.r) * ang1 - sqr(cir1.r) * sin(ang1) * cos(ang1);
	ret -= sqr(cir2.r) * ang2 - sqr(cir2.r) * sin(ang2) * cos(ang2); 
	return -ret;
} 

int main()
{
	int cases;
	cin >> cases;
	for (int cur = 1; cur <= cases; cur++) {
		int n, m;
		cin >> n >> m;
		if (n != 2) {
			cerr << "ERROR!, N should be 2" << endl;
			break;
		}
		vector<point> p(n);
		vector<point> q(m);
		for (int i = 0; i < n; i++)
			cin >> p[i].x >> p[i].y;
		for (int i = 0; i < m; i++)
			cin >> q[i].x >> q[i].y;
		vector<double> area(m);
		for (int i = 0; i < m; i++) {
			circle cir1, cir2;
			cir1.c = p[0];
			cir2.c = p[1];
			cir1.r = dis2(cir1.c, q[i]);
			cir2.r = dis2(cir2.c, q[i]);
			area[i] = IntersectionArea(cir1, cir2);
		}
		printf("Case #%d:", cur);
		for (int i = 0; i < m; i++)
			printf(" %.7f", area[i]);
		printf("\n");
	}
	return 0;
}
