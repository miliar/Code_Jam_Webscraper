#include<stdio.h>
FILE *in,*out;
int h[2097152];
int main()
{
	in =fopen("c.in" ,"r");
	out=fopen("c.out","w");
	int tests,test;
	int m,n,o;
	int c,k,x,low;
	int a,s;
	fscanf(in,"%d",&tests);
	for(test=0;test<tests;test++)
	{
		fscanf(in,"%d%d",&m,&n);
		c=0;
		k=1;
		x=n;
		while( x>0 ) { x/=10; c++; k*=10; }
		for(a=0;a<=n;a++) h[a]=0;
		for(a=m;a<=n;a++)
		{
			x=a;
			low=x;
			for(s=1;s<c;s++)
			{
				x=(x+(x%10)*k)/10;
				if( x<low ) low=x;
			}
			h[low]++;
		}
		o=0;
		for(a=0;a<=n;a++) o+=h[a]*(h[a]-1)/2;
		fprintf(out,"Case #%d: ",test+1);
		fprintf(out,"%d\n",o);
	}
	return 0;
}