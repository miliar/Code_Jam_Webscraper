#include <cstdio>
#include <cmath>

int main()
{
	FILE*rd=fopen("C-small-attempt0.in","r");
	FILE*wt=fopen("C-small-attempt0.out","w");
	if(rd==NULL||wt==NULL)
		printf("error open file");
	int ln,n,k,r;

	fscanf(rd,"%d",&ln);
	fgetc(rd);

	for(int i=0;i<ln;i++)
	{
		fprintf(wt,"Case #%d: ",i+1);
		fscanf(rd,"%d %d %d",&r,&k,&n);
		fgetc(rd);
		int *gs=new int[n];
		for(int j=0;j<n;j++)
			fscanf(rd,"%d",&gs[j]);

		int pt=0;
		long long earn=0;
		int once=0;

		for(int j=0;j<r;j++)
		{
			once=0;
			int t=0;
			while((once+=gs[pt])<=k&&t++<n)
			{
				pt=(pt+1)%n;
			}
			earn+=once-gs[pt];
		}
		fprintf(wt,"%d",earn);
		fputc('\n',wt);
	}


	return 0;
}