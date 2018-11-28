#include<iostream.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void main()
{

	int numSearchEngines, numSearchQueries; //a,b
	char **SearchEngineName, **SearchQuerieName; //c,d
	int i,j,k,l;
	bool NOT_SET=false;
	int switches = 0;
	bool *flag;
	FILE *fin, *fout;
	char name[100];
	int num_cases = 0 ,cases;

	printf("\n Enter the input file name: ");
	scanf("%s",name);
	
	fin = fopen(name,"r");
	
	if(fin)
	{
		fout = fopen("out.txt","w");

		fscanf(fin,"%d",&num_cases);
	
		for(cases=0; cases<num_cases; cases++)
		{
			switches = 0;
			
			fscanf(fin,"%d",&numSearchEngines);
			
			SearchEngineName = (char**) malloc(sizeof(char*) * numSearchEngines);
			
			fgetc(fin);/*** For reading the \n character ****/

			for(i =0;i<numSearchEngines;i++)
			{
				SearchEngineName[i] = (char*)malloc(sizeof(char)*101);
				fgets(SearchEngineName[i],100,fin);
			}

			fscanf(fin,"%d",&numSearchQueries);

			fgetc(fin); /*** For reading the \n character ****/

			SearchQuerieName = (char**) malloc(sizeof(char*) * numSearchQueries);
		
			for(i =0;i<numSearchQueries;i++)
			{
				SearchQuerieName[i] = (char*)malloc(sizeof(char)*101);
				fgets(SearchQuerieName[i],100,fin);
			}
	
			flag = (bool*)malloc(sizeof(bool)* numSearchEngines);
	
			for(i=0;i<numSearchEngines;i++)
				flag[i]=false;

			j = 0;

			while(j<numSearchQueries)
			{
				for(k=0;k<numSearchEngines && strcmp(SearchEngineName[k],SearchQuerieName[j]);k++);
			
				if(k!=numSearchEngines)
				{
					flag[k]=true;
				}
				
				NOT_SET=false;
				
				for(l=0;l<numSearchEngines;l++)
					if(flag[l]!=true)
						NOT_SET=true;
				
				if(NOT_SET==false)
				{
					switches++;
					
					for(l=0;l<numSearchEngines;l++)
						flag[l]=false;
					
					flag[k]=true;
				}
				j++;
			}
			
			
			if(fout)
			{
				fprintf(fout,"\nCase #%d: %d ",cases + 1,switches);
			}
			else
				printf("\nCase #%d: %d ",cases + 1,switches);

			free(flag);
			
			for(i=0;i<numSearchEngines;i++)
			{
				free(SearchEngineName[i]);
			}
			free(SearchEngineName);

			for(i=0;i<numSearchQueries;i++)
			{
				free(SearchQuerieName[i]);
			}
			free(SearchQuerieName);
		}
		fclose(fin);
		if(fout)
			fclose(fout);
	}
	else
		printf("\n Error Opening file");
}
