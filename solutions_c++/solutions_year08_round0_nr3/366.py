#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

#define PI 3.1415926536

using namespace std;
ifstream fin;
ofstream fout;

struct POINT
{
	double x,y;
};
inline bool inside(double x,double y,double r)
{
	if(x*x+y*y<=r*r)
		return true;
	return false;
}
double calc_dist(POINT p1, POINT p2)
{
	return sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y));
}
double calc_tri(POINT p1, POINT p2, POINT p3)
{
	double a,b,c,p;
	a=calc_dist(p1,p2);
	b=calc_dist(p1,p3);
	c=calc_dist(p2,p3);
	p=(a+b+c)/2.0;
	return sqrt(p*(p-a)*(p-b)*(p-c));
}
double calc_gong(POINT p1, POINT p2)
{
	POINT O1;
	O1.x=O1.y=0.0;
	double a,b,c,angle;
	c=calc_dist(p1,p2);
	a=calc_dist(p1,O1);
	b=calc_dist(p2,O1);
	angle=acos((a*a+b*b-c*c)/(2.0*a*b));
	return a*a*angle/2.0-calc_tri(p1,p2,O1);
}
double calc_vol(double x,double y,double a,double r)
{
	POINT corner[4];
	corner[0].x=x-a;
	corner[0].y=y-a;
	corner[1].x=x+a;
	corner[1].y=y-a;
	corner[2].x=x-a;
	corner[2].y=y+a;
	corner[3].x=x+a;
	corner[3].y=y+a;
	POINT p1,p2;
	if(corner[3].x*corner[3].x+corner[3].y*corner[3].y<=r*r)
	{
		return a*a*4.0;
	}
	if(corner[0].x*corner[0].x+corner[0].y*corner[0].y>=r*r)
	{
		return 0.0;
	}
	if((corner[1].x*corner[1].x+corner[1].y*corner[1].y>=r*r)&&
		(corner[2].x*corner[2].x+corner[2].y*corner[2].y>=r*r))
	{//case 1:
		p1.x=corner[0].x;
		p1.y=sqrt(r*r-corner[0].x*corner[0].x);
		p2.y=corner[0].y;
		p2.x=sqrt(r*r-corner[0].y*corner[0].y);
		return calc_tri(p1,p2,corner[0])+calc_gong(p1,p2);
	}
	else if((corner[1].x*corner[1].x+corner[1].y*corner[1].y<=r*r)&&
		(corner[2].x*corner[2].x+corner[2].y*corner[2].y<=r*r))
	{//case 2:
		p1.y=corner[3].y;
		p1.x=sqrt(r*r-corner[3].y*corner[3].y);
		p2.x=corner[3].x;
		p2.y=sqrt(r*r-corner[3].x*corner[3].x);
		return a*a*4.0-calc_tri(p1,p2,corner[3])+calc_gong(p1,p2);
	}
	else if((corner[1].x*corner[1].x+corner[1].y*corner[1].y<=r*r)&&
		(corner[2].x*corner[2].x+corner[2].y*corner[2].y>=r*r))
	{//case 3:
		p1.x=corner[0].x;
		p1.y=sqrt(r*r-corner[0].x*corner[0].x);
		p2.x=corner[3].x;
		p2.y=sqrt(r*r-corner[3].x*corner[3].x);
		return calc_gong(p1,p2)+calc_tri(p1,p2,corner[0])+calc_tri(p2,corner[0],corner[1]);
	}
	else if((corner[1].x*corner[1].x+corner[1].y*corner[1].y>=r*r)&&
		(corner[2].x*corner[2].x+corner[2].y*corner[2].y<=r*r))
	{//case 4:
		p1.y=corner[3].y;
		p1.x=sqrt(r*r-corner[3].y*corner[3].y);
		p2.y=corner[0].y;
		p2.x=sqrt(r*r-corner[0].y*corner[0].y);
		return calc_gong(p1,p2)+calc_tri(p1,p2,corner[0])+calc_tri(p1,corner[0],corner[2]);
	}
	else
	{
		cout<<"Error"<<endl;
	}
	return 0.0;
}

int main(void)
{
	int it,i,j,k,l,N;
	double f,R,t,r,g;
	double x,y;
	fin.open("input.in");
	FILE *fp=fopen("output.out","w");
	fin>>N;
//	fin>>noskipws;
//	fin>>skipws;
	double area,prob;
	for(it=1;it<=N;it++)
	{
		fin>>f>>R>>t>>r>>g;
		if(g/2.0<=f)
		{
			fprintf(fp,"Case #%d: %.6f\n",it,1.0);
			continue;
		}
		x=y=0.0;
		area=0.0;
		for(j=0;y-g/2.0<=R;j++)
		{
			y=r+g/2.0+j*(2*r+g);
			x=0.0;
			for(i=0;x-g/2.0<=R;i++)
			{
				x=r+g/2.0+i*(2*r+g);
				area+=calc_vol(x,y,g/2.0-f,R-t-f);
			}
		}
		area*=4.0;
		prob=(PI*R*R-area)/(PI*R*R);
		fprintf(fp,"Case #%d: %.6f\n",it,prob);
	}
    fin.close();
	fclose(fp);
	return 0;
}
