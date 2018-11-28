#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>
#include <iostream>
#include <fstream>
using namespace std;

#define bool int
#define true 1
#define false 0
#define ACCURACY 1

main(int argc,char*argv[])
{

	int testcases,numengines,queuesize,i,j;
	FILE *fpOut;
	fpOut = fopen("test.out","w");
	if( fpOut == NULL)
	{
		perror("ouput file open failed");
		return -1;
	}
	ifstream fpIn;
	fpIn.open(argv[1]);
	char **engines,**queue,stream[100];
	int *usedengine;
	fpIn.getline(stream,100);
	testcases = atoi(stream);
	for( i =0;i<testcases;i++)
	{
	fpIn.getline(stream,100);
	numengines = atoi(stream);
		//printf("engines =%d\n",numengines);

		engines = (char**)malloc(numengines * sizeof(char**));
		usedengine = (int*)malloc(numengines * sizeof(int));
		for( j =0;j<numengines;j++)
		{
			fpIn.getline(stream,100);
			engines[j] = (char*)malloc( (strlen(stream)+1) * sizeof(char));
			strcpy(engines[j],stream);
			usedengine[j] = 0;
		//	printf("engg: %s\n",engines[j]);

		}
		fpIn.getline(stream,100);
		queuesize = atoi(stream);
		//printf("ques =%d\n",queuesize);
		queue= (char**)malloc(queuesize * sizeof(char**));
		for( j =0;j<queuesize;j++)
		{
			fpIn.getline(stream,100);
			queue[j] = (char*)malloc( (strlen(stream)+1) * sizeof(char));
			strcpy(queue[j],stream);
			//printf("queue:%s\n",queue[j]);

		}
		int sw=0,k,found,lastused;
		for ( j =0 ;j<queuesize;j++)
		{
			for(k=0;k<numengines;k++)
			{
				if(!usedengine[k] && strstr(engines[k],queue[j]))
				{
					usedengine[k]=1;
					lastused=k;
					break;
				}
			}
			found=0;
			for(k=0;k<numengines;k++)
			{
				if (!usedengine[k])
				{
					found=1;
					break;
				}
			}
			if( !found)
			{
				sw++;
				for(k=0;k<numengines;k++)
					if( k !=lastused)
					usedengine[k]=0;
			}
		}
		fprintf(fpOut,"Case #%d: %d\n",i+1,sw);
		for( j = 0;j<numengines;j++)
			if(engines[j])
			free(engines[j]);
		for(j=0;j<queuesize;j++)
			if(queue[j])
			free(queue[j]);
		if( engines)
			free(engines);
		engines=NULL;
		if(queue)
			free(queue);
		queue=NULL;
	}
	return 0;
}
