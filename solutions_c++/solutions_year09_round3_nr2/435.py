//============================================================================
// Name        : the_center_of_mass.cpp
// Author      : Kinshul Verma
// Version     :
// Copyright   : !!!MIT License!!!
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int cases,n,x,y,z,vx,vy,vz,i;
	long double cx,cy,cz,cvx,cvy,cvz,time,distance,denom;
	scanf("%d",&cases);
	for(int var=1; var<=cases; var++)
	{
		scanf("%d",&n);
		cx=0;cy=0;cz=0;cvx=0;cvy=0;cvz=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d%d%d%d",&x,&y,&z,&vx,&vy,&vz);
			cx+=(x+0.0);
			cy+=(y+0.0);
			cz+=(z+0.0);
			cvx+=(vx+0.0);
			cvy+=(vy+0.0);
			cvz+=(vz+0.0);
		}
		cx/=(n+0.0);
		cy/=(n+0.0);
		cz/=(n+0.0);
		cvx/=(n+0.0);
		cvy/=(n+0.0);
		cvz/=(n+0.0);
		denom = (cvx*cvx + cvy*cvy + cvz*cvz);
		if(denom - 0.0000000000<0.000001000)
		{
			time=0.00000000;
			distance = sqrt(cx*cx + cy*cy + cz*cz);
		}
		else
		{
			time = (-1*(cx * cvx + cy*cvy + cz*cvz))/ denom;
			if(time-0<0.0000001)
			{
				distance = sqrt(cx*cx + cy*cy + cz*cz);
				time = 0.00000000;
			}
			else
			{
				distance = sqrt((cx + cvx * time)*(cx + cvx * time) + (cy + cvy * time)*(cy + cvy * time) + (cz + cvz * time)*(cz + cvz * time));
			}
		}
		printf("Case #%d: %0.8llf %0.8llf\n",var,distance,time);
	}
	return 0;
}
