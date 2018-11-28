#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

#define MAX_N 1000005

using namespace std;

int ttt,iii,n,s,r,x;
double t;
int d,b,e,w,i,j;
int sp[MAX_N];
double tmp[MAX_N];
double answer;

int main()
{
	FILE *fin=fopen("A-large.in","r");
	FILE *fout=fopen("A-large.out","w");
	fscanf(fin,"%d",&ttt);
	for(iii=0;iii<ttt;iii++)
	{
		fscanf(fin,"%d %d %d %lf %d",&x,&s,&r,&t,&n);
		//fprintf(fout,"YY %d %d\n",s,r);
		d=r-s;
		for(i=0;i<x;i++)
		{
			sp[i]=s;
		}
		for(i=0;i<n;i++)
		{
			fscanf(fin,"%d %d %d",&b,&e,&w);
			//fprintf(fout,"XX %d %d %d\n",b,e,w);
			for(j=b;j<e;j++)
			{
				sp[j]=w+s;
			}
		}
		for(i=0;i<MAX_N;i++)
		{
			tmp[i]=0;
		}
		for(i=0;i<x;i++)
		{
			tmp[sp[i]]++;
		}
		answer=0.0;
		//fprintf(fout,"%d\n",d);
		for(i=1;i<MAX_N;i++)
		{
			if(tmp[i]!=0)
			{
				if(t*(i+d)>tmp[i])
				{
					answer+=(tmp[i]/(double)(i+d));
					//fprintf(fout,"%d %d\n",tmp[i],i+d);
					t-=(tmp[i]/(double)(i+d));
					tmp[i]=0;
				}
				else
				{
					answer+=(t);
					//fprintf(fout,"%lf %d\n",t,i+d);
					tmp[i]-=t*(i+d);
					t=0;
				}
			}
		}
		for(i=1;i<MAX_N;i++)
		{
			if(tmp[i]!=0)
			{
			answer+=(tmp[i]/(double)(i));
			//fprintf(fout,"%d %d\n",tmp[i],i);
			}
		}
		fprintf(fout,"Case #%d: %.9lf\n",iii+1,answer);
	}
	return 0;
}