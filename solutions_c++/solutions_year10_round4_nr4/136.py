#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

//typedef double TYPE;
//
//#define Abs(x) (((x)>0)?(x):(-(x)))
//#define Sgn(x) (((x)<0)?(-1):(1))
//#define Max(a,b) (((a)>(b))?(a):(b))
//#define Min(a,b) (((a)<(b))?(a):(b))
//
//#define Epsilon 1e-10
//#define Infinity 1e+10
//#define Pi 3.14159265358979323846
//
//TYPE Deg2Rad(TYPE deg)
//{
//	return (deg * Pi / 180.0);
//}
//
//TYPE Rad2Deg(TYPE rad)
//{
//	return (rad * 180.0 / Pi);
//}
//
//TYPE Sin(TYPE deg)
//{
//	return sin(Deg2Rad(deg));
//}
//
//TYPE Cos(TYPE deg)
//{
//	return cos(Deg2Rad(deg));
//}
//
//TYPE ArcSin(TYPE val)
//{
//	return Rad2Deg(asin(val));
//}
//
//TYPE ArcCos(TYPE val)
//{
//	return Rad2Deg(acos(val));
//}
//
//TYPE Sqrt(TYPE val)
//{
//	return sqrt(val);
//}
//
//struct POINT
//{
//	TYPE x;
//	TYPE y;
//	TYPE z;
//	POINT() : x(0), y(0), z(0) {};
//	POINT(TYPE _x_, TYPE _y_, TYPE _z_ = 0) : x(_x_), y(_y_), z(_z_) {};
//};
//
//// cross product of (o->a) and (o->b)
//// 叉乘
//TYPE Cross(const POINT & a, const POINT & b, const POINT & o)
//{
//	return (a.x - o.x) * (b.y - o.y) - (b.x - o.x) * (a.y - o.y);
//}
//
//// planar points' distance
//// 两个点的距离
//TYPE Distance(const POINT & a, const POINT & b)
//{
//	return Sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y) +
//		(a.z - b.z) * (a.z - b.z));
//}
//
//struct LINE
//{
//	POINT a;
//	POINT b;
//	LINE() {};
//	LINE(POINT _a_, POINT _b_) : a(_a_), b(_b_) {};
//};
//
//// 返回直线 Ax + By + C =0 的系数
//void Coefficient(const LINE & L, TYPE & A, TYPE & B, TYPE & C)
//{
//	A = L.b.y - L.a.y;
//	B = L.a.x - L.b.x;
//	C = L.b.x * L.a.y - L.a.x * L.b.y;
//}
//
//void Coefficient(const POINT & p,const TYPE a,TYPE & A,TYPE & B,TYPE & C)
//{
//	A = Cos(a);
//	B = Sin(a);
//	C = - (p.y * B + p.x * A);
//}
//
//// 线段
//struct SEG
//{
//	POINT a;
//	POINT b;
//	SEG() {};
//	SEG(POINT _a_, POINT _b_):a(_a_),b(_b_) {};
//};
//
//// 圆
//struct CIRCLE
//{
//	TYPE x;
//	TYPE y;
//	TYPE r;
//	CIRCLE() {}
//	CIRCLE(TYPE _x_, TYPE _y_, TYPE _r_) : x(_x_), y(_y_), r(_r_) {}
//};
//
//POINT Center(const CIRCLE & circle)
//{
//	return POINT(circle.x, circle.y);
//}
//
//TYPE Area(const CIRCLE & circle)
//{       
//	return Pi * circle.r * circle.r;
//}
////两个圆的公共面积
//TYPE CommonArea(const CIRCLE & A, const CIRCLE & B)
//{
//	TYPE area = 0.0;
//
//	const CIRCLE & M = (A.r > B.r) ? A : B;
//	const CIRCLE & N = (A.r > B.r) ? B : A;
//
//	TYPE D = Distance(Center(M), Center(N));
//
//	if ((D < M.r + N.r) && (D > M.r - N.r))
//	{
//		TYPE cosM = (M.r * M.r + D * D - N.r * N.r) / (2.0 * M.r * D);
//		TYPE cosN = (N.r * N.r + D * D - M.r * M.r) / (2.0 * N.r * D);
//
//		TYPE alpha = 2.0 * ArcCos(cosM);
//		TYPE beta = 2.0 * ArcCos(cosN);
//
//		TYPE TM = 0.5 * M.r * M.r * Sin(alpha);
//		TYPE TN = 0.5 * N.r * N.r * Sin(beta);
//
//		TYPE FM = (alpha / 360.0) * Area(M);
//		TYPE FN = (beta / 360.0) * Area(N);
//
//		area = FM + FN - TM - TN;
//	}
//	else if (D <= M.r - N.r)
//	{
//		area = Area(N);
//	}
//
//	return area;
//}
//
//// 矩形
////矩形的线段
////        2
////   --------------- b
////   |             |
//// 3 |             | 1
//// a ---------------
////         0
//
//struct RECT
//{
//	POINT a;                                   // 左下点
//	POINT b;                                   // 右上点
//	RECT() {};
//	RECT(const POINT & _a_, const POINT & _b_)
//	{
//		a = _a_;
//		b = _b_;
//	}
//};
//
////根据下标返回多边形的边
//SEG Edge(const RECT & rect, int idx)
//{
//	SEG edge;
//	while (idx < 0) idx += 4;
//	switch (idx % 4)
//	{
//	case 0:
//		edge.a = rect.a;
//		edge.b = POINT(rect.b.x, rect.a.y);
//		break;
//	case 1:
//		edge.a = POINT(rect.b.x, rect.a.y);
//		edge.b = rect.b;
//		break;
//	case 2:
//		edge.a = rect.b;
//		edge.b = POINT(rect.a.x, rect.b.y);
//		break;
//	case 3:
//		edge.a = POINT(rect.a.x, rect.b.y);
//		edge.b = rect.a;
//		break;
//	default:
//		break;
//	}
//	return edge;
//}
//
//TYPE Area(const RECT & rect)
//{
//	return (rect.b.x - rect.a.x) * (rect.b.y - rect.a.y);
//}
//// 两个矩形的公共面积
//TYPE CommonArea(const RECT & A, const RECT & B)
//{
//	TYPE area = 0.0;
//
//	POINT LL(Max(A.a.x, B.a.x), Max(A.a.y, B.a.y));
//	POINT UR(Min(A.b.x, B.b.x), Min(A.b.y, B.b.y));
//
//	if ((LL.x <= UR.x) && (LL.y <= UR.y))
//	{
//		area = Area(RECT(LL, UR));
//	}
//
//	return area;
//}
//
//
//// 多边形 ,逆时针或顺时针给出x,y
//struct POLY
//{
//	int n;        //n个点
//	TYPE * x;     //x,y为点的指针，首尾必须重合
//	TYPE * y;
//	POLY() : n(0), x(NULL), y(NULL) {};
//	POLY(int _n_, const TYPE * _x_, const TYPE * _y_)
//	{        
//		n = _n_;
//
//		x = new TYPE[n + 1];
//		memcpy(x, _x_, n*sizeof(TYPE));
//		x[n] = _x_[0];
//
//		y = new TYPE[n + 1];
//		memcpy(y, _y_, n*sizeof(TYPE));
//		y[n] = _y_[0];
//	}
//};
////多边形顶点
//POINT Vertex(const POLY & poly, int idx)
//{
//	idx %= poly.n;
//	return POINT(poly.x[idx], poly.y[idx]);
//}
////多边形的边
//SEG Edge(const POLY & poly, int idx)
//{
//	idx %= poly.n;
//	return SEG(POINT(poly.x[idx], poly.y[idx]),
//		POINT(poly.x[idx + 1], poly.y[idx + 1]));
//}
//
//
//
//
////多边形的周长
//TYPE Perimeter(const POLY & poly)
//{
//	TYPE p = 0.0;
//	for (int i = 0; i < poly.n; i++)
//		p = p + Distance(Vertex(poly, i), Vertex(poly, i + 1));
//	return p;
//}
//
//bool IsEqual(TYPE a, TYPE b)
//{
//	return (Abs(a - b) < Epsilon);
//}
//
//bool IsEqual(const POINT & a, const POINT & b)
//{
//	return (IsEqual(a.x, b.x) && IsEqual(a.y, b.y));
//}
//
//bool IsEqual(const LINE & A, const LINE & B)
//{
//	TYPE A1, B1, C1;
//	TYPE A2, B2, C2;
//
//	Coefficient(A, A1, B1, C1);
//	Coefficient(B, A2, B2, C2);
//
//	return IsEqual(A1 * B2, A2 * B1) &&
//		IsEqual(A1 * C2, A2 * C1) &&
//		IsEqual(B1 * C2, B2 * C1);
//}
//
//// 判断点是否在线段上
//bool IsOnSeg(const SEG & seg, const POINT & p)
//{
//	return (IsEqual(p, seg.a) || IsEqual(p, seg.b)) ||
//		(((p.x - seg.a.x) * (p.x - seg.b.x) < 0 ||
//		(p.y - seg.a.y) * (p.y - seg.b.y) < 0) &&
//		(IsEqual(Cross(seg.b, p, seg.a), 0)));
//}
////判断两条线断是否相交，端点重合算相交
//bool IsIntersect(const SEG & u, const SEG & v)
//{
//	return (Cross(v.a, u.b, u.a) * Cross(u.b, v.b, u.a) >= 0) &&
//		(Cross(u.a, v.b, v.a) * Cross(v.b, u.b, v.a) >= 0) &&
//		(Max(u.a.x, u.b.x) >= Min(v.a.x, v.b.x)) &&
//		(Max(v.a.x, v.b.x) >= Min(u.a.x, u.b.x)) &&
//		(Max(u.a.y, u.b.y) >= Min(v.a.y, v.b.y)) &&
//		(Max(v.a.y, v.b.y) >= Min(u.a.y, u.b.y));
//}
//
////判断两条线断是否平行
//bool IsParallel(const LINE & A, const LINE & B)
//{
//	TYPE A1, B1, C1;
//	TYPE A2, B2, C2;
//
//	Coefficient(A, A1, B1, C1);
//	Coefficient(B, A2, B2, C2);
//
//	return (A1 * B2 == A2 * B1) &&
//		((A1 * C2 != A2 * C1) || (B1 * C2 != B2 * C1));
//}
////判断两条直线断是否相交
//bool IsIntersect(const LINE & A, const LINE & B)
//{
//	return !IsParallel(A, B);
//}
////直线相交的交点
//POINT Intersection(const LINE & A, const LINE & B)
//{
//	TYPE A1, B1, C1;
//	TYPE A2, B2, C2;
//
//	Coefficient(A, A1, B1, C1);
//	Coefficient(B, A2, B2, C2);
//
//	POINT I(0, 0);
//
//	I.x = - (B2 * C1 - B1 * C2) / (A1 * B2 - A2 * B1);
//	I.y =   (A2 * C1 - A1 * C2) / (A1 * B2 - A2 * B1);
//
//	return I;
//}
//
//
//bool IsInCircle(const CIRCLE & circle, const RECT & rect)
//{
//	return (circle.x - circle.r >= rect.a.x) &&
//		(circle.x + circle.r <= rect.b.x) &&
//		(circle.y - circle.r >= rect.a.y) &&
//		(circle.y + circle.r <= rect.b.y);
//}
//
////判断是否简单多边形
//bool IsSimple(const POLY & poly)
//{
//	if (poly.n < 3)
//		return false;
//	SEG L1, L2;
//	for (int i = 0; i < poly.n - 1; i++)
//	{
//		L1 = Edge(poly, i);
//		for (int j = i + 1; j < poly.n; j++)
//		{
//			L2 = Edge(poly, j);
//			if (j == i + 1)
//			{
//				if (IsOnSeg(L1, L2.b) || IsOnSeg(L2, L1.a))
//					return false;                               
//			}
//			else if (j == poly.n - i - 1)
//			{
//				if (IsOnSeg(L1, L2.a) || IsOnSeg(L2, L1.b))
//					return false;                               
//			}
//			else
//			{
//				if (IsIntersect(L1, L2))
//					return false;
//			}
//		} // for j
//	} // for i
//	return true;
//}
//
////求多边形面积
//TYPE Area(const POLY & poly)
//{
//	if (poly.n < 3) return TYPE(0);
//	double s = poly.y[0] * (poly.x[poly.n - 1] - poly.x[1]);
//	for (int i = 1; i < poly.n; i++)
//	{
//		s += poly.y[i] * (poly.x[i - 1] - poly.x[(i + 1) % poly.n]);
//	}
//	return s/2;
//}
//
////判断是否在多边形上
//bool IsOnPoly(const POLY & poly, const POINT & p)
//{
//	for (int i = 0; i < poly.n; i++)
//	{
//		if (IsOnSeg(Edge(poly, i), p))
//		{
//			return true;
//		}
//	}
//	return false;
//}
//
////判断是否在多边形内部
//bool IsInPoly(const POLY & poly, const POINT & p)
//{
//	SEG L(p, POINT(Infinity, p.y));
//
//	int count = 0;
//	for (int i = 0; i < poly.n; i++)
//	{
//		SEG S = Edge(poly, i);
//		if (IsOnSeg(S, p))
//		{
//			return false;                        //如果想让在poly上则返回 true,
//			//则改为true
//		}
//		if (!IsEqual(S.a.y, S.b.y))
//		{
//			POINT & q = (S.a.y > S.b.y)?(S.a):(S.b);
//			if (IsOnSeg(L, q))
//			{
//				++count;
//			}
//			else if (!IsOnSeg(L, S.a) && !IsOnSeg(L, S.b) && IsIntersect(S, L))
//			{
//				++count;
//			}
//		}
//	}
//	return (count % 2 != 0);
//}
//
//// 点阵的凸包，返回一个多边形
//POLY ConvexHull(const POINT * set, int n)            // 不适用于点少于三个的情况
//{
//	POINT * points = new POINT[n];
//	memcpy(points, set, n * sizeof(POINT));
//
//	TYPE * X = new TYPE[n];
//	TYPE * Y = new TYPE[n];
//
//	int i, j, k = 0, top = 2;
//	for(i = 1; i < n; i++)
//	{
//		if ((points[i].y < points[k].y) ||
//			((points[i].y == points[k].y) &&
//			(points[i].x < points[k].x)))
//		{
//			k = i;
//		}
//	}
//
//	std::swap(points[0], points[k]);
//
//	for (i = 1; i < n - 1; i++)
//	{
//		k = i;
//		for (j = i + 1; j < n; j++)
//		{
//			if ((Cross(points[j], points[k], points[0]) > 0) ||
//				((Cross(points[j], points[k], points[0]) == 0) &&
//				(Distance(points[0], points[j]) < Distance(points[0], points[k]))))
//			{
//				k = j;
//			}
//		}
//		std::swap(points[i], points[k]);
//	}
//
//	X[0] = points[0].x; Y[0] = points[0].y;
//	X[1] = points[1].x; Y[1] = points[1].y;
//
//	X[2] = points[2].x; Y[2] = points[2].y;
//
//	for (i = 3; i < n; i++)
//	{
//		while (Cross(points[i], POINT(X[top], Y[top]),
//			POINT(X[top - 1], Y[top - 1])) >= 0)
//		{
//			top--;
//		}
//		++top;
//		X[top] = points[i].x;
//		Y[top] = points[i].y;
//	}
//
//	delete [] points;
//
//	POLY poly(++top, X, Y);
//
//	delete [] X;
//	delete [] Y;
//
//
//	return poly;
//}

double s(double r1, double r2, double d){
	double ang = 2*acos((r1*r1+d*d-r2*r2)/(2*r1*d));
	double s2 = 0.5*r1*r1*sin(ang);
	double s1 = 0.5*ang*r1*r1;
	return s1 - s2;
}//解析几何

double GetArea(double x1, double y1, double x2, double y2, double r1, double r2)
{
	if(r1 < r2)
	{
		//swap(r1, r2);
		double tmp = r1;
		r1 = r2; r2 = tmp;
	}

	double pi = acos(-1.0);
	double d = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
	//cout.precision(7);
	if(d >= r1+r2 )
		//cout << "0.000" << endl;
		return 0;
	else if(d <= r1-r2) 
		//cout << fixed << pi*r2*r2 << endl; 
		return pi*r2*r2;
	else
		//cout << fixed << s(r1, r2, d)+s(r2, r1, d) << endl;
		return  s(r1, r2, d)+s(r2, r1, d);
}

int N, M;


double GetDist(double x, double y, double x1, double y1)
{
	return sqrt((x-x1)*(x-x1) + (y-y1)*(y-y1));
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
	//freopen("XXX-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	//cout << test << endl;
	while(test--)
	{
		int i;
		cin>>N>>M;
		double x0[100], y0[100];
		double x1[100], y1[100];
		
		for(i=0; i<N; i++) cin>>x0[i]>>y0[i];
		for(i=0; i<M; i++) cin>>x1[i]>>y1[i];

		cout << "Case #" << cas++ << ": ";

		for(i=0; i<M; i++)
		{
			double area = GetArea(x0[0], y0[0], x0[1], y0[1], GetDist(x0[0], y0[0], x1[i], y1[i]), GetDist(x0[1], y0[1], x1[i], y1[i]));
			printf("%.7lf ", area);
			if(i<M-1) printf(" ");
		}
		printf("\n");

	}
	return 0;
}