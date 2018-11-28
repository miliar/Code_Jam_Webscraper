#include<iostream>
#include<string>
#include<sstream>
#include<math.h>
#include<map>
using namespace std;
struct node
{
	double x,y,z,vx,vy,vz;

};
int main()
{
	
	int num,test;
	cin>>test;
	for(int i=0;i<test;++i)
	{
		printf("Case #%i: ",i+1);
		cin>>num;
		node A[num];
		for(int i=0;i<num;++i)
			cin>>A[i].x>>A[i].y>>A[i].z>>A[i].vx>>A[i].vy>>A[i].vz;
		double X=0.0,Y=0.0,Z=0.0,VX=0.0,VY=0.0,VZ=0.0;
		for(int i=0;i<num;++i)
		{
			X+=A[i].x;
			Y+=A[i].y;
			Z+=A[i].z;
			VX+=A[i].vx;
			VY+=A[i].vy;
			VZ+=A[i].vz;
		}
		X/=num;
		Y/=num;
		Z/=num;
		VX/=num;
		VY/=num;
		VZ/=num;
		//cout<<X<<" "<<Y<<" "<<Z<<"  "<<VX<<" "<<VY<<" "<<VZ<<"\n";
		double alpha,beta,gama,time;
		alpha=X*X+Y*Y+Z*Z;
		beta=2.0*X*VX+2.0*Y*VY+2.0*Z*VZ;
		gama=VX*VX+VY*VY+VZ*VZ;
		//cout<<alpha<<" "<<beta<<" "<<gama<<"\n";
		
		if(gama>0.0000000001 || gama<-0.0000000001)
			time=-1.0*beta/(2.0*gama);
		else
			time=0.0;
		
		if(time<0.0)
			time=0.0;
		double dist=alpha+beta*time+gama*time*time;
		if(dist>0.0000000001)
			dist=pow(dist,0.5);
		else
			dist=0.0;
		printf("%.08f %.08f\n",dist,time);
	}
}