// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <string>
#include "shlwapi.h"
//shlwapi.lib
using namespace std;
/*__int64
{
	for(int j =0;j < engineNumber;j++)
	{
		__int64 count(0);
		
		for(int index =0;index < size; index++)
		{
			if(engineName[j] == vector->at(index))
			{
				if(i > maxCount )
				{
					maxCount = i;
					maxIndex = j
				}
				break;
			}
			count++;			
		}
	}
}*/
__int64 numberSwitches(const char** engineName,__int64 engineNumber,vector<const char*>  *vector)
{
	__int64 switches(0);
	__int64 size = vector->size();
	__int64 maxCount(0);
	__int64 maxIndex(0);
	__int64 index(0),newIndex(0);
	while(index < size)
	{
		newIndex += maxCount;
		maxCount = 0;
		switches++;
		for(int j =0;j < engineNumber;j++)
		{
			__int64 count(0);			
			for(index = newIndex;index < size; index++)
			{
				if(engineName[j] == vector->at(index))
				{
					if(count > maxCount )
					{
						maxCount = count;
						maxIndex = j;
					}
					break;
				}
				count++;				
			}
			if(index >= size)
				return (switches - 1);
		}
	}
	if(size == 0)
		return 0;
	return (switches - 1);
}


int main(int argc, const char* argv[])
{
	string output,inPath(argv[1]),outPath(argv[2]);
	FILE* fpIn,*fpOut;
	fpIn  = fopen(inPath.c_str(),"rb");
	fpOut = fopen(outPath.c_str(),"wb");
    fseek( fpIn , 0L, SEEK_SET );
	fseek( fpOut, 0L, SEEK_SET );	
	__int64 engineNumber(0),caseNumber(0),queryNumber(0);
	fscanf(fpIn,"%I64d",&caseNumber);	
	vector<const char*> queryVector;
	const char* queryName = new char[1000];
	
	for(int index=1;index<=caseNumber;index++)
	{
		fscanf(fpIn,"%I64d",&engineNumber);	
		char start[3];
		fgets(start,3,fpIn);
		const char** engineName = new const char*[engineNumber];
		for(int i=0;i < engineNumber;i++)
		{
			engineName[i]= new char[1000];			
			if(fgets((char*)engineName[i],10000,fpIn) == NULL)
			{	
				printf("Erro EngineName\n");
				break;
			}				
		}		
		fscanf(fpIn,"%I64d",&queryNumber);	
		fgets(start,3,fpIn);
		for(int i=0;i < queryNumber;i++)
		{
			if(fgets((char*)queryName,1000,fpIn) == NULL)
			{	
				printf("Erro QueryName\n");
				break;
			}				
			for(int i=0;i < engineNumber;i++)
			{
				if(strcmp(queryName,engineName[i]) == 0)
				{
					queryVector.push_back(engineName[i]);
					break;
				}
			}
		}
		//Process
		__int64 swicthes = numberSwitches(engineName,engineNumber,&queryVector);

		//OutPut
		fprintf(fpOut,"Case #%d: %I64d\n",index,swicthes);

		//Clean
		queryVector.clear();
		for(int i=0;i < engineNumber;i++)
			delete []engineName[i];
	}			
	fclose(fpIn);
	fclose(fpOut);
	return 0;
}

