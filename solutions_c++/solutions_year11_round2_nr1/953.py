#include<stdio.h>

int a[400][400];
double la[400];
double wp[400];
double wp1[400];
double wp2[400];
double owp[400];
double oowp[400];
char c[400][400];

void main()
{
	int i,j,k,l,t,n,m;
	FILE *fp1;
	FILE *fp2;
	fp1=fopen("input.in","r");
	fp2=fopen("output.out","w");
	fscanf(fp1,"%d",&t);
	for(l=1;l<=t;l++)
	{
		fscanf(fp1,"%d",&n);
		for(j=1;j<=n;j++)
		{
			wp1[j]=wp2[j]=0;
			wp[j]=owp[j]=oowp[j]=0;
			fscanf(fp1,"%s",c[j]);
			for(k=0;k<n;k++)
			{
				if(c[j][k]=='1')
				{
					wp1[j]+=1;
					wp2[j]+=1;
					a[j][k+1]=1;
				}
				else if(c[j][k]=='0')
				{
					wp2[j]+=1;
					a[j][k+1]=2;
				}
				else
					a[j][k+1]=0;
			}
			wp[j]=wp1[j]/wp2[j];
		}
		for(j=1;j<=n;j++)
		{
			m=0;
			for(k=1;k<=n;k++)
			{
				if(a[j][k]==1)
				{
					owp[j]+=wp1[k]/(wp2[k]-1);
					m++;
				}
				if(a[j][k]==2)
				{
					owp[j]+=(wp1[k]-1)/(wp2[k]-1);
					m++;
				}
			}
			owp[j]/=m;
		}
		for(j=1;j<=n;j++)
		{
			m=0;
			for(k=1;k<=n;k++)
			{
				if(a[j][k]!=0)
				{
					oowp[j]+=owp[k];
					m++;
				}
			}
			oowp[j]/=m;
		}
		for(j=1;j<=n;j++)
			la[j]=0.25*wp[j]+0.5*owp[j]+0.25*oowp[j];
		fprintf(fp2,"Case #%d:\n",l);
		for(j=1;j<=n;j++)
			fprintf(fp2,"%lf\n",la[j]);
	}
	fclose(fp1);
	fclose(fp2);
}