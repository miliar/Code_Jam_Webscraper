/*
 * nc.cpp
 *
 *  Created on: 2013. 2. 13.
 *      Author: freetskim
 */

#include <vector>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define U32	unsigned long long

//#define FILE_DBG
#ifdef FILE_DBG
#define TSSCANF(X)	fscanf(g_fp,"%d",X);
#define TSSCANF(X)	fscanf(g_fp,"%d",X);
#define TSSCANFU(X)	fscanf(g_fp,"%u",X);
#define TSSCANFS(X)	fscanf(g_fp,"%s",X);
#else
#define TSSCANF(X)	scanf("%d",X);
#define TSSCANF(X)	scanf("%d",X);
#define TSSCANFU(X)	scanf("%u",X);
#define TSSCANFS(X)	scanf("%s",X);
#endif

#define MAXVAL	(1<<18)
using namespace std;

////general
int g_nTotalCases = 0;
FILE * g_fp = NULL;
////specific
int g_arrMatrix[8][8];
char g_arrStatus[4][32] = {"Game has not completed","Draw","X won","O won"};

#define STATUS_XWON	2
#define STATUS_OWON	3
#define STATUS_DRAW	1
#define STATUS_NOTCOMPLETED	0

int doSpecificJob(int nTestCase)
{
	int nCnt;
	int nRow;
	int nStatus = 0;
	int nCheckComplete = 0;
	int nXCnt;
	int nOCnt;
	int nUncompletedCnt;
	char strBuff[256];

	for(nRow=0; nRow<4; nRow++) {
		TSSCANFS(strBuff);
		g_arrMatrix[nRow][0] = strBuff[0];
		g_arrMatrix[nRow][1] = strBuff[1];
		g_arrMatrix[nRow][2] = strBuff[2];
		g_arrMatrix[nRow][3] = strBuff[3];
	}
	nUncompletedCnt = 0;
	//////////////////////////////////////////////////
	////scan x axis
	for(nRow=0; nRow<4; nRow++) {
		nXCnt = 0;
		nOCnt = 0;
		for(nCnt=0; nCnt<4; nCnt++) {
			if(g_arrMatrix[nRow][nCnt]=='X') {
				nXCnt++;
			}else if(g_arrMatrix[nRow][nCnt]=='O') {
				nOCnt++;
			}else if(g_arrMatrix[nRow][nCnt]=='T') {
				nXCnt++;
				nOCnt++;
			}else if(g_arrMatrix[nRow][nCnt]=='.') {
				nUncompletedCnt++;
			}
		}
		////check
		if(nXCnt>=4) {
			nCheckComplete = 1;
			nStatus = STATUS_XWON;
			break;
		}else if(nOCnt>=4) {
			nCheckComplete = 1;
			nStatus = STATUS_OWON;
			break;
		}
	}
	if(nCheckComplete)
		goto LABEL_ENDOF_JOB;
	//////////////////////////////////////////////////
	////scan y axis
	for(nCnt=0; nCnt<4; nCnt++) {
		nXCnt = 0;
		nOCnt = 0;
		for(nRow=0; nRow<4; nRow++) {
			if(g_arrMatrix[nRow][nCnt]=='X') {
				nXCnt++;
			}else if(g_arrMatrix[nRow][nCnt]=='O') {
				nOCnt++;
			}else if(g_arrMatrix[nRow][nCnt]=='T') {
				nXCnt++;
				nOCnt++;
			}
		}
		////check
		if(nXCnt>=4) {
			nCheckComplete = 1;
			nStatus = STATUS_XWON;
			break;
		}else if(nOCnt>=4) {
			nCheckComplete = 1;
			nStatus = STATUS_OWON;
			break;
		}
	}
	if(nCheckComplete)
		goto LABEL_ENDOF_JOB;

	//////////////////////////////////////////////////
	////scan diagonal 1
	nXCnt = 0;
	nOCnt = 0;
	for(nCnt=0; nCnt<4; nCnt++) {
		if(g_arrMatrix[nCnt][nCnt]=='X') {
			nXCnt++;
		}else if(g_arrMatrix[nCnt][nCnt]=='O') {
			nOCnt++;
		}else if(g_arrMatrix[nCnt][nCnt]=='T') {
			nXCnt++;
			nOCnt++;
		}
	}
	////check
	if(nXCnt>=4) {
		nCheckComplete = 1;
		nStatus = STATUS_XWON;
	}else if(nOCnt>=4) {
		nCheckComplete = 1;
		nStatus = STATUS_OWON;
	}
	if(nCheckComplete)
		goto LABEL_ENDOF_JOB;

	//////////////////////////////////////////////////
	////scan diagonal 2
	nXCnt = 0;
	nOCnt = 0;
	for(nCnt=0; nCnt<4; nCnt++) {
		if(g_arrMatrix[nCnt][3-nCnt]=='X') {
			nXCnt++;
		}else if(g_arrMatrix[nCnt][3-nCnt]=='O') {
			nOCnt++;
		}else if(g_arrMatrix[nCnt][3-nCnt]=='T') {
			nXCnt++;
			nOCnt++;
		}
	}
	////check
	if(nXCnt>=4) {
		nCheckComplete = 1;
		nStatus = STATUS_XWON;
	}else if(nOCnt>=4) {
		nCheckComplete = 1;
		nStatus = STATUS_OWON;
	}
	if(nCheckComplete)
		goto LABEL_ENDOF_JOB;

	////check end
	if(nUncompletedCnt>0)
		nStatus = STATUS_NOTCOMPLETED;
	else
		nStatus = STATUS_DRAW;
LABEL_ENDOF_JOB:
	printf("Case #%d: %s\n",nTestCase,g_arrStatus[nStatus]);
	return 0;
}

int main(int nArgc, char * argv[])
{
	int nCnt;
#ifdef FILE_DBG
	g_fp = fopen("C:\\input.txt","r");
#endif
	TSSCANF(&g_nTotalCases);
	for(nCnt=0; nCnt<g_nTotalCases; nCnt++) {
		doSpecificJob(nCnt+1);
	}
#ifdef FILE_DBG
	fclose(g_fp);
#endif
	return 0;
}
