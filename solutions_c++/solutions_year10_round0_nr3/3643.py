
#include<conio.h>
#include<iostream.h>
#include<stdio.h>
#include<fstream.h>

void main()
{
int t,n[1000],no,i,j,start,i1,e;
double m,k,r,c,f;
FILE  *infile, *outfile;
 infile  = fopen("C-small.in","r");
 outfile = fopen("3.out", "w");

 fscanf(infile,"%d",&t);
 for(i=0;i<t;i++)
	{
	c=0;
	fscanf(infile,"%lf%lf%d",&r,&k,&no);
	for(j=0;j<no;j++)
		fscanf(infile,"%d",&n[j]);
	start=0;
	i1=0;
	do
		{
		f=0;
		e=start;
		while((f+n[start])<=k)
			{
			f=f+n[start++];
			if(start>=no)
				{
				start=0;
				}
			if(start==e)
				break;
			}
		c+=f;
		i1++;
		}
		while(i1<r);
	fprintf(outfile,"\nCase #%d",(i+1));
	fprintf(outfile,": %.0lf",c);
	}
 getch();
 }
