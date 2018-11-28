#include <stdio.h>
#include <string.h>

const int MAXSIZE=32;
int nResult[100];
int nCase;
char strString[20]="welcome to code jam";

void checkSentence(char *strSentence, int n)
{
	int nJump[MAXSIZE];
	int nPosSentence=0;
	int nCount=0, i;

	if(*strSentence==strString[n])
	{
		if(n==18)
		{
			nResult[nCase]+=1;

			return;
		}

		n+=1;
	}

	while(*(strSentence+nPosSentence)!=NULL)
	{
		if(*(strSentence+nPosSentence)==strString[n])
			nJump[nCount++]=nPosSentence;

		nPosSentence+=1;
	}

	if(nCount==0) return;

	nPosSentence+=1;

	for(i=0;i<nCount;i++)
		checkSentence(strSentence+nJump[i], n);
}

int main()
{
	FILE *fpopen, *fpout;
	int nN;
	int nLength;
	int nPosSentence;
	char strSentence[MAXSIZE];
	int nJump[MAXSIZE];
	int nCount;
	int i, j;

	fpopen=fopen("C-small.in", "r");
	fpout=fopen("C-small.out", "w");

	fscanf(fpopen, "%d\n", &nN);

	for(i=0;i<nN;i++)
	{
		nResult[i]=0;
		nPosSentence=0;
		nCount=0;

		fgets(strSentence, MAXSIZE, fpopen);

		nLength=strlen(strSentence);

		nCase=i;

		while(*(strSentence+nPosSentence)!=NULL)
		{
			if(*(strSentence+nPosSentence)==strString[0])
				nJump[nCount++]=nPosSentence;

			nPosSentence+=1;
		}

		for(j=0;j<nCount;j++)
			checkSentence(&strSentence[nJump[j]], 0);
	}	

	for(i=0;i<nN;i++)
		fprintf(fpout, "Case #%d: %04d\n", i+1, nResult[i]%10000);

	fclose(fpout);
	fclose(fpopen);
	return 0;
}