#include <stdio.h>
#include <stdlib.h>
#include <string.h>
double wp[100],owp[100],oowp[100];
double calcwp(char arr[100][100],int n,int i,int di)
{
	int count=0,win=0;
	for(int j=0;j<n;j++)
	{
		if(i==j)
			continue;
		if(arr[i][j]=='.')
			continue;
		if(j==di)
			continue;
		count++;
		if(arr[i][j]=='1')
			win++;
	}
	return (double)win/count;
}
double calcowp(char arr[100][100],int n,int i)
{
	double wp1=0;
	int count=0;
	for(int j=0;j<n;j++)
	{
		if(i==j)
			continue;
		if(arr[i][j]=='.')
			continue;
		count++;
		wp1+=calcwp(arr,n,j,i);
	}
	return wp1/(count);
}
double calcoowp(char arr[100][100],int n,int i)
{
	int count=0;
	double ans=0;
	for(int j=0;j<n;j++)
	{
		if(i==j)
			continue;
		if(arr[i][j]=='.')
			continue;
		count++;
		ans+=owp[j];
	}
	return ans/count;
}
int main()
{
	FILE *fin,*fout;
	fin=fopen("input.txt","r");
	fout=fopen("output.txt","w");
	int t,n;
	double rpi;
	char arr[100][100];
	int pg,pd;
	fscanf(fin,"%d",&t);
	for(int i=0;i<t;i++)
	{
		fprintf(fout,"Case #%d:\n",i+1);
		fscanf(fin,"%d",&n);
		fgetc(fin);
		for(int j=0;j<n;j++)
		{
			for(int k=0;k<n;k++)
			{
				arr[j][k]=fgetc(fin);
			}
			fgetc(fin);
		}
		for(int j=0;j<n;j++)
		{
			wp[j]=calcwp(arr,n,j,-1);
		}
		for(int j=0;j<n;j++)
		{
			owp[j]=calcowp(arr,n,j);			
		}
		for(int j=0;j<n;j++)
		{
			oowp[j]=calcoowp(arr,n,j);
		}
		for(int j=0;j<n;j++)
		{
			rpi=.25*wp[j] + 0.50 * owp[j] + 0.25 * oowp[j];
			fprintf(fout,"%.12lg",rpi);
			if(j!=n-1)
				fprintf(fout,"\n");
		}
		if(i!=t-1)
			fprintf(fout,"\n");
	}
	return 0;
}