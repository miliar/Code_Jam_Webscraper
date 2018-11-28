
#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;
string str;
typedef	struct SearchEngineList
{
	int		m_Num;
	int		*m_Mark;
	char	**m_Name;
}SearchEngineList;

typedef	struct QueryList 
{
	int		m_Num;
	char	**m_Name;
}QueryList;

//////////////////////////////////////////////////////////////////////////
//declaration function
int	switchTimes(SearchEngineList &SEList, QueryList &QList);
bool findEng(int * p,int n);
int findUseEng(int *p,int n);
bool trav(int *p , int n);
bool searchQue(char * str,SearchEngineList & arrayEng);

int main(int argc, char **argv)
{
	int		InstantNum;
	int		SwitchNum = 0;
	SearchEngineList	SEList;
	QueryList			QList;
	FILE*	input = NULL;
	FILE*	output = NULL;

	char	cTemp[20];

	int		i, j;
	if (argc != 3)
	{
		printf("Useage: program inputfile outputfile\n");
		return 0;
	}

	if (!(input = fopen(argv[1], "rt")))
	{
		printf("Open file %s failed!\n", argv[1]);
		return -1;
	}
	if (!(output = fopen(argv[2], "wt")))
	{
		printf("Open file %s failed!", argv[2]);
		return -1;
	}

	fscanf(input, "%d", &InstantNum);

	for(i = 1; i <= InstantNum; i++)
	{
		fscanf(input, "%d", &SEList.m_Num);
		fgets(cTemp, 15, input);
		//fseek(input, 1, SEEK_CUR);
		SEList.m_Mark = (int *)malloc(SEList.m_Num*sizeof(int));
		SEList.m_Name = (char **)malloc(SEList.m_Num*sizeof(char *));
		for (j = 0; j < SEList.m_Num; j++)
		{
			SEList.m_Name[j] = (char *)malloc(200*sizeof(char));
			//fscanf(input, "%s", SEList.m_Name[j]);
			fgets(SEList.m_Name[j], 150, input);   
			SEList.m_Mark[j] = 0;
		}

		fscanf(input, "%d", &QList.m_Num);
		//fseek(input, 2, SEEK_CUR);
		fgets(cTemp, 15, input);
		QList.m_Name = (char **)malloc(QList.m_Num*sizeof(char *));
		for (j = 0; j < QList.m_Num; j++)
		{
			QList.m_Name[j] = (char *)malloc(200*sizeof(char));
			//fscanf(input, "%s", QList.m_Name[j]);
			fgets(QList.m_Name[j], 150, input);
		}

		SwitchNum = switchTimes(SEList, QList);
		//printf("Case #%d: %d\n", i, SwitchNum);
		fprintf(output, "Case #%d: %d\n", i, SwitchNum);

		for (j = 0; j < QList.m_Num; j++)
		{
			free(QList.m_Name[j]);
		}
		free(QList.m_Name);

		for (j = 0; j < SEList.m_Num; j++)
		{
			free(SEList.m_Name[j]);
		}
		free(SEList.m_Name);
		free(SEList.m_Mark);
	}

	return 0;
}

int	switchTimes(SearchEngineList &SEList, QueryList &QList)
{
	int Qswitch = 0;
	int engNum = SEList.m_Num;
	int qurNum = QList.m_Num;
	char * tempQur;
	for (int i = 0;i < qurNum; i++)
	{
		tempQur = SEList.m_Name[i];
		if (findEng(SEList.m_Mark,SEList.m_Num))//only one useful engine 
		{
			int loc = findUseEng(SEList.m_Mark,SEList.m_Num);
			if (!strcmp(QList.m_Name[i],SEList.m_Name[loc])) //a = b
			{
				trav(SEList.m_Mark,SEList.m_Num);
				Qswitch++;
			}
		}else{
			searchQue(QList.m_Name[i],SEList);
		}//end else
		
	}//end for
	return	Qswitch;
}
//////////////////////////////////////////////////////////////////////////
//p = 0表示可用，1 不可用
//引擎个数为 n
//返回值为 是否只剩下一个可用引擎
//////////////////////////////////////////////////////////////////////////
bool findEng(int * p,int n)
{
	int temp1 = 0;
	for(int i = 0; i < n ; i++){
		if(0 == p[i]) temp1++;
	}
	if (temp1 == 1)
		return true;
	else
		return false;
}
//////////////////////////////////////////////////////////////////////////
//find the location of useful engine
//
//////////////////////////////////////////////////////////////////////////
int findUseEng(int *p,int n)
{
	for(int i = 0; i < n ; i++)
		if(0 == p[i]) return i;
	
}
//////////////////////////////////////////////////////////////////////////
//
//let array of p become negative p
//////////////////////////////////////////////////////////////////////////
bool trav(int *p , int n)
{
	for(int i = 0; i < n ; i++)
		if(0 == p[i]) 
			p[i] = 1;
		else
			p[i] = 0;
	return true;
}
//////////////////////////////////////////////////////////////////////////
//
//find the engine == query
//////////////////////////////////////////////////////////////////////////
bool searchQue(char * str,SearchEngineList & arrayEng)
{
	for (int i = 0; i < arrayEng.m_Num; i++)
	{
		if (0 == arrayEng.m_Mark[i] && !strcmp(str,arrayEng.m_Name[i]))
		{
			arrayEng.m_Mark[i] = 1;
			return true;
		}
	}
	return false;
}