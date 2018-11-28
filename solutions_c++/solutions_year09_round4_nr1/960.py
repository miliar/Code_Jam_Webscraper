//#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>
//#include <math.h>
//const double PI = acos(-1.0);
//const double EPS = 1e-8;
//int SGN(double d){ return d > EPS ? 1 : (d < -EPS ? -1 : 0) ; }
//struct Point
//{
//	double x , y;
//	Point(){}
//	Point(double _x , double _y) { x = _x ; y = _y ; }
//	Point operator-(Point &p1) { return Point(x - p1.x , y - p1.y); }
//	double operator*(Point &p1) { return x * p1.y - y * p1.x ; }
//	double operator&(Point p1) { return x * p1.x + y * p1.y ; }
//};
//
//double angle(Point &p1)
//{
//	if (SGN(p1.x))
//	{
//		double tmp = atan(p1.y / p1.x);
//		if (SGN(p1.x) == 1) return (SGN(p1.x) == -1 ? 2 * PI : 0) + tmp;
//		else return tmp + PI;
//	}
//	else
//	{
//		if (SGN(p1.y) == 1) return PI / 2.0;
//		else return PI * 1.5;
//	}
//}
//double r;
//void intersector(Point &p1 , Point &p2 , Point &a1 , Point &a2)
//{
//	double k , b , A , B , C;
//	if (SGN(p1.x - p2.x))
//	{
//		k = (p1.y - p2.y) / (p1.x - p2.x);
//		b = p1.y - k * p1.x;
//		A = k * k + 1;
//		B = 2 * k * b;
//		C = b * b - r * r;
//		double delta = sqrt(B * B - 4 * A * C);
//		a1.x = (- B - delta) / (2.0 * A);
//		a2.x = (- B + delta) / (2.0 * A);
//		a1.y = a1.x * k + b;
//		a2.y = a2.x * k + b;
//	}
//	else
//	{
//		a1.x = a2.x = p1.x;
//		double y = sqrt(r * r - p1.x * p1.x);
//		a1.y = y;
//		a2.y = -y;
//	}
//}
//
//double dis(Point &p1 , Point &p2)
//{
//	return sqrt((p1.x - p2.x)*(p1.x - p2.x)+(p1.y - p2.y)*(p1.y - p2.y));
//}
//double ang(Point &p1 , Point &p2 , Point p0)
//{
//	double a = (p1 - p0) & (p2 - p0) , l1 = dis(p1 , p0) , l2 = dis(p2 , p0);
//	//double tmp = acos(a / (l1 * l2));
//	//if (SGN(tmp - PI) == 0) printf("%lf %lf %lf %lf %lf %lf\n" , p1.x , p1.y , p2.x , p2.y  ,p0.x , p0.y );
//	return acos(a / (l1 * l2));
//}
//
//Point p[200] , a1 , a2;
//int pcnt;
//
//int main()
//{
//	int i , j;
//	double maxn = 0;
//	while (scanf("%d %lf" , &pcnt , &r)!= EOF)
//	{
//		for (i = 0;i < pcnt;i ++)
//			scanf("%lf %lf" , &p[i].x , &p[i].y);
//		maxn = 0;
//		for (i = 0;i < pcnt;i ++)
//		{
//			for (j = i + 1;j < pcnt;j ++)
//			{
//				intersector(p[i] , p[j] , a1 , a2);
//				double t1 = angle(a1) , t2 = angle(a2);
//				//printf("%lf %lf %lf %lf\n" , a1.x , a1.y , a2.x , a2.y);
//				if (t1 > t2){ double t = t1; t1 = t2; t2 = t; }
//				if (t2 - t1 > PI) { double t = t2 , t2 = t1 , t1 = t2 - 2 * PI; }
//				//printf("%lf %lf\n" , t1 , t2);
//				double ans , m1 , m2 , tm1 , tm2;
//
//				while (SGN(t2 - t1) == 1)
//				{
//					m1 = (t2 + t1) / 2.0;
//					m2 = (m1 + t2) / 2.0;
//					tm1 = ang(p[i] , p[j] , Point(r * cos(m1) , r * sin(m1)));
//					tm2 = ang(p[i] , p[j] , Point(r * cos(m2) , r * sin(m2)));
//					if (tm1 > tm2) t2 = m2 - EPS;
//					else t1 = m1 + EPS;
//				}
//				ans = ang(p[i] , p[j] , Point(r * cos(t1) , r * sin(t1)));
//				if (ans > maxn) maxn = ans;
//			}
//		}
//		printf("%.10lf\n" , maxn);
//	}
//	return 0;
//}


#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char a[61][61];
int num[61];
bool hash[61];
int b[61];
int n;
int t;

int main()
{
	int i , j,  k , t;
	freopen("C:\\Documents and Settings\\Mad@Frog\\桌面\\黑白棋\\新建文件夹\\A-large.in" , "r" , stdin);
	freopen("C:\\Documents and Settings\\Mad@Frog\\桌面\\黑白棋\\新建文件夹\\A-large.out" , "w" , stdout);
	scanf("%d" , &t);
	
	for (k = 1;k <= t;k ++)
	{
		memset(num , 0  ,sizeof(num));
		memset(hash , 0 , sizeof(hash));
		scanf("%d" , &n);
		for (i = 0;i < n;i ++)
			b[i] = n - 1 - i;
		for (i = 0;i < n;i ++)
			scanf("%s" , a[i]);
		for (i = 0;i < n;i ++)
			for (j = n - 1;j >= 0;j --)
			{
				if (a[i][j] == '1') break;
				num[i] ++;
			}
		int ans = 0;
		for (i = 0;i < n;i ++)
		{
			if (num[i] >= b[i]) continue;
			
			for (j = i + 1;j < n;j ++)
			{
				if (num[j] >= b[i]) break;
			}
			for (j = j;j > i;j --)
			{
				num[j] = num[j - 1];
				ans ++;
			}
		}
		printf("Case #%d: %d\n" , k , ans);
	}
}