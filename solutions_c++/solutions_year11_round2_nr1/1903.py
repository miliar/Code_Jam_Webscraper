// poj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int main()
{
	int t,n;
	char a[100][101];
	double wp[100],owp[100],oowp[100];
	int i,j,k,l;
	int win,total;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%s",a[j]);
		}
		printf("Case #%d:\n",i+1);
		for(j=0;j<n;j++)
		{
			win=total=0;
			for(k=0;k<n;k++)
			{
				if(a[j][k]!='.')
					total++;
				if(a[j][k]=='1')
					win++;
			}
			wp[j]=1.0*win/total;
			owp[j]=oowp[j]=0;
		}
		for(j=0;j<n;j++)
		{
			double temp=0;
			for(k=0;k<n;k++)
			{
				if(a[j][k]!='.')
				{
					owp[j]+=1;
					win=total=0;
					for(l=0;l<n;l++)
					{
						if(l!=j)
						{
							if(a[k][l]!='.')
								total++;
							if(a[k][l]=='1')
								win++;
						}
					}
					temp+=1.0*win/total;
					
				}
				
			}
			owp[j]=temp/owp[j];
		}
		for(j=0;j<n;j++)
		{
			double temp=0;
			for(k=0;k<n;k++)
			{
				if(a[j][k]!='.')
				{
					oowp[j]+=1;
					temp+=owp[k];
				}
			}
			oowp[j]=temp/oowp[j];
		}
		for(j=0;j<n;j++)
		{
			printf("%.8lf\n",0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]);
		}

	}
}

