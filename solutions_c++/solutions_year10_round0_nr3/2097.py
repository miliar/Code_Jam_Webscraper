// Minimum Scalar Product.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <afx.h>
#include <map>
#include <vector>
#include <stdlib.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{

	CStdioFile cstdfRead;
	CStdioFile cstdfWrite;
	wchar_t databuffer[16*1024];
	INT64 iNumOfCases;
	wchar_t * seps = L" ";
	wchar_t * pwcToken;

	INT64 iRounds;
	INT64 iSpace;
	INT64 iNumOfGroups;
	vector<INT64> vecQueue;
	vector<INT64> vecBoard;
	INT64 iVecIter;
	INT64 iTemp;
	INT64 iResult;
	wchar_t num[64];
	INT64 iOnBoard;

	cstdfRead.Open(L"D:\\C-small-attempt0.in.txt",CStdioFile::modeRead);
	cstdfWrite.Open(L"D:\\Projects\\2010\\CodeJam2010\\testout.txt",CStdioFile::modeCreate);
	cstdfWrite.Close();
	cstdfWrite.Open(L"D:\\Projects\\2010\\CodeJam2010\\testout.txt",CStdioFile::modeWrite);

	memset(databuffer,0,sizeof(databuffer));
	cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
	iNumOfCases = _wtoi(databuffer);
	
	for (int iIndex1 = 0;iIndex1 < iNumOfCases;iIndex1++)
	{
		vecQueue.clear();
		iVecIter = 0;
		iResult = 0;

		memset(databuffer,0,sizeof(databuffer));
		cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
		pwcToken = wcstok(databuffer,seps);
		iRounds = _wtoi64(pwcToken);
		pwcToken = wcstok(NULL,seps);
		iSpace = _wtoi64(pwcToken);
		pwcToken = wcstok(NULL,seps);
		iNumOfGroups = _wtoi64(pwcToken);

		memset(databuffer,0,sizeof(databuffer));
		cstdfRead.ReadString(databuffer,sizeof(databuffer)-1);
		pwcToken = wcstok(databuffer,seps);
		while(pwcToken!=NULL)
		{
			iTemp = _wtoi64(pwcToken);
			vecQueue.push_back(iTemp);
			pwcToken = wcstok(NULL,seps);
		}

		for (INT64 iIndex2 = 0;iIndex2 < iRounds;iIndex2++)
		{
			//board
			iOnBoard = 0;
			vecBoard.clear();
			while(iVecIter < vecQueue.size())
			{
				if (iOnBoard + vecQueue[iVecIter] <= iSpace)
				{
					vecBoard.push_back(vecQueue[iVecIter]);
					iResult += vecQueue[iVecIter];
					iOnBoard += vecQueue[iVecIter];
					iVecIter++;
				}
				else
				{
					break;
				}
			}
			//requeue
			for (INT64 iIndex3 = 0;iIndex3 < vecBoard.size();iIndex3++)
			{
				vecQueue.push_back(vecBoard[iIndex3]);
			}
		}

		_i64tow(iResult,num,10);
		memset(databuffer,0,sizeof(databuffer));
		wsprintf(databuffer,L"Case #%d: %s\n",iIndex1+1,num);
		cstdfWrite.WriteString(databuffer);

	}

	cstdfRead.Close();
	cstdfWrite.Close();
	return 0;
}

