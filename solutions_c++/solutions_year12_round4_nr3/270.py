#include<stdio.h>
#include<string.h>
#include<vector.h>
FILE *in,*out;
int i[16384];
int o[16384];
int b[16384];
int main()
{
	in =fopen("c.in" ,"r");
	out=fopen("c.out","w");
	int tests,test;
	int n;
	int t;
	int a,s;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fprintf(out,"Case #%d:",test+1);
		fscanf(in,"%d",&n);
		for(a=0;a<n-1;a++) fscanf(in,"%d",&i[a]);
		o[n-1]=1000000000;
		o[n]=1000000000;
		for(a=0;a<n;a++) b[a]=0;
		b[n-1]=1;
		b[n]=1;
		for(a=n-2;a>=0;a--)
		{
			t=i[a]-1;
			if( b[t]==0 ) break;
			for(s=t+1;s<=n;s++) if( b[s]==1 ) break;
			o[a]=o[t]-(o[s]-o[t])*(t-a)/(s-t)-500;
			for(s=a+1;s<t;s++) b[s]=0;
			b[a]=1;
		}
		if( a!=-1 )
		{
			fprintf(out," Impossible\n");
		}
		else
		{
///*
for(a=0;a<n-1;a++)
{
	double g,v;
	g=0;
	t=-1;
	for(s=a+1;s<n;s++)
	{
		v=(double)(o[s]-o[a])/(double)(s-a);
		if( v>g ) { g=v; t=s; }
	}
	if( t!=i[a]-1 ) fprintf(out,"!");
}
//*/
			for(a=0;a<n;a++) fprintf(out," %d",o[a]);
			fprintf(out,"\n");
		}
	}
	return 0;
}