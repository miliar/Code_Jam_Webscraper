#include "stdafx.h"
#include <iostream>
using namespace std;
int RollerCoaster(int r,int k,int n,int *arrray){

	int round = 1,subSum = 0,temp = 0,sum = 0;
	while (round <= r)
	{		
		int i = 0;
		for(;i < n && subSum + *(arrray + i) <= k;i++)
		{
			subSum += *(arrray + i);
		}

		sum += subSum;

		for (int j = 0;j < i;j++)
		{
			temp = *arrray;
			int h = 1;
			for (;h < n;h++)
			{
				*(arrray + h-1) = *(arrray + h);
			}
			*(arrray + h - 1) = temp;
		}

		//cout<<": sum = "<<sum<<endl;
		//for (int i = 0;i < n; i++)
		//{
		//	cout<<*(arrray + i)<<" ";
		//}
		//cout<<endl;

		round++;
		subSum = 0;		
	}
	return sum;
}
void ThemePark(){
	FILE *fin,*fout;
	char inputFile[] = "C-small-attempt1.in";
	char outFile[] = "CpengjinningSubmition1.out";

	int T = 0,R = 0,k = 0,N = 1,count = 1;

	if ((fin = fopen(inputFile,"r"))==NULL)
	{
		printf("can not open file %s\n",inputFile);
		//exit(-1);
	}
	if ((fout = fopen(outFile,"w"))==NULL)
	{
		printf("can not open file %s\n",outFile);
		//exit(-1);
	}

	fscanf(fin,"%d",&T);

	while (count <= T)
	{
		fscanf(fin,"%d%d%d",&R,&k,&N);

		int *pArray = new int[N];
		for (int i = 0;i < N;i++)
		{
			fscanf(fin,"%d",pArray+i); 
		}
		
		fprintf(fout,"Case #%d: %d",count++,RollerCoaster(R,k,N,pArray));
		if (count <= T)
		{
			fprintf(fout,"\n","");
		}

	}
	fclose(fin);
	fclose(fout);

}