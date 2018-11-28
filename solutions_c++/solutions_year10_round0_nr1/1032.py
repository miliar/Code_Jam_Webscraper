#include<stdio.h>

int main()
{
	FILE	*fin,*fout;
	fin = fopen("\A-large.in","r");
	fout = fopen("\A-large.out","w");
	
	int cn,t,n,k;
	fscanf(fin,"%d",&t);
	for(cn=1;cn<=t;cn++)
	{
		fscanf(fin,"%d%d",&n,&k);
		if((k+1)%(1<<n)==0)
			fprintf(fout,"Case #%d: ON\n",cn);
		else
			fprintf(fout,"Case #%d: OFF\n",cn);
	}
}
