#include <iostream>
using namespace std;

struct Point
{
	double x, y;
	Point() {}
	Point(double x1, double y1): x(x1), y(y1) {}
};
struct Line
{
	Point p1, p2;
	Line() {}
	Line(Point t1, Point t2): p1(t1), p2(t2) {}
};

inline double Cross(Point p, Point from, Point to)
{
	return (to.x-from.x)*(p.y-from.y)-(to.y-from.y)*(p.x-from.x);
}

Line line[1000];

bool Intersect(Line li1, Line li2);
bool OnSeg(Line li, Point p);

int main()
{
	int cas, N, res;

	freopen("t.txt", "r", stdin);
	freopen("t.out", "w", stdout);
	cin>>cas;
	for(int ii=1; ii<=cas; ii++)
	{
		cin>>N;
		res = 0;
		for(int i=0; i<N; i++)
		{
			line[i].p1.x = 1;
			line[i].p2.x = 2;
			cin>>line[i].p1.y>>line[i].p2.y;
		}
		for(int i=0; i<N; i++)
			for(int j=0; j<i; j++)
				if( Intersect(line[i], line[j]) )
					res++;
		cout<<"Case #"<<ii<<": "<<res<<endl;
	}

	return 0;
}

bool Intersect(Line li1, Line li2)
{
	long long p11 = Cross(li1.p1, li2.p1, li2.p2);
	long long p12 = Cross(li1.p2, li2.p1, li2.p2);
	long long p21 = Cross(li2.p1, li1.p1, li1.p2);
	long long p22 = Cross(li2.p2, li1.p1, li1.p2);

	if( p11*p12<0 && p21*p22<0 )
		return true;
	else if( !p11 && OnSeg(li2, li1.p1) )
		return true;
	else if( !p12 && OnSeg(li2, li1.p2) )
		return true;
	else if( !p21 && OnSeg(li1, li2.p1) )
		return true;
	else if( !p22 && OnSeg(li1, li2.p2) )
		return true;
	else
		return false;
}

bool OnSeg(Line li, Point p)
{
	if( p.x>=min(li.p1.x, li.p2.x) && p.x<=max(li.p1.x, li.p2.x) &&
		p.y>=min(li.p1.y, li.p2.y) && p.y<=max(li.p1.y, li.p2.y)     )
		return true;
	else
		return false;
}
