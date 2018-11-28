/*
 * prob1.cc
 *
 *  Created on: Jul 26, 2008
 *      Author: balakrishnanvaradarajan
 */

#include <stdio.h>
#include <math.h>

#include <vector>
using namespace std;
long long int n,A,B,C,D,x0,Y0,X,Y,M,numtrees,numtestcases;
long long int xmodval,ymodval;
long long int Xmods[100002];
long long int Ymods[100002];
long long int cumulativemodvals[100002][11];
long long int wantedx,wantedy;
int main(int argc,char *argv[])
{
	FILE *fp;
	fp=fopen(argv[1],"r");

	fscanf(fp,"%lld",&numtestcases);
	for(long long int i=1;i<=numtestcases;i++)
	{

		fscanf(fp,"%lld",&n);
		fscanf(fp,"%lld",&A);
		fscanf(fp,"%lld",&B);
		fscanf(fp,"%lld",&C);
		fscanf(fp,"%lld",&D);
		fscanf(fp,"%lld",&x0);
		fscanf(fp,"%lld",&Y0);
		fscanf(fp,"%lld",&M);
		X=x0;
		Y=Y0;

		for(long long int j=1;j<=n+2;j++)
				{
					for(long long int k=1;k<=10;k++)
						cumulativemodvals[j][k]=0;
				}
		xmodval=X%3;
		ymodval=Y%3;


		Xmods[1]=xmodval;
		Ymods[1]=ymodval;

		for(int j=2;j<=n;j++)
		{
			X=(A*X+B)%M;
			Y=(C*Y+D)%M;

			xmodval=X%3;
			ymodval=Y%3;

			Xmods[j]=xmodval;
			Ymods[j]=ymodval;

			for(long long int k=1;k<j;k++)
				cumulativemodvals[k][xmodval*3+ymodval]++;

		}
		long long int count=0;

		for(long long int j=1;j<=n;j++)
					for(long long int k=j+1;k<=n;k++)
						for(long long int l=k+1;l<=n;l++)
							if((Xmods[j]+Xmods[k]+Xmods[l])%3==0 && (Ymods[j]+Ymods[k]+Ymods[l])%3==0)
								count++;


		printf("Case #%lld: %lld\n",i,count);

	}


}

