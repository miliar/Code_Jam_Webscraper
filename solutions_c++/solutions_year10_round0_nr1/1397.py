#include<stdio.h>

void main()
{
	FILE *in,*out;
	in = fopen("SnapperChain.in","r");
	out = fopen("SnapperChain.out","w+");
	int T,N,K,t;
	fscanf(in,"%d",&T);
	for(t=0;t<T;t++)
	{
		fscanf(in,"\n%d %d ",&N,&K);
		for(;N && (K&1);N--,K>>=1);
		fprintf(out,"Case #%d: %s\n",t+1,(N?"OFF":"ON"));
	}
	fclose(in);
	fclose(out);
}