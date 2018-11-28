#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
using namespace std;

typedef long double f64;

const f64 pi = 2*acosl(0.0L);

f64 f, R, t, r, g, d; // d = r+g+r

f64 simpleArea(f64 y1, f64 x2, f64 y2)
{
	assert(y2 >= y1 && x2 >= 0.0L && x2 <= d && y2 <= d);
	f64 wx1 = r, wx2 = min(x2,r+g), wy1 = max(r,y1), wy2 = min(y2,r+g);
	return (y2-y1)*x2-max(0.0L,wx2-wx1)*max(0.0L,wy2-wy1);
}

f64 area(f64 y1, f64 x2, f64 y2)
{
	assert(y1 >= 0.0L && x2 >= 0.0L && y2 >= y1);
	f64 ix = floorl(x2/d-1e-9L);
	if (ix >= 1.0L-1e-9L)
	{
		return ix*area(y1,d,y2) + area(y1,x2-ix*d,y2);
	}
	else
	{
		f64 hy = floorl(y2/d+1e-9L)*d;
		assert(hy <= y2);
		if (hy >= y1 && hy <= y2)
		{
			f64 ly = floorl(y1/d+1.0L-1e-9L)*d;
			assert(ly <= hy && ly >= y1 && ly <= y2);
			return simpleArea(0.0L,x2,ly-y1) + floorl(hy-ly+1e-9L)*simpleArea(0.0L,x2,d) + simpleArea(0.0L,x2,y2-hy);
		}
		else
		{
			return simpleArea(y1-hy,x2,y2-hy);
		}
	}
}

f64 selectedAreaCircle()
{
	const int n = 4000000;
	assert(R-t-f >= 0.0L);

	f64 res = 0.0L;
	for (int i=0;i<n;i++)
	{
		f64 y1 = (f64)i*(R-t-f)/(f64)n, y2 = (f64)(i+1)*(R-t-f)/(f64)n;
		f64 x2 = sqrtl(powl(R-t-f,2.0L)-powl(y2,2.0L));
		f64 a = area(y1,x2,y2);
		assert (a <= x2*(y2-y1)+1.0);
		res += a;
	}

	return 4.0L*res;
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int tcase=1;tcase<=tc;tcase++)
	{
		scanf("%llf %llf %llf %llf %llf",&f,&R,&t,&r,&g);
		//d = r+g+r; printf("%llf\n", area(0.5L,3.5L,2.0L)); return 0.0L;
		f *= 10e6L, R *= 10e6L, t *= 10e6L, r *= 10e6L, g *= 10e6L;
		
		printf("Case #%d: ", tcase);
		if (g-2.0L*f <= 0.0L)
		{
			printf("%.6llf\n", 1.0L);
		}
		else
		{
			g -= 2.0L*f; r += f; d = r+g+r;
			if (R-t-f <= 0.0L)
				printf("%.6llf\n", 1.0L);
			else
			{
				f64 inArea = pi*powl(R-t-f,2.0L);
				f64 totalArea = pi*powl(R,2.0L);
				f64 outArea = totalArea - inArea;
				f64 hitArea = selectedAreaCircle();
				assert(hitArea <= inArea);
				printf("%.6llf\n", inArea/totalArea*(hitArea/inArea) + outArea/totalArea);
			}
		}
	}
	return 0;
}
