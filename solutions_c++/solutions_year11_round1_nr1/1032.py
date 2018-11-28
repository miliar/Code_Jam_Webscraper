#include<stdio.h>
#include<string.h>
#include<vector.h>
FILE *in,*out,*dbg;

int main()
{
	long long n,p,q,t,k;
	in =fopen("a.in" ,"r");
	out=fopen("a.out","w");
//	dbg=fopen("debug.txt","w");
	int tests,test;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%I64d%I64d%I64d",&n,&p,&q);
		t=1;
		if( q==100 && p!=100 ) t=0;
		if( q==0 && p!=0 ) t=0;
		k=1;
		if( p%2!=0 ) k*=2;
		if( p%4!=0 ) k*=2;
		if( p%5!=0 ) k*=5;
		if( p%25!=0 ) k*=5;
		if( k>n ) t=0;
		fprintf(out,"Case #%d: ",test+1);
		fprintf(out,(t==1?"Possible":"Broken"));
		fprintf(out,"\n");
	}
	return 0;
}