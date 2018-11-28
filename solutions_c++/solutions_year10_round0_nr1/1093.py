#include<stdio.h>
FILE *in,*out,*dbg;
void io()
{
	in =fopen("a.in" ,"r");
	out=fopen("a.out","w");
	dbg=fopen("debug.txt","w");
}
int main()
{
	io();
	int n,c;
	int k;
	int a;
	fscanf(in,"%d",&k);
	for(a=0;a<k;a++)
	{
		fscanf(in,"%d%d",&n,&c);
		fprintf(out,"Case #%d: ",a+1);
		fprintf(out,"%s",(c%(1<<n)==(1<<n)-1?"ON":"OFF"));
		fprintf(out,"\n");
	}
	return 0;
}