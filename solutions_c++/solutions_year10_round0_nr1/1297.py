#include "stdio.h"
#include "stdlib.h"

const char finput[]="input.txt";
const char foutput[]="output.txt";
FILE *fi,*fo;
int t,n,k;
int i,x,temp;

void process2()
{
	fscanf(fi,"%d %d\n",&n,&k);
	temp=1;
	temp=temp << n;
	if ((k+1)%temp) fprintf(fo,"Case #%d: OFF\n",x+1); else fprintf(fo,"Case #%d: ON\n",x+1);
}

void process()
{
	fi=fopen(finput,"r");
	fo=fopen(foutput,"w");
	fscanf(fi,"%d\n",&t);
	for (x=0;x<t;x++) process2();
	fclose(fi);
	fclose(fo);
}

void main()
{
	process();
}