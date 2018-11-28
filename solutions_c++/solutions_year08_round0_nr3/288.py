#include "stdio.h"
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
#define MaxNum 100
#define PI 3.1415926
struct  Point 
{
	double x;
	double y;
};
double LineAera(double L,double R)
{
	double H;
	H = sqrt(R*R-(L/2)*(L/2));
	double ang = atan2(L/2,H);
	return (ang*R*R - L*H/2);
}
void main()
{
	FILE   *infile;
	int CaseNum;
	double f[MaxNum];
	double R[MaxNum];
	double t[MaxNum];
	double l[MaxNum];
	double g[MaxNum];
	Point corner[5];
	double HStep;
	double WStep;
	double CubeWidth;
	double StepWidth;
	double TotlaAera;
	double SingleAera;
	double QAear;
	double Percent[MaxNum];
	double Line;
	int flag[2];
	infile=fopen("c:\\C-large.in","r");   
    fscanf(infile,"%d",&CaseNum); 
	for (int i=0;i<CaseNum;i++)
	{
		 fscanf(infile,"%lf %lf %lf %lf %lf",  &f[i],&R[i],&t[i],&l[i],&g[i]);
		 cout<<"f:"<<f[i]<<" "<<"R:"<<R[i]<<" "<<"t:"<<t[i]<<" "<<"r:"<<l[i]<<" "<<"g:"<<g[i]<<endl;
		 HStep = l[i]+f[i];	
		 CubeWidth = g[i] - 2*f[i];
		 StepWidth = g[i]+2*l[i];
		 TotlaAera = 0;
		 if (CubeWidth<=0)
		 {
			 goto next;
		 }
		 while (HStep<=(R[i]-t[i]-f[i]))
		 {
			  WStep = l[i]+f[i];
			 while ((WStep*WStep+HStep*HStep)<=(R[i]-t[i]-f[i])*(R[i]-t[i]-f[i])&&WStep<=(R[i]-t[i]-f[i]))
			 {
				 SingleAera = 0;
				 corner[0].x = WStep;
				 corner[0].y = HStep;
				 if((corner[0].x*corner[0].x+(corner[0].y+CubeWidth)*(corner[0].y+CubeWidth))<=(R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]))
				 {
				 corner[1].x = corner[0].x;
				 corner[1].y = corner[0].y+CubeWidth;
				 flag[0] = 0;
				 }
				 else if((corner[0].x*corner[0].x+(corner[0].y+CubeWidth)*(corner[0].y+CubeWidth))>(R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]))
				 {
					 corner[1].x = corner[0].x;
					 corner[1].y = sqrt((R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]) - corner[0].x*corner[0].x);
					 flag[0] = 1;
				 }
				 if ((corner[0].y*corner[0].y+(corner[0].x+CubeWidth)*(corner[0].x+CubeWidth))<=(R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]))
				 {
					 corner[2].x = corner[0].x + CubeWidth;
					 corner[2].y = corner[0].y;
					 flag[1] = 0;
				 }
				 else if((corner[0].y*corner[0].y+(corner[0].x+CubeWidth)*(corner[0].x+CubeWidth))>(R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]))
				 {
					 corner[2].y = corner[0].y;
					 corner[2].x = sqrt((R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]) - corner[0].y*corner[0].y);
					 flag[1] = 1;
 				 }
				 if (flag[0]==0&&flag[1]==0)
				 {
					 if ((corner[1].y*corner[1].y+corner[2].x*corner[2].x)<=(R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]))
					 {
						 SingleAera = CubeWidth*CubeWidth;
					 }
					 else
					 {
						 corner[3].x = sqrt((R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]) - corner[1].y*corner[1].y);
						 corner[3].y = corner[1].y;
						 corner[4].y = sqrt((R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]) - corner[2].x*corner[2].x);
						 corner[4].x = corner[2].x;
	                     SingleAera = (corner[4].y - corner[2].y)*CubeWidth;
						 SingleAera = SingleAera + ((corner[3].x-corner[1].x)+CubeWidth)*(corner[3].y-corner[4].y)*0.5;
						 Line = sqrt((corner[3].y-corner[4].y)*(corner[3].y-corner[4].y)+(corner[4].x-corner[3].x)*(corner[4].x-corner[3].x));
						 SingleAera = SingleAera + LineAera(Line,R[i]-t[i]-f[i]);
					 }
				 }
				 else if (flag[0]==1&&flag[1]==0)
				 {
					 corner[3].x = corner[2].x;
					 corner[3].y = sqrt((R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]) - corner[2].x*corner[2].x);
					 SingleAera = ((corner[3].y - corner[2].y)+(corner[1].y-corner[0].y))*CubeWidth*0.5;
					 Line = sqrt((corner[1].y-corner[3].y)*(corner[1].y-corner[3].y)+CubeWidth*CubeWidth);
					 SingleAera = SingleAera + LineAera(Line,R[i]-t[i]-f[i]);
				 }
				 else if (flag[0]==0&&flag[1]==1)
				 {
					 corner[3].y = corner[1].y;
					 corner[3].x = sqrt((R[i]-t[i]-f[i])*(R[i]-t[i]-f[i]) - corner[1].y*corner[1].y);
					 SingleAera = ((corner[3].x-corner[1].x)+(corner[2].x-corner[0].x))*CubeWidth*0.5;
					 Line = sqrt((corner[2].x-corner[3].x)*(corner[2].x-corner[3].x)+CubeWidth*CubeWidth);
					 SingleAera = SingleAera + LineAera(Line,R[i]-t[i]-f[i]);
				 }
				 else if(flag[0]==1&&flag[1]==1)
				 {
					 SingleAera = (corner[1].y-corner[0].y)*(corner[2].x-corner[0].x)*0.5;
					 Line = sqrt((corner[1].y-corner[0].y)*(corner[1].y-corner[0].y)+(corner[2].x-corner[0].x)*(corner[2].x-corner[0].x));
					 SingleAera = SingleAera + LineAera(Line,R[i]-t[i]-f[i]);
				 }
			 TotlaAera = TotlaAera + SingleAera;
			 WStep = WStep + StepWidth;
			 }
		 HStep = HStep + StepWidth;
		 }
    next:
	QAear = R[i]*R[i]*PI*0.25;
	Percent[i] = 1.0-TotlaAera/QAear;
	cout<<"percent:"<<Percent[i]<<endl;
	}
	fclose(infile);
	infile=fopen("c:\\Output.out","w");   
	for (int i=0;i<CaseNum;i++)
	{
		fprintf(infile,"Case #%d: %6f\n",i+1,Percent[i]);
	}
	fclose(infile);
}

