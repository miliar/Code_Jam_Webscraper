#include <cstdio>
#include <algorithm>

using namespace std;

struct point
{
	int x, y;
	point (){};
	point (int _x, int _y) { x = _x; y = _y;}
};

point a[1024], b[1024];

int n;

inline int isleft(point p0, point p1, point p2)
{
    int t= (p1.x-p0.x)*(p2.y-p0.y) - (p2.x-p0.x) *(p1.y-p0.y);

    if( t < 0) return -1;
    if(t > 0) return 1;
    return 0;
}

int intersect(point p1, point p2, point p3, point p4)
{
    if(max(p2.x, p1.x) < min(p3.x, p4.x)) return 0;
    if(max(p3.x, p4.x) < min(p1.x, p2.x)) return 0;
    if(max(p1.y, p2.y) < min(p3.y, p4.y)) return 0;
    if(max(p3.y, p4.y) < min(p1.y, p2.y)) return 0;

    if(isleft(p1, p2, p3) * isleft(p1, p2, p4) > 0) return 0;
    if(isleft(p3, p4, p1) * isleft(p3, p4, p2) > 0) return 0;
    return 1;

}

int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);
	int T;
	
	scanf ("%d\n", &T);
	int i;
	int j;
	for (int caz = 1; caz <= T; ++caz)
	{
		scanf ("%d\n", &n);
			
		for (i = 1; i <= n; ++i)
		{
			int h1, h2;
			scanf ("%d %d\n", &h1, &h2);
		
			a[i].x = 0;
			a[i].y = h1;
			
			b[i].x = 10000;
			b[i].y = h2;
		}
		
		int nr = 0;
		for (i = 1; i < n; ++i)
			for (j = i + 1; j <= n; ++j)
				if (intersect (a[i], b[i], a[j], b[j]))
					++nr;
				
		printf ("Case #%d: %d\n", caz, nr);
		
		
	}
	
	
	return 0;
}