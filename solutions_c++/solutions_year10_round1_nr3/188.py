#include<stdio.h>

FILE *in,*out,*dbg;
void io()
{
	in =fopen("c.in" ,"r");
	out=fopen("c.out","w");
	dbg=fopen("debug.txt","w");
}

int test(int x,int y)
{
	int z;
	int a;
	if( x<y ) { z=x; x=y; y=z; }
	if( x%y==0 )
	{
		if( x==y ) return 0;
		return 1;
	}
	for(a=y*(x/y);a>0;a-=y)
	{
		if( test(x-a,y)==0 ) return 1;
	}
	return 0;
}

int main()
{
	io();
	int k;
	int i1,i2,j1,j2;
	int o;
	int a,s,d;
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%d%d%d%d",&i1,&i2,&j1,&j2);
		o=0;
		for(s=i1;s<=i2;s++) for(d=j1;d<=j2;d++)
		{
			o+=test(s,d);
		}
		fprintf(out,"Case #%d: ",a+1);
		fprintf(out,"%d\n",o);
	}
	return 0;
}