// codeJam.cpp : Defines the entry point for the console application.
//

#include "StdAfx.h"

#define TOP 1000000000
#define MAXPEOPLESIZE 1024

int main(int argc, char* argv[])
{	
	FILE *fpIn,*fpOut;
	long people[MAXPEOPLESIZE];
	long money[MAXPEOPLESIZE];
	int next[MAXPEOPLESIZE];
	long sum = 0,sa=0,sb=0;
	int j=0,m=0,p=0,caseNo=0,i=0;
	long r=0,k=0,n=0;
	
	fpIn = fopen("C-large.in","r");
	fpOut = fopen("C-large.out","w");

	fscanf(fpIn,"%d",&caseNo);		
	for (i=1; i<=caseNo; i++)
	{
		fscanf(fpIn,"%d%d%d",&r,&k,&n);
		for (j=0;j<n;j++)
			fscanf(fpIn,"%d",&people[j]);
		
		for (j=0; j<n; j++)
		{
			sum = 0;
			m = j;
			do
			{
				sum += people[m];
				m = (m+1)%n;
			}while(sum<=k&&m!=j);		

			if (sum>k)
			{
				m = (m-1+n)%n;
				sum -= people[m];				
			}
			next[j] = m;
			money[j] = sum;
		}

		sa = 0;
		sb = 0;

		p = 0;
		for(j=0; j<r; j++)
		{
			sb += money[p];
			p = next[p];
			sa += sb/TOP;
			sb = sb%TOP;
		}

		if (sa)
			fprintf(fpOut,"Case #%d: %d%09d\n",i,sa,sb);
		else
			fprintf(fpOut,"Case #%d: %d\n",i,sb);
	}

	fclose(fpOut);
	fclose(fpIn);

	return 0;
}

