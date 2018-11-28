#include "stdio.h"
#include "stdlib.h"

const char finput[]="input.txt";
const char foutput[]="output.txt";
FILE *fi,*fo;
int x,t;
long int r,k,n;
long int g[1000];
long long int money;
long int i,j;
int p;
int flag;

struct item
{
	long int v,n;
};
item g2[1000];

void process()
{
	money=0;
	fscanf(fi,"%ld %ld %ld\n",&r,&k,&n);
	for (i=0;i<n;i++) fscanf(fi,"%ld",&g[i]);
	fscanf(fi,"\n");

	for (i=0;i<n;i++) 
	{
		g2[i].v=g[i];
		flag=1;
		for (j=i+1;j<n;j++)
		{
			g2[i].v+=g[j];
			if (g2[i].v>k)
			{
				flag=0;
				g2[i].v-=g[j];
				g2[i].n=j;
				break;
			}
		}
		if (flag) for (j=0;j<i;j++)
		{
			g2[i].v+=g[j];
			if (g2[i].v>k)
			{

				flag=0;
				g2[i].v-=g[j];
				g2[i].n=j;
				break;
			}
		}
		if (flag) g2[i].n=i;
	}
	for (i=0,p=0;i<r;i++)
	{
		money+=g2[p].v;
		p=g2[p].n;
	}

	fprintf(fo,"Case #%d: %lld\n",x+1,money);
}

void inout()
{
	fi=fopen(finput,"r");
	fo=fopen(foutput,"w");
	fscanf(fi,"%d\n",&t);
	for (x=0;x<t;x++) process();
	fclose(fi);
	fclose(fo);
}

void main()
{
	inout();
}