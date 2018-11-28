#include <stdio.h>
#include <string.h>
#include <malloc.h>

#define MAX_LENGTH	(512)

int Add(int x, int y)
{
	int nRet = x + y;
	int nVal1 = nRet&0xFF;
	int nVal2 = (nRet>>8)&0xFF;
	int nVal3 = (nRet>>16)&0xFF;
	int nVal4 = (nRet>>24)&0xFF;
	if(nVal1>=10)
	{
		nVal2 += nVal1/10;
		nVal1%=10;
	}
	if(nVal2>=10)
	{
		nVal3 += nVal2/10;
		nVal2%=10;
	}
	if(nVal3>=10)
	{
		nVal4 += nVal3/10;
		nVal3%=10;
	}
	if(nVal4>=10)
	{
		nVal4%=10;
	}
	return nVal1+(nVal2<<8)+(nVal3<<16)+(nVal4<<24);
}

int main()
{
	char pStr[MAX_LENGTH];
	char *pMatch = "welcome to code jam";

	FILE* fp;
	int nRound;
	int i, j, k;
	fp = fopen("1.txt", "r");
	fscanf(fp, "%d", &nRound);
	int nLenMatch = strlen(pMatch);
	int nLenStr;

	int* pCal = (int*)malloc(MAX_LENGTH*nLenMatch*sizeof(int));
	int* pCalTmp;
	fgetc(fp);
	for(i=0; i<nRound; i++)
	{

		for(j=0; j<MAX_LENGTH; j++)
		{
			int ch = fgetc(fp);
			if(ch == '\n') break;
			pStr[j] = ch;
		}
		nLenStr = j;
		pCalTmp = pCal+nLenMatch*nLenStr-1;
		
		if(pStr[nLenStr-1]==pMatch[nLenMatch-1])
			*pCalTmp--=1;
		else
			*pCalTmp--=0;
		for(k=nLenStr-2; k>=0; k--, pCalTmp--)
		{
			if(pStr[k]==pMatch[nLenMatch-1])
			{
				*pCalTmp = Add(*(pCalTmp+1), 1);
			}
			else
			{
				*pCalTmp = *(pCalTmp+1);
			}
		}
		for(j=nLenMatch-2; j>=0; j--)
		{
			*pCalTmp--=0;
			for(k=nLenStr-2; k>=0; k--, pCalTmp--)
			{
				if(pStr[k]==pMatch[j])
				{
					*pCalTmp = Add(*(pCalTmp+1), *(pCalTmp+nLenStr));
				}
				else
				{
					*pCalTmp = *(pCalTmp+1);
				}
			}
		}
		int nRet = *pCal;
		printf("Case #%d: %d%d%d%d\n", i+1, (nRet>>24), (nRet>>16)&0xFF, (nRet>>8)&0xFF, nRet&0xFF);
	}
	return 0;
}