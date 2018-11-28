#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int N,NA,NB,T,trainCntA,trainCntB;

bool bSolvedA[200];
bool bSolvedB[200];

int startA[200],startB[200];
int endA[200],endB[200];
int trains[200], station[200];

void clean()
{
	int i;
	for (i=0;i<NA+NB;++i)
	{
		trains[i]=-1;
		station[i]=-1;
		bSolvedA[i]=false;
		bSolvedB[i]=false;
	}
}

int findA(int time)
{
	int i;
	for (i=0;i<NA;++i)
	{
		if(startA[i]==time && bSolvedA[i]==false)
		{
			bSolvedA[i] = true;
			return i;
		}
	}
	return -1;
}

int findB(int time)
{
	int i;
	for (i=0;i<NB;++i)
	{
		if(startB[i]==time && bSolvedB[i]==false)
		{
			bSolvedB[i] = true;
			return i;
		}
	}
	return -1;
}



void main()
{
	FILE *f;
	FILE *o;
	int i,j,k;
	f=fopen("B-large.in","rt");
	o=fopen("B-large.out","wt");
	fscanf(f,"%d\n",&N);
	for (i=0;i<N;++i)
	{
		clean();
		trainCntA=trainCntB=0;
		fscanf(f,"%d\n",&T);
		fscanf(f,"%d %d\n",&NA, &NB);
		for (j=0;j<NA;++j)
		{
			int hh,mm;
			fscanf(f,"%d:%d\n",&hh, &mm);
			startA[j] = hh*60+mm;
			fscanf(f,"%d:%d\n",&hh, &mm);
			endA[j] = hh*60+mm+T;
		}
		for (j=0;j<NB;++j)
		{
			int hh,mm;
			fscanf(f,"%d:%d\n",&hh, &mm);
			startB[j] = hh*60+mm;
			fscanf(f,"%d:%d\n",&hh, &mm);
			endB[j] = hh*60+mm+T;
		}
		for (j=0;j<24*60;++j)
		{
			int a = findA(j);
			if (a>=0)
				printf("a:%d ",a);
			while(a>=0)
			{
				bool bAssigned = false;
				for (k=0;k<trainCntA+trainCntB;++k)
				{
					if (station[k]=='A' && trains[k]<=j)
					{
						station[k]='B';
						trains[k] = endA[a];
						bAssigned = true;
						break;
					}
				}
				if (bAssigned == false)
				{
					trains[k] = endA[a];
					station[k]='B';
					++trainCntA;
				}
				printf("%d\n",k);
				a = findA(j);
			}
			int b = findB(j);
			if (b>=0)
				printf("b:%d ",b);
			while(b>=0)
			{
				bool bAssigned = false;
				for (k=0;k<trainCntA+trainCntB;++k)
				{
					if (station[k]=='B' && trains[k]<=j)
					{
						station[k]='A';
						trains[k] = endB[b];
						bAssigned = true;
						break;
					}
				}
 				if (bAssigned == false)
				{
					trains[k] = endB[b];
					station[k]='A';
					++trainCntB;
				}
				printf("%d\n",k);
				b = findB(j);
			}
		}
//		fprintf(o,"Case #%d: %d\n",i+1,change);
		fprintf(o,"Case #%d: %d %d\n",i+1, trainCntA, trainCntB);
	}
	fclose(f);
	fclose(o);
}