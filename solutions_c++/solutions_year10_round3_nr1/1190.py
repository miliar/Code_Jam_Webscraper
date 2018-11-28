// googlecodejam1c.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include "stdio.h"
#include "string.h"


int arr[2000][2];



int main()
{
	int TestCase;
	FILE *fp2;
	FILE *fp1;
	fp2 = fopen("c:/codejaminput1.in","r");
	fp1 = fopen("c:/gocodejam1","w");
	fscanf(fp2,"%d",&TestCase);
	int i,K,j,m,l;
	int N, M;
	int count = 0;
	char str[1000];
	for( i = 1; i <= TestCase ; i++ )
	{
		count = 0;
		fscanf(fp2,"%d",&N);
		for(l=0;l<N;l++)
		{
			fscanf(fp2,"%d %d",&arr[l][0],&arr[l][1]);
		}
		for( l = 0;l<N-1;l++)
		{
			for( m=l+1; m<N; m++ )
			{
				if((arr[l][0] - arr[m][0])*(arr[l][1] - arr[m][1]) < 0 )
				{
					count++ ;
				}
			}
		}
		fprintf( fp1 , "Case #%d: %d\n",i,count);
	}
	fclose(fp1);
	fclose(fp2);
	scanf("%d",&i);
}

