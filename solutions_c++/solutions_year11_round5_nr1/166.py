#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>

#define MAX_L 105
#define MAX_U 105
#define ROUND 50

using namespace std;

FILE *fin=fopen("A-large.in","r");
FILE *fout=fopen("A-large.out","w");

int t,iii,ii,i,j,ir;
int w,l,u,g;
double xnow;
double xl;
double x1[MAX_U],y11[MAX_U];
double x2[MAX_L],y2[MAX_L];
double ytmp1,ytmp2;
double ynow1,ynow2;
double yl1,yl2;
double le,ri;
double mi;
double area;
double res;

double comp(double x)
{
	i=1;
	j=1;
	res=0.0;
	yl1=y11[0];
	yl2=y2[0];
	xl=0.0;
	xnow=0.0;
	while(min(x1[i],x2[j])<=x&&i<l&&j<u)
	{
		if(x1[i]==x2[j])
		{
			xnow=x1[i];
			ynow1=y11[i];
			ynow2=y2[j];
			res+=((ynow2+yl2)/2.0)*(xnow-xl);
			res-=((ynow1+yl1)/2.0)*(xnow-xl);
			yl1=ynow1;
			yl2=ynow2;
			xl=xnow;
			i++;
			j++;
		}
		else if(x1[i]>x2[j])
		{
			xnow=x2[j];
			ynow1=y11[i-1]+(xnow-x1[i-1])*(y11[i]-y11[i-1])/(x1[i]-x1[i-1]);
			ynow2=y2[j];
			res+=((ynow2+yl2)/2.0)*(xnow-xl);
			res-=((ynow1+yl1)/2.0)*(xnow-xl);
			yl1=ynow1;
			yl2=ynow2;
			xl=xnow;
			j++;
		}
		else
		{
			xnow=x1[i];
			ynow1=y11[i];
			ynow2=y2[j-1]+(xnow-x2[j-1])*(y2[j]-y2[j-1])/(x2[j]-x2[j-1]);
			res+=((ynow2+yl2)/2.0)*(xnow-xl);
			res-=((ynow1+yl1)/2.0)*(xnow-xl);
			yl1=ynow1;
			yl2=ynow2;
			xl=xnow;
			i++;
		}
		//fprintf(fout,"KK %lf %lf %lf: %lf: %lf %lf\n",yl1,yl2,xl,res,x1[i],x2[j]);
	}
	//fprintf(fout,"DD %d %d %d %d %lf %lf %lf",i,u,j,l,x1[i],x2[j],x);
	if(i<l&&j<u&&x1[i]>x&&x2[j]>x)
	{
		xnow=x;
		ynow1=y11[i-1]+(xnow-x1[i-1])*(y11[i]-y11[i-1])/(x1[i]-x1[i-1]);
		ynow2=y2[j-1]+(xnow-x2[j-1])*(y2[j]-y2[j-1])/(x2[j]-x2[j-1]);
		res+=((ynow2+yl2)/2.0)*(xnow-xl);
		res-=((ynow1+yl1)/2.0)*(xnow-xl);
		//fprintf(fout,"LLL %lf %lf %lf\n",xnow,ynow1,ynow2);
	}
	return res;
}

double binarysearch(double rat)
{
	le=0.0;
	ri=(double)w;
	for(ir=0;ir<ROUND;ir++)
	{
		mi=(le+ri)/2.0;
		if(comp(mi)>=area*rat)
		{
			ri=mi;
		}
		else
		{
			le=mi;
		}
	}
	return ri;
}

int main()
{
	fscanf(fin,"%d",&t);
	for(iii=0;iii<t;iii++)
	{
		fscanf(fin,"%d %d %d %d",&w,&l,&u,&g);
		for(i=0;i<l;i++)
		{
			fscanf(fin,"%lf %lf",&x1[i],&y11[i]);
		}
		for(i=0;i<u;i++)
		{
			fscanf(fin,"%lf %lf",&x2[i],&y2[i]);
		}
		fprintf(fout,"Case #%d:\n",iii+1);
		area=comp((double)w);
		for(ii=1;ii<g;ii++)
		{
			fprintf(fout,"%.6lf\n",binarysearch(((double)ii)/((double)g)));
		}
	}
	return 0;
}