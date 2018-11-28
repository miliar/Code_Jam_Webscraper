#include<stdio.h>
#include<math.h>
int main()
{
	long c=0,i,a,x,p;
	int t,n,k;

	FILE *fp = fopen("A-large.in","r") , *ofp = fopen("A-large.out","w");
	fscanf(fp,"%d",&t);
	for(c=1;c<=t;c++)
	{
		fscanf(fp,"%d %d",&n,&k);
		p = pow(2,n);
		if((k+1)%p==0)
			fprintf(ofp,"Case #%d: ON\n",c);
		else
			fprintf(ofp,"Case #%d: OFF\n",c);
	}
	return 0;
}