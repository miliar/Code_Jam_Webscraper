#include <stdio.h>
#include <malloc.h>
#include <memory.h>

int SetVal(char* pVal, int* pPar, int nPos)
{
	if(pVal[nPos]==0)
	{
		pVal[nPos] = SetVal(pVal, pPar, pPar[nPos]);
	}
	return	pVal[nPos];
}

int main()
{
	FILE* fp;
	int i, x, y;
	fp = fopen("1.txt", "r");

	int nRound = 0;
	fscanf(fp, "%d", &nRound);
	
	for(i=0; i<nRound; i++)
	{
		int nWidth, nHeight;
		fscanf(fp, "%d %d", &nHeight, &nWidth);

		int* pHei = (int*)malloc(nWidth*nHeight*sizeof(int));
		int* pPar = (int*)malloc(nWidth*nHeight*sizeof(int));
		char* pVal = (char*)malloc(nWidth*nHeight*sizeof(char));
		memset(pVal, 0, nWidth*nHeight*sizeof(char));
		int* pHeiT = pHei;
		for(y=0; y<nHeight; y++)
		{
			for(x=0; x<nWidth; x++, pHeiT++)
			{
				fscanf(fp, "%d", pHeiT);
			}
		}

		int nPos = 0;
		int nChar = 0;
		for(y=0; y<nHeight; y++)
		{
			for(x=0; x<nWidth; x++, nPos++)
			{
				int nHei = pHei[nPos];
				int nMinHei = 0xFFFFFF;
				int nMinPos;
				if(y>0)
				{
					if(pHei[nPos-nWidth]<nMinHei)
					{
						nMinHei = pHei[nPos-nWidth];
						nMinPos = nPos-nWidth;
					}
				}
				if(x>0)
				{
					if(pHei[nPos-1]<nMinHei)
					{
						nMinHei = pHei[nPos-1];
						nMinPos = nPos-1;
					}
				}
				if(x<nWidth-1)
				{
					if(pHei[nPos+1]<nMinHei)
					{
						nMinHei = pHei[nPos+1];
						nMinPos = nPos+1;
					}
				}
				if(y<nHeight-1)
				{
					if(pHei[nPos+nWidth]<nMinHei)
					{
						nMinHei = pHei[nPos+nWidth];
						nMinPos = nPos+nWidth;
					}
				}

				if(nMinHei<nHei)
				{
					pPar[nPos] = nMinPos;
				}
				else
				{
					pPar[nPos] = nPos;
					pVal[nPos] = 'a'+nChar;
					nChar++;
				}
			}
		}
		nPos = 0;
		for(y=0; y<nHeight; y++)
		{
			for(x=0; x<nWidth; x++, nPos++)
			{
				SetVal(pVal, pPar, nPos);
			}
		}
		
		char* pMask = (char*)malloc(nChar*sizeof(char));
		int* pMinPos = (int*)malloc(nChar*sizeof(int));
		for(x=0; x<nChar; x++)
		{
			pMask[x] = x;
			pMinPos[x] = 0xFFFFFF;
		}
		nPos = 0;
		for(y=0; y<nHeight; y++)
		{
			for(x=0; x<nWidth; x++, nPos++)
			{
				if(nPos<pMinPos[pVal[nPos]-'a'])
				{
					pMinPos[pVal[nPos]-'a'] = nPos;
				}
			}
		}

		for(y=0; y<nChar; y++)
		{
			for(x=0; x<nChar; x++)
			{
				if(pMinPos[y]<pMinPos[x])
				{
					int nTmp;
					nTmp = pMinPos[y];
					pMinPos[y] = pMinPos[x];
					pMinPos[x] = nTmp;
					nTmp = pMask[y];
					pMask[y] = pMask[x];
					pMask[x] = nTmp;
				}
			}
		}
		printf("Case #%d:\n", i+1);
		nPos = 0;
		for(y=0; y<nHeight; y++)
		{
			for(x=0; x<nWidth; x++, nPos++)
			{
				printf("%c ", pMask[pVal[nPos]-'a']+'a');
			}
			printf("\n");
		}

		free(pMask);
		free(pHei);
		free(pPar);
		free(pVal);
	}
	



	fclose(fp);
	return 0;
}