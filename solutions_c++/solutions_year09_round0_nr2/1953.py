
#include <stdio.h>
#include <conio.h>

//////////////////////////////////////////
#define  LIMIT_H		100
#define  LIMIT_W		100

#define  LIMIT_STR		65536
char czInputString[LIMIT_STR] = {0,};


typedef struct _ST_COOD{
	int nX;
	int nY;
	int nDir;
	
} ST_COOD, *PST_COOD;

int  nzMap[LIMIT_W][LIMIT_H] = {-1,};
char czMap[LIMIT_W][LIMIT_H] = {-1,};
int nStackCnt = 0;
ST_COOD stStack[LIMIT_W*LIMIT_H];

/////////////////////////////////////////

#define TRUE			1
#define FALSE			0



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
ST_COOD getNextCood(ST_COOD stCood,int nWidth,int nHight) 
{
	int i;
	int nDepth[4] = {-1,-1,-1,-1};
	char cOcc[6] = {0,0,0,0,0,0};
	int nPrevDepth = nzMap[stCood.nX][stCood.nY];
	int nDir = 5;

	if(stCood.nY != 0)		   {nDepth[0] = nzMap[stCood.nX][stCood.nY - 1]; cOcc[0] = czMap[stCood.nX][stCood.nY - 1];}
	if(stCood.nX != 0)		   {nDepth[1] = nzMap[stCood.nX - 1][stCood.nY]; cOcc[1] = czMap[stCood.nX - 1][stCood.nY];}
	if(stCood.nX < nWidth - 1) {nDepth[2] = nzMap[stCood.nX + 1][stCood.nY]; cOcc[2] = czMap[stCood.nX + 1][stCood.nY];}
	if(stCood.nY < nHight - 1) {nDepth[3] = nzMap[stCood.nX][stCood.nY + 1]; cOcc[3] = czMap[stCood.nX][stCood.nY + 1];}

	//check depth
	for(i=0;i<4;i++) {
		if(nDepth[i] == -1) continue;

		if(nPrevDepth > nDepth[i]) {
			nPrevDepth = nDepth[i];
			nDir = i;
		}
//		else if (nPrevDepth == nDepth[i]) {
//			if(cOcc[nDir] != 0) nDir = i;
//		}
	}

	switch(nDir) {
		case 0: stCood.nY--; stCood.nDir = 0; break;
		case 1: stCood.nX--; stCood.nDir = 1; break;
		case 2: stCood.nX++; stCood.nDir = 2; break;
		case 3: stCood.nY++; stCood.nDir = 3; break;
		default: stCood.nDir = 5; break;
	}

	if(cOcc[nDir] != 0) stCood.nDir = 5;

	return stCood;
}

/*/////////////////////////////////////*/

int main(int argc, char* argv[])
{
	int i,j,k,case_id;
	int nCase,nWidth,nHight;
	int nDirec = 5;
	char cAlpha = 'a',cStackAlpha;
	ST_COOD stPos;

	FILE* pfInput  = NULL;
	FILE* pfOutput = NULL;

	if(argc > 2) pfOutput = fopen(argv[2],"w+");
	else		 pfOutput = fopen("output2.txt","w+");

	if(argc > 1) pfInput = fopen(argv[1],"r");
	else		 pfInput = fopen("input2.txt","r");
	
	if(pfInput == NULL) { printf("error in input file opening\n"); return -1;}
/*////////////////////////////////////////////////////////////////////////*/

	fscanf(pfInput,"%d", &nCase);
	for(case_id = 1; case_id <= nCase; case_id++) {
		cAlpha = 'a';
	//map
		fscanf(pfInput,"%d %d",&nHight,&nWidth);

		for(i = 0;i< nHight;i++) {
			for(j=0;j<nWidth;j++) {
				fscanf(pfInput,"%d",&(nzMap[j][i]));
				czMap[j][i] = 0;
			}
		}

	//generate
		for(j=0;j<nHight;j++) {
			for(i = 0;i< nWidth;i++) {
				if(czMap[i][j] != 0) continue;
				cStackAlpha = 0;
				stPos.nX = i; stPos.nY = j; stPos.nDir = 4;
				nStackCnt = 0;
				while(stPos.nDir != 5) {
					stStack[nStackCnt++] = stPos;
					stPos = getNextCood(stPos,nWidth,nHight);
					if(czMap[stPos.nX][stPos.nY] != 0) {
						cStackAlpha = czMap[stPos.nX][stPos.nY];
					}
				}
				if(cStackAlpha == 0) cStackAlpha = cAlpha++;
				for(k=0;k<nStackCnt;k++) {
					czMap[stStack[k].nX][stStack[k].nY] = cStackAlpha;
				}
			}
		}
	//Ãâ·Â
		fprintf(pfOutput,"Case #%d:\n",case_id);
		for(i=0;i<nHight;i++) {
			for(j=0;j<nWidth;j++) {
				fprintf(pfOutput,"%c ",czMap[j][i]);
			}
			fprintf(pfOutput,"\n");
		}

	}


/*////////////////////////////////////////////////////////////////////////*/
	fclose(pfInput);
	fclose(pfOutput);
	return 0;
}

