#include <stdio.h>
#include <malloc.h>
#include <string.h>

int main()
{
	FILE* fp;
	FILE* fpW;
	int i, j, k;
	char pTmp[65535];
	fp = fopen("1.txt", "r");

	int nL, nD, nN;
	fscanf(fp, "%d %d %d", &nL, &nD, &nN);

	char* pData = (char*)malloc(nL*nD*sizeof(char)+1);
	int* pListOld = (int*)malloc(nD*sizeof(int));
	int* pListNew = (int*)malloc(nD*sizeof(int));
	for(i=0; i<nD; i++)
	{
		fscanf(fp, "%s", pData+i*nL);
	}
	for(i=0; i<nN; i++)
	{
		int nPos = 0;
		int bStop = 0;
		fscanf(fp, "%s", pTmp);
		int nCountOld = nD;
		int nCountNew = 0;
		for(j=0; j<nCountOld; j++)
		{
			pListOld[j] = j;
		}

		for(j=0; j<strlen(pTmp); j++)
		{
			if(pTmp[j]=='(')
			{
				bStop = 1;
			}
			else if(pTmp[j]==')')
			{
				bStop = 0;
				memcpy(pListOld, pListNew, nCountNew*sizeof(int));
				nCountOld = nCountNew;
				nCountNew = 0;
				nPos++;
			}
			else
			{
				for(k=0; k<nCountOld; k++)
				{
					if(pData[pListOld[k]*nL+nPos]==pTmp[j])
					{
						pListNew[nCountNew++] = pListOld[k];
					}
				}
				if(bStop==0)
				{
					memcpy(pListOld, pListNew, nCountNew*sizeof(int));
					nCountOld = nCountNew;
					nCountNew = 0;
					nPos++;
				}
			}
		}
		printf("Case #%d: %d\n", i+1, nCountOld);
	}
	free(pData);
	free(pListOld);
	free(pListNew);
	fclose(fp);
	return 0;
}