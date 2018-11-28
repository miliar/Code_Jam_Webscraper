#include <stdio.h>
#include <math.h>
#include <algorithm>
#define Bint long long
using namespace std;
Bint X, Y, Z, x, y, z, a, b, c;
pair<double,double> process()
{
	a = x*x+y*y+z*z; b = 2*(x*X+y*Y+z*Z); c = X*X+Y*Y+Z*Z;
	return a*b<0?make_pair(sqrt(4*a*c-b*b+0.0)/sqrt(4*a+0.0),-(double)b/2/a):make_pair(sqrt(c+0.0),0.0);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, n, i;
	int xx, yy, zz, vx, vy, vz;
	
	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		scanf("%d",&n);
		X = Y = Z = 0; x = y = z = 0;
		for (i = 0; i < n; i++) {
			scanf("%d%d%d%d%d%d",&xx,&yy,&zz,&vx,&vy,&vz);
			X += xx; Y += yy; Z += zz;
			x += vx; y += vy; z += vz;
		}
//		X /= n; Y /= n; Z /= n; x /= n; y /= n; z /= n;
		printf("Case #%d: %lf %lf\n", t, process().first/n, process().second);
	}
	return 0;
}