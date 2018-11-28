// try1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"



unsigned long Run(unsigned long R, unsigned long K, int N, unsigned long *pGroup)
{
	if( K == 0 || R == 0 || N == 0)
		return 0;
	
	int n=0; //current GroupNo
	unsigned long nCurOnboardPeopleNum;
	unsigned long nCurOnboardGroupNum;
	unsigned long nTotalMoney=0;
	for (unsigned long r=0; r<R; r++)
	{
		for(nCurOnboardGroupNum = nCurOnboardPeopleNum = 0;nCurOnboardGroupNum < N;n= (n+1)% N)
		{
			if(nCurOnboardPeopleNum + pGroup[n] <= K)
			{
				//board group n
				nTotalMoney += pGroup[n];
				nCurOnboardPeopleNum += pGroup[n];
				nCurOnboardGroupNum++;
			}
			else
				break;
		}
	}

	return nTotalMoney;
}


int main(int argc, char* argv[])
{
	unsigned long R, K;		
	int N,nInputs;
	unsigned long *pGroup;
	FILE *f=fopen(argv[1],"rt");
	FILE *fout= fopen(argv[2],"wt");
	fscanf(f,"%d", &nInputs);
	int nLine=0;
	while(!feof(f) && nLine < nInputs)
	{
		fscanf(f,"%ul",&R);
		fscanf(f,"%ul",&K);
		fscanf(f,"%d", &N);
		pGroup = new unsigned long[N];
		for(unsigned long i=0; i < N; i++)
			fscanf(f,"%ul",pGroup+i);
		fprintf(fout,"Case #%d: %u\n", nLine+1,Run(R, K, N,pGroup));
		nLine++;
		delete pGroup;
	}
	fclose(f);
	fclose(fout);
	return 0;
}

