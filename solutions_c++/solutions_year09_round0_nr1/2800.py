#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
void main()
{
	FILE *Filein;
	FILE *Fileout;
	char CurrentChar;
	if ((Filein= fopen("C:\\Sample.in","r"))==NULL)
	{
		printf("Cannot open the input file.\n");
		return;
	}
	if ((Fileout= fopen("C:\\Result.out","w"))==NULL)
	{
		printf("Cannot open the output file.\n");
		return;
	}
	int CaseCount;
	int CharLenth;
	int StringCount;
	int Result[500];
	string GetString[15];
    char CharList[5000][15];
	int CaseResult[5000];
	fscanf(Filein,"%d %d %d\n",&CharLenth,&StringCount,&CaseCount);
	printf("%d %d %d\n",CharLenth,StringCount,CaseCount);
	for (int k=0; k<StringCount; k++)
	{
		fscanf(Filein,"%s\n",CharList[k]);
		printf("%s\n",CharList[k]);
	}
	for (int i=0;i<CaseCount;i++)
	{
		for (int e=0;e<CharLenth;e++)
		{
			GetString[e].clear();
		}
		fscanf(Filein,"%c",&CurrentChar);
		int LenCount = 0;
		while (CurrentChar!='\n')
		{
			if (CurrentChar=='(')
			{
				fscanf(Filein,"%c",&CurrentChar);
				while(CurrentChar!=')')
				{
					GetString[LenCount].push_back(CurrentChar);
					fscanf(Filein,"%c",&CurrentChar);
				}
				//GetString[LenCount].push_back('\0');
				LenCount++;
			}
			else
			{
				GetString[LenCount].push_back(CurrentChar);
				//GetString[LenCount].push_back('\0');
				LenCount++;
			}
			fscanf(Filein,"%c",&CurrentChar);
		}
		for (int n=0;n<StringCount;n++)
		{
			CaseResult[n] = 1;
		}
		for (int c=0;c<StringCount;c++)
		{
			for (int pos=0;pos<CharLenth&&CaseResult[c]==1;pos++)
			{
				putchar(CurrentChar);
				printf("%d %d %s\n",i,pos,GetString[pos]);
				int findpos = GetString[pos].find(CharList[c][pos]);
				if (findpos == -1)
				{
					CaseResult[c] = 0;
				}
			}
		}
		Result[i] = 0;
		for (int b=0;b<StringCount;b++)
		{
			Result[i] = Result[i] + CaseResult[b];
		}
	}
	fclose(Filein);
	
	for (int i=0; i<CaseCount; i++)
	{
		fprintf(Fileout,"Case #%d: %d\n",i+1,Result[i]);
	}
	fclose(Fileout);
}

