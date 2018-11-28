#include<conio.h>
#include<iostream.h>
#include<stdio.h>

void main()
{
int t,n[30],no,i,j,f,j1;
double m,k;
FILE  *infile, *outfile;
 infile  = fopen("A-small.in",  "r");
 outfile = fopen("1.out", "w");

 fscanf(infile,"%d",&t);
 for(i=0;i<t;i++)
	{
	fscanf(infile,"%d%lf",&no,&k);
	for(j=0;j<no;j++)
		n[j]=0;
	for(m=0;m<k;m++)
		{
		for(j=no-1;j>0;j--)
			{
                        f=0;
			for(j1=0;j1<j;j1++)
				if(n[j1]==0)
					f=1;
			if(f==0)
				{
				if(n[j]==0)
					n[j]=1;
				else
					n[j]=0;
				}
			}
		if(n[0]==0)
			n[0]=1;
		else
                       	n[0]=0;
		}

	fprintf(outfile,"\nCase #%d: ",i+1);
	
	f=0;
	for(j=0;j<no;j++)
		if(n[j]==0)
			f=1;
	if(f==1)
		{
		fprintf(outfile,"OFF");
	        }
	else
		{
		fprintf(outfile,"ON");
		}
	}
 getch();
 }
