#include <string>
#include <vector>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include<fstream> 
using namespace std;
struct point
{
	double x,y,z,vx,vy,vz;
}res[501];
int main()
{
	ofstream ofs; 
	ifstream ifs;
	ifs.open("d:\\Wraith\\A.in");
	ofs.open("d:\\Wraith\\a.out");
	int num;
	//cin>>num;
	ifs>>num;
	for(int i=1;i<=num;i++)
	{
		int a;
		double aswd=0,aswt=0;
		double X=0,Y=0,Z=0,vX=0,vY=0,vZ=0;
		ifs>>a;
		//cin>>a;
		for(int j=0;j<a;j++)
		{
			ifs>>res[j].x>>res[j].y>>res[j].z>>res[j].vx>>res[j].vy>>res[j].vz;
			X+=res[j].x;Y+=res[j].y;Z+=res[j].z;vX+=res[j].vx;vY+=res[j].vy;vZ+=res[j].vz;
		}
		ofs<<"Case #"<<i<<": ";
		//cout<<"Case #"<<i<<": ";
		X/=double(a);Y/=double(a);Z/=double(a);
		vX/=double(a);vY/=double(a);vZ/=double(a);
		double aa=(vX*vX+vY*vY+vZ*vZ),cc=(X*X+Y*Y+Z*Z),bb=2*(X*vX+Y*vY+Z*vZ);
		if(aa==0){aswt=0;if(bb==0)aswd=cc;else aswd=-cc/bb;}
		else 
		{
			aswt=-bb/(2.0*aa);
			if(aswt>=0)
			aswd=cc-bb*bb/(4.0*aa);
			else {aswt=0;aswd=cc;}
		}aswd=sqrt(fabs(aswd));
		ofs<<std::fixed<<aswd<<" "<<aswt<<endl;
	}
	return 0;
}