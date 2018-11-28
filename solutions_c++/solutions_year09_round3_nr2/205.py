#include <iostream>
#include <cmath>
using namespace std;
#define tiao system("pause")

int t;
int n;
int x[555],y[555],z[555];
int vx[555],vy[555],vz[555];
long long X,Y,Z;
long long VX,VY,VZ;

double sqr(double a)
{
	return (double)a * a;
}
int main(void)
{
	int i,j,k,ci,cici,cicici;
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	scanf("%d",&t);
	for (cicici=1; cicici<=t; cicici++)
	{
		scanf("%d",&n);
		for (i=1; i<=n; i++)
			scanf("%d%d%d%d%d%d",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
		
		X = Y = Z = VX = VY = VZ = 0;
		for (i=1; i<=n; i++)
		{
			X += x[i];
			Y += y[i];
			Z += z[i];
			VX += vx[i];
			VY += vy[i];
			VZ += vz[i];
		}	
		
		if (VX == 0 && VY == 0 && VZ == 0)
		{
			double ans;
			ans = sqrt(sqr((double)X / n) + sqr((double)Y / n) + sqr((double)Z / n));
			
			printf("Case #%d: %.8lf %.8lf\n",cicici,ans,0);
			continue;
		}
		
		
		double a,b,c;
		a = (VX*VX + VY*VY + VZ*VZ);
		b = 2 * (X*VX + Y*VY + Z*VZ);
		c = X*X + Y*Y + Z*Z;
		
		double ans = (4*a*c - b*b) / 4.0 / a / n / n;
		double dtime = -b / (2.0 * a);
		
		if (dtime >= 0) ans = sqrt(ans);
		
		if (dtime < 0) // CCCCCCB
		{
			dtime = 0;
			ans = sqrt(c / n / n);
		}
		printf("Case #%d: %.8lf %.8lf\n",cicici,ans,dtime);	
	}
//	tiao;
	return 0;
}
