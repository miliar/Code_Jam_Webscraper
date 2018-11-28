#include <stdio.h>

const int cL=15;
const int cD=5000;
const int cN=500;

int nL, nD, nN;
int nPosLetter, nPosProblem, nResult, nCount[cN];
int i, j;

char cLetter[cD][cL];
char cProblem[cL*2+cL*cD];

void checkLetter(int nCase)
{
	nPosProblem+=1;

	while(cProblem[nPosProblem]!=')')
	{
		if(cLetter[nCase][nPosLetter]==cProblem[nPosProblem]) nResult=1;

		nPosProblem+=1;
	}

	nPosProblem+=1;
}

int main()
{
	FILE *fpopen, *fp;

	fpopen=fopen("A-large.in", "r");
	fp=fopen("A-large.out", "w");

	fscanf(fpopen, "%d %d %d", &nL, &nD, &nN);
	for(i=0;i<nD;i++)
		fscanf(fpopen, "%s", cLetter[i]);

	for(i=0;i<nN;i++)
	{
		fscanf(fpopen, "%s", cProblem);

		for(j=0;j<nD;j++)
		{
			nPosLetter=0;
			nPosProblem=0;
			while(nPosLetter<nL)
			{
				nResult=0;
				if(cProblem[nPosProblem]=='(')
				{
					checkLetter(j);
					if(nResult==0) break;
				}
				else
				{
					if(cLetter[j][nPosLetter]!=cProblem[nPosProblem]) break;

					nPosProblem+=1;
				}
				nPosLetter+=1;
			}
			if(nPosLetter==nL) nCount[i]+=1;
		}
	}

	for(i=0;i<nN;i++)
		fprintf(fp, "Case #%d: %d\n", i+1, nCount[i]);

	fclose(fp);
	fclose(fpopen);
	return 0;
}