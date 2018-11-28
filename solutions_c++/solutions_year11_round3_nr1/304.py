#include<stdio.h>

int t,r,c,ip;
char a[105][105];

int main()
{
	FILE *fp1;
	FILE *fp2;
	int i,j,k,n,m;
	fp1=fopen("input.in","r");
	fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&t);
	for(i=1;i<=t;i++)
	{
		ip=0;
		fscanf(fp1,"%d %d",&r,&c);
		for(j=1;j<=r+1;j++)
			for(k=1;k<=c+1;k++)
				a[j][k]='.';
		for(j=1;j<=r;j++)
			fscanf(fp1,"%s",&a[j][1]);
		for(j=1;j<=r;j++)
		{
			for(k=1;k<=c;k++)
			{
				if(a[j][k]=='#')
				{
					if(a[j+1][k]=='#' && a[j][k+1]=='#' && a[j+1][k+1]=='#')
					{
						a[j][k]=47;
						a[j][k+1]=92;
						a[j+1][k]=92;
						a[j+1][k+1]=47;
					}
					else
					{
						ip=1;
					}
				}
			}
		}
		fprintf(fp2,"Case #%d:\n",i);
		if(ip==1)
			fprintf(fp2,"Impossible\n");
		else
		{
			for(j=1;j<=r;j++)
			{
				for(k=1;k<=c;k++)
				{
					fprintf(fp2,"%c",a[j][k]);
				}
				fprintf(fp2,"\n");
			}
		}
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}