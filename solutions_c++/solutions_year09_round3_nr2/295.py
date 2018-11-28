#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>
using namespace std;
int main(void)
{
	int w,n,Ax,Ay,Az,Bx,By,Bz,i,x,y,z,vx,vy,vz,q;
	double Axx,Ayy,Azz,Bxx,Byy,Bzz,d,t;
	freopen("r2.in","r",stdin);
	freopen("r2.out","w",stdout);
	scanf("%d",&w);
	for (q=1;q<=w;q++)
	{
		scanf("%d",&n);
		Ax=Ay=Az=Bx=By=Bz=0;
		for (i=0;i<n;i++)
		{
			scanf("%d%d%d%d%d%d",&x,&y,&z,&vx,&vy,&vz);
			Ax+=x;
			Ay+=y;
			Az+=z;
			Bx+=vx;
			By+=vy;
			Bz+=vz;
		}
		Axx=Ax/double(n);
		Ayy=Ay/double(n);
		Azz=Az/double(n);
		Bxx=Bx/double(n);
		Byy=By/double(n);
		Bzz=Bz/double(n);
		if (((Bx==0)&&(By==0)&&(Bz==0))||((Ax==0)&&(Ay==0)&&(Az==0)))
			t=0; else
			t=-(Axx*Bxx+Ayy*Byy+Azz*Bzz)/(Bxx*Bxx+Byy*Byy+Bzz*Bzz);
		if (t<0)
			t=0;
		d=sqrt((Axx+t*Bxx)*(Axx+t*Bxx)+(Ayy+t*Byy)*(Ayy+t*Byy)+(Azz+t*Bzz)*(Azz+t*Bzz));
		printf("Case #%d: %.8lf %.8lf\n",q,d,t);
	}
	fclose(stdout);
	return 0;
}