#include "stdio.h"
#include "stdlib.h"

const char *finput="input.txt";
const char *foutput="output.txt";
FILE *fi,*fo;
int t;
int x,y;
int n;
int i,j;
int a[26];
//-----------------------------------------------------------------------------
void initp()
{
	y=0;
}
//-----------------------------------------------------------------------------
void inputp()
{
	fscanf(fi,"%d\n",&n);
}
//-----------------------------------------------------------------------------
void outputp()
{
	fprintf(fo,"Case #%d: %d\n",x,y);
}
//-----------------------------------------------------------------------------
void check(int k)
{
	int i,j,f;
	a[k]=n;
	j=k;
	while (j>1)
	{
	f=0;
	for (i=1;i<k;i++) if (a[i]==j) {f=i;break;}
	j=f;
	}
	if (j==1) {y++;y%=100003;return;}
}
void tryt(int k)
{
	int i;
	check(k);
	for (i=a[k-1]+1;i<n;i++)
	{
		a[k]=i;
		tryt(k+1);
	}
}
void processp()
{
	a[0]=1;
	tryt(1);
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