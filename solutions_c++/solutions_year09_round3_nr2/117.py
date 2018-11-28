#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>

#define ERR 1e-9

using namespace std;

int main()
{
//	freopen("B-small-attempt1.in", "rt", stdin);
//	freopen("B-small.out", "wt", stdout);
	
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	int i, j, kase, inp, n;
	double xi, yi, zi, vxi, vyi, vzi;
	double x, y, z, a, b, c;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d", &n);
		x = y = z = a = b = c = 0.0;
		int tn = n;
		while(tn--)
		{
			scanf("%lf %lf %lf %lf %lf %lf", &xi, &yi, &zi, &vxi, &vyi, &vzi);
			x += (xi / n);
			y += (yi / n);
			z += (zi / n);
			a += (vxi / n);
			b += (vyi / n);
			c += (vzi / n);
		}
		double dn = (a * a + b * b + c * c);
		double t;
		if(fabs(dn) < ERR)
			t = 0.0;
		else
			t = (-1.0 * (a * x + b * y + c * z)) / dn;

		if(t < 0.0)
			t = 0.0;
		double d = (x + a * t) * (x + a * t) + (y + b * t) * (y + b * t) + (z + c * t) * (z + c * t);
		d = sqrt(d);
		printf("Case #%d: %lf %lf\n", kase, d + ERR, t + ERR);
	}
	return 0;
}
