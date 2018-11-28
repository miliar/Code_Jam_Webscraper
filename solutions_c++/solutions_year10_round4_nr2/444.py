#include <ios>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

const int INF=600000000;

int M[5005],price;
int dp[5005][30],save[5005][30];
int main()
{
	FILE *fin, *fout;
	fin = fopen("\B-large.in","r");
	fout = fopen("\B-large.out","w");

	int t,p,i,j,k,N,x;
	fscanf(fin,"%d",&t);
	int cnt=0;
	while(t--)
	{
		fscanf(fin,"%d",&p);
		N=(1<<p);
		for(i=1;i<=N;i++)
		{
			fscanf(fin,"%d",&M[i]);
			M[i]=p-M[i];
			for(k=0;k<M[i];k++)
				dp[i][k]=INF;
			for(k=M[i];k<=p+1;k++)
				dp[i][k]=0;
		}
		for(i=p-1;i>=0;i--)
		{
			x=(1<<i);
			for(j=1;j<=x;j++)
			{
				fscanf(fin,"%d",&price);
				for(k=0;k<=p;k++)
				{
					save[j][k]=min(dp[2*j-1][k]+dp[2*j][k],dp[2*j-1][k+1]+dp[2*j][k+1]+price);
					if(save[j][k]>INF)save[j][k]=INF;
				}
			}
			for(j=1;j<=x;j++)
				for(k=0;k<=p;k++)
					dp[j][k]=save[j][k];
		}
		fprintf(fout,"Case #%d: %d\n",++cnt,dp[1][0]);
	}
}
