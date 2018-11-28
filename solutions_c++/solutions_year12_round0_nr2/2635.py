#include<stdio.h>
FILE *in,*out;
int main()
{
	in =fopen("b.in" ,"r");
	out=fopen("b.out","w");
	int tests,test;
	int n,k,t,o;
	int a,s;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d%d%d",&n,&k,&t);
		o=0;
		for(a=0;a<n;a++)
		{
			fscanf(in,"%d",&s);
			if( (s+2)/3>=t ) o++;
			else if( s%3!=1 && s>=3 && s<=27 && k>0 && (s+4)/3>=t ) { k--; o++; }
		}
		fprintf(out,"Case #%d: ",test+1);
		fprintf(out,"%d\n",o);
	}
	return 0;
}
/*
	0 : 0 0 0
	1 : 0 0 1
	2 : 0 1 1
	3 : 1 1 1 , 0 1 2
	4 : 1 1 2
	5 : 1 2 2 , 1 1 3
	...
	25 : 8 8 9
	26 : 8 9 9 , 8 8 10
	27 : 9 9 9 , 8 9 10
	28 : 9 9 10
	29 : 9 10 10
	30 : 10 10 10
*/