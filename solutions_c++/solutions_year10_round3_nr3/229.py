#include "stdio.h"
#include "stdlib.h"

const char *finput="input.txt";
const char *foutput="output.txt";
FILE *fi,*fo;
int t;
int x,k,min;

int m,n,nn,md,mc,flag;
int a[512][512];
int b[513];
int i,j,ii;
char c;

//-----------------------------------------------------------------------------
void initp()
{
	for (i=512;i;i--) b[i]=0;
	k=0;
	min=(m>n?n:m);
}
//-----------------------------------------------------------------------------
void inputp()
{
	fscanf(fi,"%d%d\n",&m,&n);
	nn=n/4;
	for (i=0;i<m;i++)
	{
		for (j=0;j<nn;j++)
		{
			fscanf(fi,"%c",&c);
			if (c>58) c-=55; else c-=48;
			a[i][j*4]=(c&8)&&1;
			a[i][j*4+1]=(c&4)&&1;
			a[i][j*4+2]=(c&2)&&1;
			a[i][j*4+3]=(c&1);
		}
		fscanf(fi,"\n");
	}
}
//-----------------------------------------------------------------------------
void outputp()
{
	fprintf(fo,"Case #%d: %d\n",x,k);
	for (i=min;i;i--)
		if (b[i]) fprintf(fo,"%d %d\n",i,b[i]);
}
//-----------------------------------------------------------------------------
int checkfortable(int sx,int sy,int dx,int dy)
{
	int i,j;
	for (i=sx;i<dx;i++)
		for (j=sy;j<dy;j++)
		{
			if (a[i][j]==2) return 0;
			if (a[i][j]==a[i+1][j]) return 0;
			if (a[i][j]==a[i][j+1]) return 0;
		}
	for (i=sx;i<dx;i++)
	{
		if (a[i][dy]==2) return 0;
		if (a[i][dy]==a[i+1][dy]) return 0;
	}
	for (j=sy;j<dy;j++)
	{
		if (a[dx][j]==2) return 0;
		if (a[dx][j]==a[dx][j+1]) return 0;
	}
	if (a[dx][dy]==2) return 0;
	return 1;
}
void cleartable(int sx,int sy,int dx,int dy)
{
	int i,j;
	for (i=sx;i<=dx;i++)
		for (j=sy;j<=dy;j++)
			a[i][j]=2;
}
void processp()
{
	for (ii=min;ii;ii--)
	{
		flag=0;
		md=m-ii+1;
		mc=n-ii+1;
		for (i=0;i<md;i++)
			for (j=0;j<mc;j++)
				if (checkfortable(i,j,i+ii-1,j+ii-1)) {cleartable(i,j,i+ii-1,j+ii-1);b[ii]++;flag=1;}
		if (flag) k++;
	}
}
//-----------------------------------------------------------------------------
void ioprocess()
{
    fi=fopen(finput,"r");
    fo=fopen(foutput,"w");
    fscanf(fi,"%d\n",&t);
    for (x=1;x<=t;x++) 
    {
        inputp();
		initp();
        processp();
        outputp();
    }
    fclose(fi);
    fclose(fo);
}
//-----------------------------------------------------------------------------
int main()
{
    ioprocess();
}