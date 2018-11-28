#include <algorithm>
#include <sstream>
#include <string>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
using namespace std;
typedef long long ll;
const int Maxint=0x7FFFFFFF;
const ll Maxlonglong=0x7FFFFFFFFFFFFFFFll;
const double EPS = 1e-6;
const double PI = 2 * acos(.0);
const double INF = 1e300;


struct Point {
	double x, y;
};
struct Segment {
	Point a, b;
};

Segment bud[1001];
/* ����Sig:
	�жϷ���.
 */
inline int Sig(double k) {
	if (k > EPS) return 1;
	if (k < -EPS) return -1;
	return 0;
}

inline int Equal(double &a, double &b) {
	return Sig(a-b);
}

/* ����Det:
	����������x1, y1)x(x2, y2)
 */
inline double Det(double x1, double y1, double x2, double y2) {
	return (x1*y2 - x2*y1);
}


/* ����Cross:
	���ac��ab����ʱ�뷽�򣬷���ֵ>0
	���ac��ab��˳ʱ�뷽�򣬷���ֵ<0
	a,b,c���ߣ�����ֵ=0
 */
inline double Cross(const Point &a, const Point &b, const Point &c) {
	return Det(b.x - a.x, b.y - a.y, c.x - a.x, c.y - a.y);
}

/* ����On_Segement:
	ǰ�᣺a,b,c����
	�жϵ�c�Ƿ����߶�ab��
 */
inline bool On_Segment(const Point &a, const Point &b, const Point &c) {
	if (c.x >= min(a.x, b.x) && c.x <= max(a.x, b.x) &&
		c.y >= min(a.y, b.y) && c.y <= max(a.y, b.y) )
		return true;
	return false;
}

/* ����Dot, DotDet:
	������ab��ac�ĵ��
 */

inline double DotDet(double x1, double y1, double x2, double y2) {
	return x1*x2 + y1*y2;
}

inline double Dot(const Point &a, const Point &b, const Point &c) {
	return DotDet(b.x - a.x, b.y - a.y, c.x - a.x, c.y - a.y);
}

/* ����Betweencmp:
	ͨ�������ȷ����a�Ƿ���bc��
 */

inline int Betweencmp(const Point &a, const Point &b, const Point &c)  {
	return Sig(Dot(a, b, c));
}


/* ����Seg_Intersect:
	���淶�ཻ������1�����󽻵�
	���ǹ淶�ཻ���򷵻�2
	���ཻ����0
	ע�⣺���Բ��淶�ཻ�󽻵㣬ֻҪ�ĵ㲻���ߣ��Կ������
 */
inline int Seg_Intersect(const Segment &sg1, const Segment &sg2, Point &pt) {
	double s1, s2, s3, s4;
	int d1, d2, d3, d4;
	d1 = Sig(s1 = Cross(sg1.a, sg1.b, sg2.a));
	d2 = Sig(s2 = Cross(sg1.a, sg1.b, sg2.b));
	d3 = Sig(s3 = Cross(sg2.a, sg2.b, sg1.a));
	d4 = Sig(s4 = Cross(sg2.a, sg2.b, sg1.b));
	if ( ((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0)) &&
		 ((d3 > 0 && d4 < 0) || (d3 < 0 && d4 > 0)) ) {
		pt.x = (sg2.a.x*s2 - sg2.b.x*s1) / (s2-s1);
		pt.y = (sg2.a.y*s2 - sg2.b.y*s1) / (s2-s1);
		return 1;
	}
// �������ж�
	else if (d1 == 0 && On_Segment(sg1.a, sg1.b, sg2.a) )
		return 2;
	else if (d2 == 0 && On_Segment(sg1.a, sg1.b, sg2.b) )
		return 2;
	else if (d3 == 0 && On_Segment(sg2.a, sg2.b, sg1.a) )
		return 2;
	else if (d4 == 0 && On_Segment(sg2.a, sg2.b, sg1.b) )
		return 2;
// �õ���Ƚ�
/* 	else if (d1 == 0 && Betweencmp(sg2.a, sg1.a, sg1.b) <= 0 )
		return 2;
	else if (d2 == 0 && Betweencmp(sg2.b, sg1.a, sg1.b) <= 0 )
		return 2;
	else if (d3 == 0 && Betweencmp(sg1.a, sg2.a, sg2.b) <= 0 )
		return 2;
	else if (d4 == 0 && Betweencmp(sg1.b, sg2.a, sg2.b) <= 0 )
		return 2;  */
	return 0;
}

int main() {
	int T;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int w = 1; w <= T; w++) {
		int n;
		scanf("%d", &n);
		int y1, y2;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d %d", &y1, &y2);
			bud[i].a.x = 0.0;
			bud[i].a.y = (double)y1;
			bud[i].b.x = 1.0;
			bud[i].b.y = (double)y2;
			Point p;
			for (int j = 0; j < i; j++) if (Seg_Intersect(bud[i], bud[j], p))
			    ans++;
		}
		printf("Case #%d: %d\n", w, ans);
	}
//	system("pause");
	return 0;
}
