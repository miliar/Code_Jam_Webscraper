#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
#include <hash_map>
using namespace std;
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
template <class T>
ostream & operator << (ostream & out, const vector<T> & t)
{	out << t.size() << " {";	for (int i = 0; i < t.size(); ++i) 		out << t[i] << " ";	out << "}";	return out;}

template <class T>
ostream & operator << (ostream & out, const set<T> & t)
{	out << "{";	for (set<T>::iterator itr = t.begin(); itr != t.end(); ++itr)		out << *itr << " ";	out << "}";	return out;}


const double eps = 1e-6;
const double pi = acos(-1.0);
const double INF = 1e20;

/** Return a float number's sign */
inline int sign(double d) { return d < -eps ? -1 : d > eps; }
inline double sqr(double x) { return x * x; }

struct Point 
{
	double x, y;
	Point() { x = 0.0; y = 0.0; }
	Point(double nx, double ny) : x(nx), y(ny) {}
	Point turnLeft() const { return Point(-y, x); }
	Point turnRight() const { return Point(y, -x); } 
	Point rotate(double ang) const { return Point(x * cos(ang) - y * sin(ang), x * sin(ang) + y * cos(ang)); }

	inline double length() { return sqrt(x * x + y * y); }
	void normalize() { double r = length(); if (sign(r) != 0)  x /= r,y /= r; }

	/** Consider the float precision to judge whether two points are the same */
	inline bool equal(const Point & other) const {
		return sign(x - other.x) == 0 && sign(y - other.y) == 0;
	}

	friend ostream & operator << (ostream & out , const Point & point)
	{
		out << "(" << point.x << "," << point.y << ")";
		return out;
	}
};

//////////////////////////////////////////////////////////////////////
// BASIC OPERATIONS
//////////////////////////////////////////////////////////////////////
inline Point operator + (const Point & a, const Point & b) {
	return Point(a.x + b.x, a.y + b.y);
}

inline Point operator - (const Point & a , const Point & b) {
	return Point(a.x - b.x, a.y - b.y);
}

inline Point operator * (const Point & a , double d) {
	return Point(a.x * d, a.y * d);
}

inline Point operator / (const Point & a , double d) {
	if (sign(d) == 0) return Point();
	return Point(a.x / d, a.y / d);
}

inline bool operator == (const Point & a , const Point & b) {
	return a.x == b.x && a.y == b.y;
}

inline bool operator != (const Point & a , const Point & b) {
	return a.x != b.x || a.y != b.y;
}

inline double dist(const Point & a , const Point & b) {
	return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
}

inline double sqrdist(const Point & a , const Point & b)
{
	return sqr(a.x - b.x) + sqr(a.y - b.y);
}

/** Cross Product */
inline double operator ^ (const Point & a , const Point & b) {
	return a.x * b.y - a.y * b.x;
}

inline double cross(const Point & p , const Point & a , const Point & b) {
	return (a - p) ^ (b - p);
}

/** Dot product */
inline double operator * (const Point & a , const Point & b) {
	return a.x * b.x + a.y * b.y;
}

inline double dot(const Point & p , const Point & a , const Point & b) {
	return (a - p) * (b - p);
}

/** return degree of two segment span */
inline double segDegree(const Point & p, const Point & a, const Point & b)
{
	double d = dot(p, a, b);
	double cosd =  d / dist(a, p) / dist(b, p);
	if (cosd > 1.0) cosd = 1.0;
	if (cosd < -1.0) cosd = -1.0;
	return acos(cosd);
}

///////////////////////////////////////////////////////////////////////////
// OPERATION ABOUT segment line
///////////////////////////////////////////////////////////////////////////
/** Whether Point p is on the segment [a, b] or not */
inline bool onSeg(const Point & p , const Point & a , const Point & b) {
	return ( sign(cross(p, a, b)) == 0 && sign(dot(p, a, b)) <= 0) ;
}

/** Whether Point p is on the ray from a to b */
inline bool onRay(const Point & p , const Point & a , const Point & b) {
	return ( sign(cross(p, a, b)) == 0 && sign(dot(a, p, b)) >= 0) ;
}

/** Whether Point p is on the straight line a-b or not */
inline bool onLine(const Point & p , const Point & a , const Point & b) {
	return sign(cross(p,a,b))==0;
}

/** Given a line equation Ax + By + C = 0, return two diff points on it, A^2 +B^2 <> 0 */
pair<Point, Point> onLine(double A, double B, double C)
{
	if (sign(A) == 0)
		return make_pair(Point(0, -C / B), Point(1, -C / B));
	if (sign(B) == 0)
		return make_pair(Point(-C / A, 0), Point(-C / A, 1));
	return make_pair(Point(-(C + B) / A, 1), Point(1, -(C + A) / B));
}

/** Find the intersection point of two strait lines a-b and c-d, 
storing the result in p */
vector<Point> interLine(const Point & a , const Point & b , const Point & c , const Point & d) 
{
	vector<Point> inters;
	double u = cross(a, c, b), v = cross(a, b, d);
	if (sign(u + v) == 0) return inters;
	Point p = (c * v + d * u) / (u + v);
	inters.push_back(p);
	return inters;
}

/** Find the intersection point of two segment a-b and c-d,
storing the result in p */
vector<Point> interSeg(const Point & a , const Point & b , const Point & c , const Point & d)
{
	vector<Point> inters = interLine(a, b, c, d);
	if (inters.size() == 0) return inters;
	const Point & p = inters[0];
	if (onSeg(p, a, b) && onSeg(p, c, d)) 
		return inters;
	else {
		inters.clear();
		return inters;
	}       
}

/** Given a segment, return its vertical equally segment */
pair<Point, Point> getVerticalEquallySegment(const Point & a, const Point & b)
{
	Point mid = (a + b) / 2;
	Point dir = mid - a;
	dir = dir.turnLeft();
	Point begin = mid - dir;
	Point end = mid + dir;
	return make_pair(begin, end);
}

/** Given a line and a point p, return the point on the line which has the minimum distance to the point */
Point getMinimumDistPointOnLine(const Point & a, const Point & b, const Point & p)
{
	pair<Point, Point> vertical = getVerticalEquallySegment(a, b);
	const Point & q = p + (vertical.second - vertical.first);
	vector<Point> inter = interLine(a, b, p, q);
	return inter[0];
}

/** Given a segment and a point p, return the point on the segment which has the minimum distance to the point */
Point getMinimumDistPointOnSeg(const Point & a, const Point & b, const Point & p)
{
	Point q = getMinimumDistPointOnLine(a, b, p);
	if (onSeg(q, a, b)) return q;
	if (dist(a, p) < dist(b, p)) return a; else return b;
}

/////////////////////////
// template finished
/////////////////////////
int T, testid;
int X;
double Walk, Run;
double t;
int N;
vector<pair<int, int> > v_s;
void init()
{
	v_s.clear();
	cin >> X >> Walk >> Run >> t >> N;
	int remain = X;
	for (int i = 0; i < N; ++i)
	{
		int B, E, w;
		cin >> B >> E >> w;
		v_s.push_back(make_pair(w + Walk, E - B));
		remain -= (E - B);
	}
	v_s.push_back(make_pair(Walk, remain));
}

void york()
{
	sort(v_s.begin(), v_s.end());
	double ans = 0;
	for (int i = 0; i < v_s.size(); ++i)
	{
		double dist = v_s[i].second;
		double nows = v_s[i].first;
		double maxrunt = dist / (nows - Walk + Run);
		
		double nowrunt = min(maxrunt, t);
		//debug4(dist, nows, maxrunt, nowrunt);
		double nowt = nowrunt + (dist - nowrunt * (nows - Walk + Run)) / nows;
		ans += nowt;
		t -= nowrunt;
	}
	printf("Case #%d: %.8f\n", testid, ans);
}

int main()
{
	cin >> T;
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}
	return 0;
}