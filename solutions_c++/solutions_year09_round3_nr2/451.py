#include<iostream>
#include <vector>
#include <stack>
#include <map>
#include <queue>
#include <list>
#include <algorithm>
#include <set>
#include <cstring>
#include<string.h>
#include <cmath>
#include<math.h>
#include <cassert>
#include <sstream>
#include <climits>
#include <deque>
#include <fstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{
	int Test;
	scanf("%d",&Test);
	for(int i=1;i<=Test;i++){
		int nos;
		scanf("%d",&nos);
		long double X[nos],Y[nos],Z[nos],VX[nos],VY[nos],VZ[nos];
		long double cx=0.0,cy=0.0,cz=0.0,vcx=0.0,vcy=0.0,vcz=0.0;
		long double time,dist;
		for(int j=0;j<nos;j++){
			scanf("%Lf%Lf%Lf%Lf%Lf%Lf",&X[j],&Y[j],&Z[j],&VX[j],&VY[j],&VZ[j]);
			cx+=X[j], cy+=Y[j], cz+=Z[j], vcx+=VX[j], vcy+=VY[j], vcz+=VZ[j];
		}
		printf("Case #%d: ",i);
		cx=cx/(long double)(nos);
		cy=cy/(long double)(nos);
		cz=cz/(long double)(nos);
		vcx=vcx/(long double)(nos);
		vcy=vcy/(long double)(nos);
		vcz=vcz/(long double)(nos);
		if(vcx==0.0 and vcy==0.0 and vcz==0.0){
			dist=sqrt(cx*cx+cy*cy+cz*cz);
			printf("%0.8Lf 0.00000000\n",dist);
		}
		else{
			long double num=0.0,den=0.0;
			for(int j=0;j<nos;j++){
				num-=(cx*vcx+cy*vcy+cz*vcz);
				den+=(vcx*vcx+vcy*vcy+vcz*vcz);
			}
			time=(num/den);
			if(time<0.0)
				time=0.0;
			long double ncx,ncy,ncz;
			ncx=cx+vcx*time;
			ncy=cy+vcy*time;
			ncz=cz+vcz*time;
			dist=sqrt(ncx*ncx+ncy*ncy+ncz*ncz);
			printf("%0.8Lf %0.8Lf\n",dist,time);
		}
	}
}
