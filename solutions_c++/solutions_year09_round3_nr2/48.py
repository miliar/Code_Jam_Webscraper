#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <queue>
#include <cmath>
using namespace std;
int tc,n;
int x[505],y[505],z[505],vx[505],vy[505],vz[505];
double ex,ey,ez,evx,evy,evz;
double P,AC,D,TMP;
double s(double a){
	return (a*a*1.0);
}
int main(){
	scanf("%d",&tc);
	for (int c=1;c<=tc;c++){
		ex=ey=ez=evx=evy=evz=0;
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			scanf("%d%d%d%d%d%d",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
			ex+=x[i]; ey+=y[i]; ez+=z[i];
			evx+=vx[i]; evy+=vy[i]; evz+=vz[i];
		}
		TMP=s(evx)+s(evy)+s(evz);
		if (fabs(TMP)>=1e-8)
			P=(-(ex*evx+ey*evy+ez*evz)*1.0)/TMP;
		else P=0;
		if (P<0) P=0;
		//printf("P = %lf\n",P);
		ex=ey=ez=evx=evy=evz=0;
		for (int i=1;i<=n;i++){
			ex+=x[i]+P*vx[i]; ey+=y[i]+P*vy[i]; ez+=z[i]+P*vz[i];
		}
		D=sqrt((s(ex/n)+s(ey/n)+s(ez/n)));
		printf("Case #%d: %lf %lf\n",c,D,P);
	}
}
