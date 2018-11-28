#include <cstdio>
#include <cmath>

int main()
{
	FILE*rd=fopen("A-large.in","r");
	FILE*wt=fopen("A-large.out","w");
	if(rd==NULL||wt==NULL)
		printf("error open file");
	int ln,n,k;

	fscanf(rd,"%d",&ln);
	fgetc(rd);

	for(int i=0;i<ln;i++)
	{
		fprintf(wt,"Case #%d: ",i+1);
		fscanf(rd,"%d %d",&n,&k);
		fgetc(rd);
		long long x=1;
		if(((k+1)%(x<<n))==0)
			fputs("ON",wt);
		else fputs("OFF",wt);
		fputc('\n',wt);
	}


	return 0;
}