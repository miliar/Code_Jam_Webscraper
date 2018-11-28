//#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>

#include <string>
#include <vector>
//#include <map>
#include <hash_map>

//#define LARGE

#ifdef LARGE 
char *sFileIn = "./A-large.in";
char *sFileOut = "./A-large.out";
#else
char *sFileIn = "./A-small-attempt0.in";
char *sFileOut = "./A-small-attempt0.out";
#endif

#define NUMBER_LETTER 26
#define PART_SIZE 4

typedef   std::pair<std::string, int>   str_int;


int **ppLetterCount;
std::string *psWordList;
std::string **ppsWordList;

int sizePart[8];

stdext::hash_map <std::string, int> wordHash;
stdext::hash_map <std::string, int> partwordHash[8];
stdext::hash_map <std::string, int> :: const_iterator hm_word_AcIter, hm_word_RcIter;

typedef struct CASE_INFO
{
	std::string sWordIn;

	bool bHave;		//if false need not calculate
	
	int nCount;		//result
	int numL;
	std::string *pSubWord;
	std::string *pSubWord_Real;	//
}CASE_INFO;

void ExplainCase(CASE_INFO *pCase);
void GetLetterCount(int **pLetterCount, int numLetter, int numD, int numL);

//void CalculateCount(CASE_INFO *pCase, std::string *sWord,  int level);
void CalculatePartCount(CASE_INFO *pCase, std::string *sWord, int iPart, int level, int** ppidxRlt);

int **New2Dim(int numx, int numy);
void Release2Dim(int **pDim, int numx, int numy);



int main(int argc, char *argv[])
{
	int i, j;
	std::ifstream inFile;
	inFile.open(sFileIn);

	std::ofstream outFile;
	outFile.open(sFileOut);

	int numL, numD , numN;

	inFile>>numL;
	inFile>>numD;
	inFile>>numN;

	//´Ê»ã·Ö¶Î word segmentation
	int numPart = numL/PART_SIZE;
	if(numL%PART_SIZE) numPart++;

	psWordList = new std::string[numD];
	
	ppsWordList= new std::string*[numPart];
	for(i=0; i<numPart; i++)
	{
		sizePart[i] = PART_SIZE;
		if(i==numPart-1)
		{
			if(numL%PART_SIZE) sizePart[i] = numL%PART_SIZE;
		}
		ppsWordList[i] = new std::string[numD];

		//printf("part size =%d \n", sizePart[i]);
	}


	//create word table and hash map
	for(i=0; i<numD; i++)
	{
		inFile>>psWordList[i];
		wordHash.insert(str_int(psWordList[i], i));
		//printf("%s \n", psWordList[i].c_str());
	}

	//get part word table
	int begin=0;
	for(i=0; i<numPart; i++)
	{
		begin=0;
		for(j=0; j<numD; j++)
		{
			begin=i*PART_SIZE;
			ppsWordList[i][j] = psWordList[j].substr(begin, sizePart[i]);

			partwordHash[i].insert(str_int(ppsWordList[i][j], j));

			//printf("%s ", ppsWordList[i][j].c_str());
		}
	}


	//create letter table count
	ppLetterCount  = New2Dim(NUMBER_LETTER, numL);
	GetLetterCount(ppLetterCount, NUMBER_LETTER, numD, numL);

	//get case information
	//std::string *psCase = new std::string[numN];
	CASE_INFO *pCase = new CASE_INFO[numN];
	for(i=0; i<numN; i++)
	{
		pCase[i].bHave = true;
		pCase[i].nCount = 0;
		pCase[i].numL = numL;
		pCase[i].pSubWord = new std::string[numL];
		pCase[i].pSubWord_Real = new std::string[numL];

		inFile>>pCase[i].sWordIn;

		ExplainCase(&pCase[i]);

		//printf("%s \n", pCase[i].sWordIn.c_str());
	}

	
	int **ppidxRlt = New2Dim(numD, numPart);

	std::string sWord = "";
	for(i=0; i<numN; i++)
	{
		for(int m=0; m<numPart; m++)
		{
			for(int n=0; n<numD; n++)
			{
				ppidxRlt[m][n]=0;
			}
		}
		if(pCase[i].bHave)
		{
			for(j=0; j<numPart; j++)
			{
				CalculatePartCount(&pCase[i], &sWord, j, 0, ppidxRlt);
			}


			int sum=0;
			for(j=0; j<numD; j++)
			{
				sum=0;
				for(int k=0; k<numPart; k++)
				{
					sum+=ppidxRlt[k][j];
				}

				//printf("sum=%d \n", sum);
				if(sum==numPart)
				{
					pCase[i].nCount++;
				}
				
			}
		}

		printf("Case #%d: %d\n", i+1, pCase[i].nCount);
	}




	char sOut[256];
	for(i=0; i<numN; i++)
	{
		sprintf(sOut, "Case #%d: %d\n", i+1, pCase[i].nCount);
		outFile<<sOut;
	}
	

	inFile.close();
	outFile.close();

	Release2Dim(ppLetterCount, NUMBER_LETTER, numL);
	Release2Dim(ppidxRlt, numD, numPart);
	

	delete [] pCase;

	
	for(i=0; i<numPart; i++)
	{
		delete [] ppsWordList[i];
	}
	delete [] ppsWordList;
	
	getchar();

	return 0;
}

void CalculatePartCount(CASE_INFO *pCase, std::string *sWord, int iPart, int level, int** ppidxRlt)
{
	if(level>sizePart[iPart]-1)
	{
		
		hm_word_AcIter = partwordHash[iPart].find(*sWord);
		if(hm_word_AcIter!=partwordHash[iPart].end())
		{
			//printf("**********%s %d\n", sWord->c_str(), iPart);
			ppidxRlt[iPart][hm_word_AcIter->second] = 1;
		}
		

		return;
	}

	int index = iPart*PART_SIZE +level;
	int len = pCase->pSubWord_Real[index].length();
	std::string sAdd;
	for(int i=0; i<len; i++)
	{
		std::string sWordAdd;

		sAdd = pCase->pSubWord_Real[index].substr(i, 1);
			//*sWord+=sAdd;
		sWordAdd = *sWord+sAdd;

		CalculatePartCount(pCase, &sWordAdd, iPart, level+1, ppidxRlt);
	}
}

/*
 *
*/
void ExplainCase(CASE_INFO *pCase)
{
	const char *sWord = pCase->sWordIn.c_str();
	int i, j;
	int len = pCase->sWordIn.length();
	

	bool bLeft = false;
	int begin;//, lenSub;
	int idxSub = 0;
	for(i=0; i<len; i++)
	{
		if(sWord[i]=='(')
		{
			begin = i+1;
			bLeft = true;
		}

		if(bLeft)
		{
			if(sWord[i]==')')
			{
				bLeft = false;
				pCase->pSubWord[idxSub] = pCase->sWordIn.substr(begin, i-begin);

				idxSub++;

			}
		}
		else
		{
			pCase->pSubWord[idxSub] = pCase->sWordIn.substr(i, 1);
			idxSub++;
		}
	}

	//decrease sub num
	std::string sAdd="";

	int count=0;
	int index;
	for(i=0; i<pCase->numL; i++)
	{
		count=0;
		pCase->pSubWord_Real[i] = "";
		len = pCase->pSubWord[i].length();
		for(j=0; j<len; j++)
		{
			index = pCase->pSubWord[i].c_str()[j]-'a';
			if(ppLetterCount[i][index]!=0)
			{
				std::string sWordAdd;
				sAdd = pCase->pSubWord[i].substr(j, 1);
				//*sWord+=sAdd;
				pCase->pSubWord_Real[i] += sAdd;
				count++;
			}
		}

		//printf("letter=%d  %s\n", i, pCase->pSubWord_Real[i].c_str());

		if(count==0)
		{
			pCase->bHave = false;
			//printf("no case count=%d\n", count);
			break;
		}

	}
	
	
}

void GetLetterCount(int **ppLetterCount, int numLetter, int numD, int numL)
{
	int i, j;

	for(i=0; i<numL; i++)
	{
		for(j=0; j<numLetter; j++)
		{
			ppLetterCount[i][j] = 0;
		}
	}

	int index = 0;
	for(i=0; i<numD; i++)
	{
		for(j=0; j<numL; j++)
		{
			index = psWordList[i].c_str()[j]-'a';
			ppLetterCount[j][index]++;
		}

	}


}

int **New2Dim(int numx, int numy)
{
	int **pDim2 = NULL;
	pDim2 = new int*[numy];
	for(int i=0; i<numy; i++)
	{
		pDim2[i] = new int[numx];
		memset(pDim2[i], 0, numy*4);
	}

	return pDim2;
}

void Release2Dim(int **pDim, int numx, int numy)
{
	for(int i=0; i<numy; i++)
	{
		delete [] pDim[i];
	}

	delete [] pDim;
}


/*
void CalculateCount(CASE_INFO *pCase, std::string *sWord,  int level)
{
	if(level>pCase->numL-1)
	{
		
	hm_word_AcIter = wordHash.find(*sWord);
	if(hm_word_AcIter!=wordHash.end())
	{
		pCase->nCount++;

		//int index = hm_word_AcIter->second;
		//printf("index=%d   %s  %s\n", index, sWord->c_str(), psWordList[index].c_str());
	}

		return;
	}

	int len = pCase->pSubWord[level].length();
	std::string sAdd;
	int index;
	
	
	for(int i=0; i<len; i++)
	{
		
		//index = pCase->pSubWord[level].c_str()[i]-'a';
		//if(ppLetterCount[i][index]!=0)
	
		std::string sWordAdd;

		sAdd = pCase->pSubWord_Real[level].substr(i, 1);
			//*sWord+=sAdd;
		sWordAdd = *sWord+sAdd;

		CalculateCount(pCase, &sWordAdd, level+1);
		
	}

}
*/


