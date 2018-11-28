
#include <stdio.h>
#include <conio.h>
#include <string.h>

#define  LIMIT_L		15
#define  LIMIT_D		5000
#define  LIMIT_N		500

#define  LIMIT_STR		65536

#define TRUE			1
#define FALSE			0

char czInputString[LIMIT_STR] = {0,};


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
typedef struct _stDB{
	int nPos;
	int nCnt;
} stDBPos, *pstDBPos;

char czDBLang[LIMIT_D][LIMIT_L + 1] = {0,};

int  nCase,nRefCnt,nMax;

int checkMatchByte(char *czRef,char czDB,stDBPos stPos)
{
	int i;
	for(i=0;i<stPos.nCnt;i++) {
		if(czRef[stPos.nPos + i] == czDB) return TRUE;
	}
	return FALSE;
}

int checkMatchCase(char *czRef,char* czDB,pstDBPos pstPos)
{
	int i;

	for(i=0;i<LIMIT_L;i++) {
		if(czDB[i] == NULL) break;
		if(checkMatchByte(czRef,czDB[i],pstPos[i]) == FALSE) return FALSE;
	}

	if(i == 0) return FALSE;
	return TRUE;
}

void checkLangPos(int nLen,char *czInput, pstDBPos pstPos)
{
	int i,j=0;
	int nCase = 0;

	for(i=0;i<nLen;i++) {
		if(czInput[i] == '(') {
			i++;
			pstPos[j].nPos = i;
			pstPos[j].nCnt = 0;
			while(czInput[i] != ')') {
				pstPos[j].nCnt++;
				i++;
			}
		}
		else {
			pstPos[j].nPos = i;
			pstPos[j].nCnt = 1;
		}
		j++;
	}	

}

/*/////////////////////////////////////*/

int main(int argc, char* argv[])
{
	int i,j,k;
	int nResultCnt;
	stDBPos stzDBPos[LIMIT_D];

	FILE* pfInput  = NULL;
	FILE* pfOutput = NULL;

	if(argc > 2) pfOutput = fopen(argv[2],"w+");
	else		 pfOutput = fopen("output1.txt","w+");

	if(argc > 1) pfInput = fopen(argv[1],"r");
	else		 pfInput = fopen("input1.txt","r");
	
	if(pfInput == NULL) { printf("error in input file opening\n"); return -1;}
/*////////////////////////////////////////////////////////////////////////*/

	fscanf(pfInput,"%d %d %d",&nMax, &nRefCnt, &nCase);

//db제작
	for(i=0;i< nRefCnt;i++) 
		fscanf(pfInput,"%s",czDBLang[i]);

		
//get 1line
	for(i=0;i< nCase;i++) {
		fscanf(pfInput,"%s",czInputString);
		k = strlen(czInputString);
		checkLangPos(k,czInputString,stzDBPos);
		nResultCnt = 0;
		for(j = 0;j < nRefCnt; j++) {
			if(checkMatchCase(czInputString,czDBLang[j],stzDBPos)) {
				nResultCnt++;
			}
		}
		//결과 출력.
		printf("case %d: %d\n",i,nResultCnt);
		fprintf(pfOutput,"Case #%d: %d\n",i+1,nResultCnt);
	}


/*////////////////////////////////////////////////////////////////////////*/
	fclose(pfInput);
	fclose(pfOutput);
	return 0;
}

