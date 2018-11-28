#include <iostream>
#include <cmath>
using namespace std;
int n;
struct point
{
	double x, y, r;
	void read () {scanf ("%lf%lf%lf", &x, &y, &r);}
	
};
double dist (point p1, point p2)
{
	
	return (sqrt ((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y)) + p1.r + p2.r)/2; 
}
double get (point p1, point p2, point p3)
{
	return max (dist(p1, p2),max(p3.r, max (p1.r, p2.r ) ) );
}
void solve ()
{
	scanf ("%d", &n);
	point  A, B, C;
	
	if (n == 1)
	{
	A.read ();
	printf ("%.6lf\n",A.r);

	}
	else
		if (n == 2)
	{
		A.read();
		B.read ();
		printf ("%.6lf\n",max (A.r, B.r));

	}
	else
	{
		A.read (); B.read  (); C.read();
	printf ("%.6lf\n", min (get (A, B, C), min (get(A, C, B), get (B, C, A))));
	}
}
int main ()
{
	int o;
	scanf ("%d", &o);
	
	int i;
	for (i = 1; i <=o; i++)
	{
		printf("Case #%d: ", i);
		solve ();		
	}

	return 0;
}