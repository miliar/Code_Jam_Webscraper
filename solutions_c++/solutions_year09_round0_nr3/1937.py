#include <stdio.h>
#include <conio.h>

#define  LIMIT_L		19
#define  LIMIT_D		500

#define  LIMIT_STR		65536

#define TRUE			1
#define FALSE			0

char czInputString[LIMIT_STR] = {0,};

char czRef[LIMIT_L] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m',};
int  nzPos[LIMIT_L][LIMIT_D];
int  nzCnt[LIMIT_L];
int getOneLineFromFile(FILE* pf,char* pczInput, int nLimit)
{
	int nByte  = NULL;
	int nCount = 0;

	while(TRUE) {
		nByte = fgetc(pf);
		if ((nByte == 10) || (nByte == EOF)) break;
		pczInput[nCount] = (char)(nByte&0xFF);
		if(++nCount > nLimit) return -1; //error case
	}
	return nCount;
}


/*/////////////////////////////////////*/

int  nCase,nRefCnt,nMax;
int nResultCnt = 0;
//int getCaseCount(int nDepth,int nPos,int* nCount);

int getCaseCount(int nDepth,int nPos)
{
	int i = 0;

	if(nDepth == LIMIT_L) {
		nResultCnt++;
		nResultCnt %= 10000;
		return 0;
	}

	for(i=0;i<nzCnt[nDepth];i++) {
		if(nzPos[nDepth][i] < nPos) continue;
		getCaseCount(nDepth+1,nzPos[nDepth][i]);
	}

	return 0;
}
/*/////////////////////////////////////*/

int main(int argc, char* argv[])
{
	int i,j,k,l;
	int ret;
	int loopCnt;

	FILE* pfInput  = NULL;
	FILE* pfOutput = NULL;

	if(argc > 2) pfOutput = fopen(argv[2],"w+");
	else		 pfOutput = fopen("output3.txt","w+");

	if(argc > 1) pfInput = fopen(argv[1],"r");
	else		 pfInput = fopen("input3.txt","r");
	
	if(pfInput == NULL) { printf("error in input file opening\n"); return -1;}
/*////////////////////////////////////////////////////////////////////////*/

	fscanf(pfInput,"%d", &nCase);
	fgetc(pfInput);

	for(loopCnt = 1; loopCnt <= nCase; loopCnt++) {
		nResultCnt = 0;
	//ref
		k = getOneLineFromFile(pfInput,czInputString,LIMIT_STR);

	// count
		for(i=0;i<LIMIT_L;i++) {
			l = 0;
			for(j = 0;j<k;j++) {
				if(czInputString[j] == czRef[i]) nzPos[i][l++] = j;
			}
			nzPos[i][l] = -1;nzCnt[i] = l;
		}
	//get 1line
		ret = getCaseCount(0,0);
//		printf("%04d\n",nResultCnt);
		fprintf(pfOutput,"Case #%d: %04d\n",loopCnt,nResultCnt);
	}
/*////////////////////////////////////////////////////////////////////////*/
	fclose(pfInput);
	fclose(pfOutput);
	return 0;
}

