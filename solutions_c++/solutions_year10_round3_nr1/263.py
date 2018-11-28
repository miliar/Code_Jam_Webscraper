#include <stdio.h>

int a[1000], b[1000];

int main()
{
	int t,n,i,j,k,l;
	FILE* fp=fopen("input.in","r"),*fp2=fopen("output.out","w");

	fscanf(fp,"%d",&t);

	for (i=1; i<=t; i++)
	{
		l=0;
		fscanf(fp,"%d",&n);
		for (j=0; j<n; j++)
		{
			fscanf(fp,"%d%d",a+j,b+j);
		}

		for (j=0; j<n; j++)
		{
			for (k=0; k<n; k++)
			{
				if (j==k) continue;
				else if ((a[j]-a[k])*(b[j]-b[k]) < 0) l++;
			}
		}

		fprintf(fp2,"Case #%d: %d\n",i,l/2);
	}
	return 0;
}