#include<stdio.h>
#include<string.h>
#include<vector.h>
FILE *in,*out,*dbg;

int abs(int x) { if( x>0 ) return x; return -x; }

int main()
{
	in =fopen("a.in" ,"r");
	out=fopen("a.out","w");
//	dbg=fopen("debug.txt","w");
	int tests,test;
	int n,i,x,y,z,w,t,u,a;
	char c;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d",&n);
		x=1;
		y=1;
		z=0;
		w=0;
		t=0;
		for(a=0;a<n;a++)
		{
			fscanf(in," %c %d",&c,&i);
			if( c=='B' )
			{
				u=abs(i-x);
				if( u>=z ) { w+=u-z+1; t+=u-z+1; }
				else { w=1; t++; }
				z=0;
				x=i;
			}
			else
			{
				u=abs(i-y);
				if( u>=w ) { z+=u-w+1; t+=u-w+1; }
				else { z=1; t++; }
				w=0;
				y=i;
			}
		}
		fprintf(out,"Case #%d: ",test+1);
		fprintf(out,"%d\n",t);
	}
	return 0;
}