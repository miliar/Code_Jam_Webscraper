#include<stdio.h>
#include<conio.h>
#include<iostream.h>
float count(int *g,int r,int n,int k);
int main()
{
	clrscr();
	FILE *inf,*outf;
	int r,k,n,*out,temp,*g;
	float c;
	int t,i,j;
	inf=fopen("input.in","r");
	outf=fopen("output.in","w");
	if(inf==0)
		cout<<"File not found..";
	fscanf(inf,"%d",&t);
	for(i=0;i<t;i++)
	{
		fscanf(inf,"\n%d %d %d\n",&r,&k,&n);
		g=new int[n];
		for(j=0;j<n;j++)
			fscanf(inf,"%d",&g[j]);
		c=count(g,r,n,k);
		fprintf(outf,"Case #%d: %.0f\n",i+1,c);
	}
	fclose(inf);
	fclose(outf);
	return(0);
}

float count(int *g,int r,int n,int k)
{
	int i,point=0,filled=0,temp;
	float count=0;
	for(i=0;i<r;i++)
	{
		filled=0;
		temp=point;
		while((filled+g[point])<=k)
		{
			filled+=g[point];
			count+=g[point];
			point=(point+1)%n;
			if(point==temp)
				break;
		}
	}
	return(count);
}
