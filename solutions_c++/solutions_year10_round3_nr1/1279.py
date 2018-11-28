#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstdlib>
#include<queue>
#include<cstring>
#include<map>
#include<iostream>

using namespace std;


struct punct{
		int x;
		int y;
		};


int min(int a,int b)
{
	if(a<b)
		return a;
	return b;
}

int max(int a,int b)
{
	if(a>b)
		return a;
	return b;
}


int det(int a,int b,int c,int d)
{

	if(a==b)
	{
		if((d>=b && c<=a) || (d<=b && c>=a))
			return 1;
	}
	if(c==d)
	{
		if((b>=d && a<=c) || (b<=d && a>=c))
			return 1;
	}

	
	if(d>=a && d<=b)
	{
		if(c>=a)
			return 1;
	}

	if(d>=b && d<=a)
	{
		if(c<=a)
			return 1;
	}


	if(c>=a && c<=b)
	{
		if(d<=b)
			return 1;
	}

	if(c>=b && c<=a)
	{
		if(d>=b)
			return 1;
	}

	if(a>=c && a<=d)
	{
		if(b<=d)
			return 1;
	}

	if(a>=d && a<=c)
	{
		if(b>=d)
			return 1;
	}


	if(b>=c && b<=d)
	{
		if(a>=c)
			return 1;
	}

	if(b>=d && b<=c)
	{
		if(a<=c)
			return 1;
	}

	if((a>max(c,d) && b<min(c,d)) || (a<min(c,d) && b>max(c,d)))
		return 1;
	if((c>max(a,b) && d<min(a,b)) || (c<min(a,b) && d>max(a,b)))
		return 1;
	return 0;
}
	
	
int  main()
{
	int t,a,b,c,d,n,i,count=0,j,k;
	punct p[1000];
	FILE *f=fopen("A.in","r");
	FILE *g=fopen("A.out","w");

	fscanf(f,"%i",&t);

	for(i=0;i<t;i++)
	{
		count=0;
		fscanf(f,"%i",&n);
		for(j=0;j<n;j++)
			fscanf(f,"%i%i",&p[j].x,&p[j].y);

		for(j=0;j<n;j++)
		{
			for(k=j+1;k<n;k++)
				count+=det(p[j].x,p[j].y,p[k].x,p[k].y);
		}

		fprintf(g,"%s%i%s%i\n","Case #",i+1,": ",count);
	}
	fclose(f);
	fclose(g);
	return 0;
}
			
	

	


























	


	
