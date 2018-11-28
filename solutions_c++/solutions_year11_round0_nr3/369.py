#include<stdio.h>
#include<string.h>
#include<vector.h>
FILE *in,*out,*dbg;

int main()
{
	in =fopen("c.in" ,"r");
	out=fopen("c.out","w");
//	dbg=fopen("debug.txt","w");
	int tests,test;
	int n,m,i,a,s,d;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d",&n);
		s=0;
		d=0;
		for(a=0;a<n;a++)
		{
			fscanf(in,"%d",&i);
			if( a==0 || i<m ) m=i;
			s^=i;
			d+=i;
		}
		fprintf(out,"Case #%d: ",test+1);
		if( s==0 ) fprintf(out,"%d\n",d-m); else fprintf(out,"NO\n");
	}
	return 0;
}