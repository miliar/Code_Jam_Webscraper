/*
Language:C++
*/

#include<string>
#include<fstream>
#include<iostream>
#include <math.h>
#include<iomanip>


using namespace std;

int main()
{
	ofstream fout("B-small.out");
	ifstream fin("B-small-attempt1.in");
	
	int t;
	fin>>t;
	for(int i=0;i!=t;i++)
	{
		int n;
		fin>>n;
		
		long ax=0,ay=0,az=0,avx=0,avy=0,avz=0;
		
		int x,y,z,vx,vy,vz;
		for(int j=0;j!=n;j++)
		{
			fin>>x>>y>>z>>vx>>vy>>vz;
			ax+=x;
			ay+=y;
			az+=z;
			avx+=vx;
			avy+=vy;
			avz+=vz;
		}
//cout<<"Case #"<<(i+1)<<": "<<ax<<","<<ay<<","<<az<<","<<avx<<","<<avy<<","<<avz;
		double a=avx*avx+avy*avy+avz*avz;
		double b=(ax*avx+ay*avy+az*avz)*2;
		double c=ax*ax+ay*ay+az*az;
//cout<<",         "<<a<<","<<b<<","<<sqrt(c/(n*n))<<endl;
		double time;
		double distance;
		
		if(a==0)
		{
			time=0;
			distance=sqrt(c/(n*n));
		}else{
		double delta=b*b-4*a*c;
		double middle=-1*b/(a*2);
		
		if(delta<=0)
		{
			if(middle<=0)
			{
				time=0;
				distance=sqrt(c/(n*n));
			}else{
				time=middle;
				distance=sqrt((c+b*time+a*time*time)/(n*n));
			}
		}else{
			double sl=-1*b-sqrt(delta)/(2*a);
			double sr=-1*b+sqrt(delta)/(2*a);
			
			if(sr<=0)
			{
				time=0;
				distance=sqrt((c/(n*n)));
			}else if(sl>=0)
			{
				time =sl;
				distance=0;
			}else{
				time =sr;
				distance=0;
			}
		}
		}
		
		fout.setf(fout.showpoint);
		fout<<setprecision(8);
		fout<<fixed;
		fout<<"Case #"<<(i+1)<<": "<<distance<<" "<<time<<endl;
	}
	return 0;
}
			