#include "stdio.h"
#include "stdlib.h"

const char *finput="input.txt";
const char *foutput="output.txt";
FILE *fi,*fo;
int t;
int x,y;
int n;
struct itemx
{
	int a,b;
};
itemx a[1000];
int i,j,t1,t2;

//-----------------------------------------------------------------------------
void initp()
{
	y=0;
}
//-----------------------------------------------------------------------------
void inputp()
{
	fscanf(fi,"%d\n",&n);
	for (i=0;i<n;i++) fscanf(fi,"%d%d\n",&a[i].a,&a[i].b);
}
//-----------------------------------------------------------------------------
void outputp()
{
	fprintf(fo,"Case #%d: %d\n",x,y);
}
//-----------------------------------------------------------------------------
void processp()
{
	for (i=0;i<n-1;i++)
		for (j=i+1;j<n;j++)
		{
			t1=a[i].a-a[j].a;
			t2=a[i].b-a[j].b;
			if (t1*t2<0) y++;
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
        initp();
        inputp();
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