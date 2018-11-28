// Minimum Scalar Product.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <afx.h>
#include <map>
#include <vector>
#include <stdlib.h>

using namespace std;
int mat[100][100] ;
int line[100];
int func(int * line,int length,int iWin,BOOL & bRed,BOOL & bBlue)
{
	int iRet = 0;

	int iLast,iNowLength;
	if (length < iWin)
	{
		return iRet;
	}
	iLast = *line;
	iNowLength = 1;
	for (int i = 1;i<length;i++)
	{
		if (iLast == line[i])
		{
			iNowLength++;
			if (iNowLength>=iWin)
			{
				if (iLast == 1)
				{
					bRed = TRUE;
				}
				else if (iLast == 2)
				{
					bBlue = TRUE;
				}
			}
		}
		else
		{
			iLast = line[i];
			iNowLength = 1;
		}
	}
	if (bRed == TRUE)
	{
		iRet += 1;
	}
	if (bBlue == TRUE)
	{
		iRet +=2;
	}
	return iRet;
}
int _tmain(int argc, _TCHAR* argv[])
{

	CStdioFile cstdfRead;
	CStdioFile cstdfWrite;
	wchar_t databuffer[16*1024];
	INT64 iNumOfCases;
	wchar_t * seps = L" ";
	wchar_t * pwcToken;
	INT64 iTemp,iResult;
	int iSize,iWin;
	BOOL bRWin,bBWin;

	//cstdfRead.Open(L"A-large-practice.in.txt",CStdioFile::modeRead);
	cstdfRead.Open(L"test.txt",CStdioFile::modeRead);
	cstdfWrite.Open(L"out.txt",CStdioFile::modeCreate);
	cstdfWrite.Close();
	cstdfWrite.Open(L"out.txt",CStdioFile::modeWrite);

	memset(databuffer,0,sizeof(databuffer));
	cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
	iNumOfCases = _wtoi(databuffer);

	for (int iIndex1 = 0;iIndex1 < iNumOfCases;iIndex1++)
	{
		bBWin = FALSE;
		bRWin = FALSE;
		memset(mat,0,sizeof(mat));
		memset(databuffer,0,sizeof(databuffer));
		cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
		pwcToken = wcstok(databuffer,seps);
		iSize = _wtoi(pwcToken);
		pwcToken = wcstok(NULL,seps);
		iWin = _wtoi(pwcToken);
		for (int iIndex2 = 0;iIndex2<iSize;iIndex2++)
		{
			memset(databuffer,0,sizeof(databuffer));
			cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
			pwcToken = databuffer;
			pwcToken += iSize -1;
			int iTemp2 = iSize -1;
			for(int iIndex3 = 0;iIndex3<iSize;iIndex3++)
			{
				if (*pwcToken == L'R')
				{
					mat[iIndex2][iTemp2] = 1;
					iTemp2--;
				}
				else if (*pwcToken == L'B')
				{
					mat[iIndex2][iTemp2] = 2;
					iTemp2--;
				}
				pwcToken--;
			}
		}
		for (int iIndex4 = 0;iIndex4<iSize;iIndex4++)
		{
			int iIndex5,iLength;
			memset(line,0,sizeof(line));
			for (iIndex5 = 0;iIndex5<iSize;iIndex5++)
			{
				line[iIndex5] = mat[iIndex4][iSize-1-iIndex5];
			}
			iLength = iIndex5;
			func(line,iLength,iWin,bRWin,bBWin);
			memset(line,0,sizeof(line));
			for (iIndex5 = 0;iIndex5<iSize;iIndex5++)
			{
				line[iIndex5] = mat[iSize-1-iIndex5][iIndex4];
			}
			iLength = iIndex5;
			func(line,iLength,iWin,bRWin,bBWin);
			memset(line,0,sizeof(line));
			for (iIndex5 = 0;iIndex5<=iIndex4;iIndex5++)
			{
				line[iIndex5] = mat[iIndex5][iIndex4-iIndex5];
			}
			iLength = iIndex4+1;
			func(line,iLength,iWin,bRWin,bBWin);
			memset(line,0,sizeof(line));
			for (iIndex5 = 0;iIndex5<=iIndex4;iIndex5++)
			{
				line[iIndex5] = mat[iSize - iIndex5 -1][iSize-iIndex4+iIndex5-1];
			}
			iLength = iIndex4+1;
			func(line,iLength,iWin,bRWin,bBWin);
			memset(line,0,sizeof(line));
			for (iIndex5 = 0;iIndex5<iSize-iIndex4;iIndex5++)
			{
				line[iIndex5] = mat[iIndex5][iIndex4+iIndex5];
			}
			iLength = iSize - iIndex4;
			func(line,iLength,iWin,bRWin,bBWin);
			memset(line,0,sizeof(line));
			for (iIndex5 = 0;iIndex5<iSize;iIndex5++)
			{
				line[iIndex5] = mat[iIndex4+iIndex5][iIndex5];
			}
			iLength = iSize - iIndex4;
			func(line,iLength,iWin,bRWin,bBWin);
		}
		wchar_t num[64];
		if (bRWin == TRUE&&bBWin == TRUE)
		{
			wcscpy(num,L"Both");
		}
		else if(bBWin == TRUE)
		{
			wcscpy(num,L"Blue");
		}
		else if(bRWin == TRUE)
		{
			wcscpy(num,L"Red");
		}
		else
		{
			wcscpy(num,L"Neither");
		}
		memset(databuffer,0,sizeof(databuffer));
		wsprintf(databuffer,L"Case #%d: %s\n",iIndex1+1,num);
		cstdfWrite.WriteString(databuffer);
	}

	cstdfRead.Close();
	cstdfWrite.Close();
	return 0;
}

