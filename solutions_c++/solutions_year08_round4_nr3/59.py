#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;
int T,nT;
int N;
struct TVAL
{
	double x,y,z;
	double p;
} vals[1000];
double bx,by,bz,bval;
void gbval(double nx,double ny,double nz)
{
	double nval=0;
	for (int i=0;i<N;i++)
	{
		double tval=(abs(vals[i].x-nx)+abs(vals[i].y-ny)+abs(vals[i].z-nz))/vals[i].p;
		if (tval>nval) nval=tval;
	}
	if (nval<bval)
	{
		bx=nx;
		by=ny;
		bz=nz;
		bval=nval;
	}
}
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	scanf("%d",&T);
	nT=T;
	while (T--)
	{
		scanf("%d",&N);
		int i;
		for (i=0;i<N;i++)
			scanf("%lf%lf%lf%lf",&vals[i].x,&vals[i].y,&vals[i].z,&vals[i].p);
		bx=by=bz=0; bval=1e20;
		double adj;
		for (adj=1e5;adj>1e-10;adj/=1.1)
			for (i=0;i<20;i++)
			{
				gbval(bx-adj,by,bz);
				gbval(bx+adj,by,bz);
				gbval(bx,by-adj,bz);
				gbval(bx,by+adj,bz);
				gbval(bx,by,bz-adj);
				gbval(bx,by,bz+adj);
			}
		printf("Case #%d: %.6lf\n",nT-T,bval);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}