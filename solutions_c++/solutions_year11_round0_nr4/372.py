#include<stdio.h>
#include<string.h>
#include<vector.h>
FILE *in,*out,*dbg;

int main()
{
	in =fopen("d.in" ,"r");
	out=fopen("d.out","w");
//	dbg=fopen("debug.txt","w");
	int tests,test;
	int n,i,o,a;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d",&n);
		o=n;
		for(a=1;a<=n;a++)
		{
			fscanf(in,"%d",&i);
			if( i==a ) o--;
		}
		fprintf(out,"Case #%d: ",test+1);
		fprintf(out,"%d\n",o);
	}
	return 0;
}