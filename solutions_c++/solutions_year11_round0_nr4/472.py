#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <Windows.h>
//#include "random.h"

int current[2000];
int sorted[2000];

/*
void test()
{
	RANDOM rand;
	int len=10;
	int list[1000];
	int places[1000];
	int correct=0;
	int i;
	for(i=0;i<100000;i++)
	{

		int rest=len;

		for(int j=0;j<len;j++)
		{
			places[j] = 0;
		};

		for(int j=0;j<len;j++)
		{
			int v;
			v = rand.ranmar()*(float)rest;
			rest--;
			int l=0;

			while (places[l]) l++;
			for(int o=0;o<v;o++)
			{
				l++;
				while (places[l]) l++;
			};


			list[j] = l;
			places[list[j]] = 1;

		};

		for(int j=0;j<len;j++)
		{
			if (list[j]==j) correct++;
		};
//		printf("%d %d %d\n",list[0],list[1],list[2]);
	};
	printf("%f\n",(float)correct/(float)i);
};
*/


int sorter(const void *a,const void *b)
{
	if (  *(int *)a > *(int *)b) return 1;
	if (  *(int *)a < *(int *)b) return -1;
	return 0;
};

int main(void)
{
// 	test();
// 	return 2;

    FILE *f;
	f=fopen("D-large.in","r");
//	f=fopen("sampd.txt","r");

	int time=0;
	int tc;
	fscanf(f,"%d\n",&tc);
	for(int t=0;t<tc;t++)
	{
		int c;
		fscanf(f,"%d\n",&c);

		for(int i=0;i<c;i++)
		{
			int v;
			fscanf(f,"%d ",&v);
			current[i] = v-1;
			sorted[i] = v-1;
		};

//		qsort(sorted,c,sizeof(int),sorter);
        
		int count=0;

/*		bool changed=true;
		int pass=0;
		while(changed)
		{
			pass++;
			changed = false;


			// scan pairs
			for(int i=0;i<c;i++)
			{
				if (current[i] != i)
				{
					if (  current[current[i]] == i )
					{
						int temp;
						temp = current[i];
						current[i] = current[temp];
						current[temp] = temp;
						count++;
						changed = true;
					};
				}
			};



			if (!changed)
			{
				for(int i=0;i<c;i++)
				{
					if (current[i] != i)
					{
						int temp;
						temp = current[i];
						current[i] = current[temp];
						current[temp] = temp;
						changed = true;
						count++;
					};
				};
			}
		};*/

//		if (pass!=2) Beep(1000,10);

		for(int j=0;j<c;j++)
		{
            if (current[j]!=j) count++;
		};

		printf("Case #%d: %d.000000\n",t+1,count);
	};
	return 1;
};