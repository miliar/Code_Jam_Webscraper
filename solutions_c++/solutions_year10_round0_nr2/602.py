#include "stdio.h"
#include "stdlib.h"

const char finput[]="input.txt";
const char foutput[]="output.txt";
FILE *fi,*fo;
int x,c;
int n;
long int t[1000],t2[1000];
long int y;
long int i;

void UCLN(long int &a,long int b)
{
	if (a==0) {a=b;return;}
	if (b==0) return;
	while (true)
	{
		if (a>b)
			{
				a%=b;
				if (a==0) {a=b;return;}
			}
		else 
			{
				b%=a;
				if (b==0) return;
			}
	}
}

void process()
{
	fscanf(fi,"%d",&n);
	for (i=0;i<n;i++) fscanf(fi,"%ld",&t[i]);
	fscanf(fi,"\n");

	for (i=1;i<n;i++) {t2[i]=t[i]-t[i-1];if (t2[i]<0) t2[i]=-t2[i];}
	t2[0]=t[0]-t[n-1];
	if (t2[0]<0) t2[0]=-t2[0];
	for (i=1;i<n;i++) UCLN(t2[0],t2[i]);
	y=t[0]%t2[0];
	if (y) y=t2[0]-y;

	fprintf(fo,"Case #%d: %ld\n",x+1,y);
}

void inout()
{
	fi=fopen(finput,"r");
	fo=fopen(foutput,"w");
	fscanf(fi,"%d\n",&c);
	for (x=0;x<c;x++) process();
	fclose(fi);
	fclose(fo);
}

void main()
{
	inout();
}