#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int OverLap(vector <string> Engine,vector <string> queries)
{
	int i,j;
	int Num = Engine.size();

	int * nSign = new int [Num];
	
	for (i=0; i<Engine.size(); i++)
	{
		nSign[i] = 0;
	}

	for (j=0; j<queries.size(); j++)
	{
		for (i=0; i<Engine.size(); i++)
		{
			if (queries[j]==Engine[i])
			{
				nSign[i] = 1;
			}
		}
	}
	
	for (i=0; i<Engine.size(); i++)
	{
		if (nSign[i]!=1)
		{
			return -1;
		}
	}

	delete [] nSign;

	return 1;
}

int MinSwitch(vector <string> Engine,vector <string> queries)
{
	int nMinSwitch;
	int nTempSwitch = 0;
	int i,j;
	vector <string> StrComp;
	
	int nSign = 0;
	
	
	for (j=0; j<queries.size(); j++)
	{
		StrComp.push_back(queries[j]);
		if (OverLap(Engine,StrComp)==1)
		{
			printf("Switch Points:%d\n",j);
			nSign++;
			StrComp.clear();
			StrComp.push_back(queries[j]);
		}
		else
		{

		}
	}

	return nSign;
}


int main(int argc,char* argv[])
{
	FILE* fpTest = fopen("A-small-attempt6.in","rt");
	int nTestCase;
	FILE* fpResult = fopen("small.result","wt");

	int nEngine;
	int nQueries;

	int i,j;
	fscanf(fpTest,"%d",&nTestCase);
	
    char Word[600];
	for (i=0; i<nTestCase; i++)
	{
		printf("TestCase : %d:",i);
		vector <string> Engine;
		vector <string> queries;

		fscanf(fpTest,"%d\n",&nEngine);
		for (j=0; j<nEngine; j++)
		{
			string Temp;
//			fscanf(fpTest,"%s\n",Word);
			fgets(Word,600,fpTest);
			int nLen = strlen(Word);
			Word[nLen-1] = '\0';
//			strcpy(Temp.c_str(),Word);
			Temp = Word;
			Engine.push_back(Temp);
		}


		fscanf(fpTest,"%d\n",&nQueries);
		for (j=0; j<nQueries; j++)
		{
			string Temp;
//			fscanf(fpTest,"%s\n",Word);
			fgets(Word,600,fpTest);
			int nLen = strlen(Word);
			Word[nLen-1] = '\0';
			Temp = Word;
			queries.push_back(Temp);
		}

//		printf("Case #%d: %d\n",i+1,MinSwitch(Engine,queries));
		printf("\n");
		fprintf(fpResult,"Case #%d: %d\n",i+1,MinSwitch(Engine,queries));
	}
	fclose(fpResult);
	fclose(fpTest);
	return 1;
}