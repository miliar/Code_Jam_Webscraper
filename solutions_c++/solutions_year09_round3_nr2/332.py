#include <stdio.h>
#include <string.h>
#include <math.h>
struct point
{
	double x,y,z,vx,vy,vz;
};
//point data[510];
int main()
{
	int i,j,k,n,m;
	point center,tmp;
	double t,d;
	freopen("out.txt","w",stdout);
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		scanf("%d",&m);
		memset(&center,0,sizeof(center));
		for(j=0;j<m;j++)
		{
			/*scanf("%d%d%d%d%d%d",
				&data[j].x,
				&data[j].y,
				&data[j].z,
				&data[j].vx,
				&data[j].vy,
				&data[j].vz);*/
			scanf("%lf%lf%lf%lf%lf%lf",
				&tmp.x,
				&tmp.y,
				&tmp.z,
				&tmp.vx,
				&tmp.vy,
				&tmp.vz);

			center.x += tmp.x;
			center.y += tmp.y;
			center.z += tmp.z;
			center.vx += tmp.vx;
			center.vy += tmp.vy;
			center.vz += tmp.vz;
		}
		center.x /=m;
		center.y /=m;
		center.z /=m;
		center.vx /=m;
		center.vy /=m;
		center.vz /=m;

		double v = -(center.vx * center.x + center.vy * center.y + center.vz * center.z);
		if(v > 0)
		{
			double u = (center.vx * center.vx + center.vy * center.vy + center.vz * center.vz);
			t = v/u;
		}
		else
			t =0;

		d = (center.vx * t + center.x) * (center.vx * t + center.x)
			+ (center.vy * t + center.y) *(center.vy * t + center.y)
			+ (center.vz * t + center.z) * (center.vz * t + center.z);

		printf("Case #%d: %.8lf %.8lf\n",i,sqrt(d),t);


		
	}

}