#include <stdio.h>
#include <malloc.h>
#include <math.h>
#include <string.h>

typedef struct tagNODE
{
	struct tagNODE *pLeft;
	struct tagNODE *pRight;
	struct tagNODE *pPar;
	double dW;
	int nLen;
	char pStr[11];
} NODE, *LPNODE;

typedef struct tagCHARLEN
{
	int nLen;
	char pStr[11];
} CHARLEN, *LPCHARLEN;


int Check(char* pFea, int feaLen, CHARLEN* pList, int nListLen)
{
	int i, j;
	for(i=0; i<nListLen; i++)
	{
		if(feaLen==pList[i].nLen)
		{
			for(j=0; j<feaLen; j++)
			{
				if(pFea[j] != pList[i].pStr[j])
					break;
			}
			if(j==feaLen)
			{
				return 1;
			}
		}
	}
	if(i==nListLen)
	{
		return 0;
	}
	return 1;
}
int main()
{
	int nRound;
	FILE* fp;
	int i, j, k;
	char pName[256];
	fp = fopen("1.txt", "r");

	fscanf(fp, "%d", &nRound);

	fgetc(fp);
	
	for(i=0; i<nRound; i++)
	{
		LPNODE pHead = (LPNODE)malloc(sizeof(NODE));
		pHead->pPar = NULL;
		pHead->pLeft=pHead->pRight=NULL;
		LPNODE pPar = pHead;
		int nTotalLine;
		fscanf(fp, "%d", &nTotalLine);
		fgetc(fp);
		int nStep = 0;
		char pW[20];
		char pStr[11];
		int nCountStr = 0;
		int nCountW = 0;
		int nLine = 0;
		while(1)
		{
			int ch = fgetc(fp);
			if(ch==' ' && nStep==0)
			{
				continue;
			}
			if(ch=='(' && nStep==0)
			{
				nStep = 1;
				continue;
			}
			if(ch==' ' && nStep==1)
			{
				continue;
			}
			if(ch!=' '&& ch != ')'&& (nStep==1||nStep==2))
			{
				nStep = 2;
				pW[nCountW++] = ch;
				continue;
			}
			if(ch==' ' && nStep==2)
			{
				nStep = 3;
				continue;
			}
			if(ch != '\n' && ch != -1 && ch != ')' && nStep==3)
			{
				pStr[nCountStr++] = ch;
				continue;
			}
			if(ch == ')' && nStep==2)
			{
				LPNODE pNode = (LPNODE)malloc(sizeof(NODE));
				pNode->pLeft=pNode->pRight=NULL;
				if(pPar->pLeft==NULL)
				{
					pPar->pLeft = pNode;
				}
				else
				{
					pPar->pRight = pNode;
				}
				pNode->pPar = pPar;
				pNode->nLen = 0;
				pW[nCountW] = '\0';
				pNode->dW = atof(pW);
				nStep = 4;
				continue;
			}
			if(ch==')' && nStep==4)
			{
				pPar = pPar->pPar;
				continue;
			}
			if(ch==' '&& nStep==3)
			{
				continue;
			}
			if((ch=='\n' || ch == -1)&& nStep==3)
			{
				LPNODE pNode = (LPNODE)malloc(sizeof(NODE));
				pNode->pLeft=pNode->pRight=NULL;
				if(pPar->pLeft==NULL)
				{
					pPar->pLeft = pNode;
				}
				else
				{
					pPar->pRight = pNode;
				}
				pNode->pPar = pPar;
				pStr[nCountStr] = '\0';
				pNode->nLen = strlen(pStr);
				pW[nCountW] = '\0';
				pNode->dW = atof(pW);
				strcpy(pNode->pStr, pStr);
				nLine++;
				if(nLine==nTotalLine)
				{
					break;
				}
				else
				{
					nStep = 0;
					nCountW = 0;
					nCountStr = 0;
					pPar = pNode;

				}
				continue;
			}
			if((ch=='\n'  || ch == -1)&& nStep==4)
			{
				nStep = 0;
				nCountW = 0;
				nCountStr = 0;
				nLine++;
				if(nLine==nTotalLine)
				{
					break;
				}
				continue;
			}
			if(ch==')' && nStep == 0)
			{
				pPar = pPar->pPar;
				nStep = 4;
				continue;
			}
		}
		int nCase;
		int nFeature;
		printf("Case #%d:\n", i+1);
		fscanf(fp, "%d", &nCase);
		for(j=0; j<nCase; j++)
		{
			fscanf(fp, "%s %d", pName, &nFeature);
			CHARLEN *pCharList = (CHARLEN*)malloc(nFeature*sizeof(CHARLEN));
			for(k=0; k<nFeature; k++)
			{
				fscanf(fp, "%s", pCharList[k].pStr);
				pCharList[k].nLen = strlen(pCharList[k].pStr);
			}
			LPNODE pCur = pHead->pLeft;
			double dCal = 1.0f;
			while(1)
			{
				dCal *= pCur->dW;
				if(pCur->nLen == 0) break;
				if(Check(pCur->pStr, pCur->nLen, pCharList, nFeature) == 1)
				{
					pCur = pCur->pLeft;
				}
				else
				{
					pCur = pCur->pRight;
				}
			}
			printf("%.7lf\n", dCal);
			free(pCharList);
		}

	}
	return 0;
}