
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#define MAX 250
#define MORE 1000
int t,h,w;
int i,j,k,x;
int m[101][101];
char l[101][101];
void flow(int i,int j,int &x,int &y)
{
	int t1,t2;
	bool low=false;
	if(i-1>=0)
	{
		if(m[i][j]>m[i-1][j])
		{
			low=true;
			t1=i-1;
			t2=j;
		}
	}
	if(j-1>=0)
	{
		if(low==false)
		{
			if(m[i][j]>m[i][j-1])
			{
				t1=i;
				t2=j-1;
				low=true;
			}
		}
		else
		{
			if(m[t1][t2]>m[i][j-1])
			{
				t1=i;
				t2=j-1;
			}
		}
	}
	if(j+1<w)
	{
		if(low==false)
		{
			if(m[i][j]>m[i][j+1])
			{
				t1=i;
				t2=j+1;
				low=true;
			}
		}
		else
		{
			if(m[t1][t2]>m[i][j+1])
			{
				t1=i;
				t2=j+1;
			}
		}
	}

	if(i+1<h)
	{
		if(low==false)
		{
			if(m[i][j]>m[i+1][j])
			{
				t1=i+1;
				t2=j;
				low=true;
			}
		}
		else
		{
			if(m[t1][t2]>m[i+1][j])
			{
				t1=i+1;
				t2=j;
			}
		}
	}
	if(low==false)
	{
		x=-1;
		y=-1;
	}
	else
	{
		x=t1;
		y=t2;
	}
	
}
void get(int i,int j,char c)
{ 
   l[i][j]=c;
   int x,y,t1,t2;
   flow(i,j,x,y);
   if(x!=-1)
   { 
      get(x,y,c);
   }
   if(i-1>=0&&l[i-1][j]==0)
   {
	   flow(i-1,j,t1,t2);
	   if(t1==i&&t2==j)
	   {
		   get(i-1,j,c);
	   }
   }
   if(j-1>=0&&l[i][j-1]==0)
   {
	   flow(i,j-1,t1,t2);
	   if(t1==i&&t2==j)
	   {
		   get(i,j-1,c);
	   }
   }
   if(i+1<h&&l[i+1][j]==0)
   {
	   flow(i+1,j,t1,t2);
	   if(t1==i&&t2==j)
	   {
		   get(i+1,j,c);
	   }
   }
   if(j+1>=0&&l[i][j+1]==0)
   {
	   flow(i,j+1,t1,t2);
	   if(t1==i&&t2==j)
	   {
		   get(i,j+1,c);
	   }
   }
}
int main()
{
	FILE *in;
	in=fopen("d:\\B-large.in.txt","rb");
	FILE *out;
	out=fopen("d:\\B-large.out.txt","wb");
	fscanf(in,"%d",&t);
	char c='a'-1;
	int x,y;
	for(k=1;k<=t;k++)
	{
		fscanf(in,"%d %d",&h,&w);
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				fscanf(in,"%d",&m[i][j]);
				l[i][j]=0;
			}
		}
		c='a'-1;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(l[i][j]==0)
				{
					c++;
					get(i,j,c);
				}
			}
		}
		fprintf(out,"Case #%d:\n",k);
		//printf("Case #%d:\n",k);
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				//printf("%c ",l[i][j]);
				fprintf(out,"%c ",l[i][j]);
			}
			fprintf(out,"\n");
			//printf("\n");
		}
	}
}


