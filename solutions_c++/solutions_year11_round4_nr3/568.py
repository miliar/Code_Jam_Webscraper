#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int t,n;

int main()
{
	int i,j,k,l,o,p,la,j1;
	FILE *fp1=fopen("input.in","r");
	FILE *fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(fp1,"%d",&n);
		la=0;
		for(j=2;j<=n;j++)
		{
			o=sqrt(j);
			p=0;
			for(k=2;k<=o;k++)
				if(j%k==0)
					p++;
			if(p==0)
			{
				j1=j;
				la--;
				for(k=1;k<k+1;k++)
				{
					if(n>=j1)
						la++;
					else
						break;
					j1*=j;
				}
			}
		}
		if(n!=1)
			la++;
		fprintf(fp2,"Case #%d: %d\n",i,la);
	}
	fclose(fp1);
	fclose(fp2);
}